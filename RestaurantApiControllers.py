import requests
from query import InterestingQuery, InterestingRadiusQuery, PlaceQuery, RouteCalculationQuery
from LocationPosition import LocationPosition
from responses import map_to_place, map_to_route, map_to_restaurants, Restaurant
import json
from flask import jsonify


def get_favorites():
    f = open('favorites.json', encoding='utf-8')
    res = f.read()
    return res


class RestaurantsAllApiController:
    __ak__: str = ''
    __sk__: str = ''

    __rating_weight__ = 75
    __price_weight__ = 36
    __distance_weight__ = 24

    def __init__(self, ak: str, sk: str):
        if ak is None or ak == '':
            raise ValueError

        if sk is None or sk == '':
            raise ValueError

        self.__ak__ = ak
        self.__sk__ = sk

    def get(self, location: str, price_section: str, result_count: int):
        if location is None or location == '':
            return 'location invalidate', 500

        try:
            restaurants = self.__get_restaurants__(location, price_section)
            sorted_restaurants = self.__sort_restaurants__(restaurants, result_count)
            restaurant_list = []
            for restaurant in sorted_restaurants:
                j_obj = restaurant.get('restaurant').to_json()
                restaurant_list.append(j_obj)

            return jsonify(restaurant_list), 200
        except IOError:
            print('RestaurantRecommendationApiController Error when get')
            return 'Error happens', 500
        else:
            return 'Error happens', 500

    def __sort_restaurants__(self, restaurants: [], result_count: int = 10):
        target_list = []
        for restaurant in restaurants:
            score = self.__generate_scores__(restaurant)
            target = {'restaurant': restaurant, 'score': score}
            target_list.append(target)
        target_list.sort(key=lambda x: x['score'], reverse=True)
        # for x in target_list:
        #     r = x.get('restaurant')
        #     s = x.get('score')
        #     print(f'{r.name}, score: {s}')
        copy_count = result_count if len(target_list) > result_count else len(target_list)
        copy_items = []
        for index in range(0, copy_count):
            copy_items.append(target_list[index])
        return copy_items

    def __generate_scores__(self, restaurant: Restaurant):
        score = (restaurant.rating / 5) * self.__rating_weight__ \
                + (1 - restaurant.price / 200) * self.__price_weight__ \
                + (1 - restaurant.distance / 2000) * self.__distance_weight__
        return score

    def __fill_restaurant_details__(self, origin_location, restaurant):
        query_routing = RouteCalculationQuery(start=origin_location, destination=restaurant.location,
                                              ak=self.__ak__, sk=self.__sk__)
        url = query_routing.get_hashed_url()
        response_routing = requests.get(url)
        detail_response = map_to_route(response_routing.text)
        restaurant.distance = detail_response.distance
        restaurant.time = detail_response.time

    def __get_restaurants__(self, location, price_section: str):
        parts = location.split(',')
        if len(parts) <= 0 or len(parts) > 2:
            raise IOError

        restaurants_list = []

        origin_location = LocationPosition(latitude=float(parts[0]), longitude=float(parts[1]))
        query_place = PlaceQuery(location=location, ak=self.__ak__, sk=self.__sk__)
        response_place = requests.get(query_place.get_hashed_url())
        place = map_to_place(response_place.text)
        address = '{0} 食堂'.format(place['area'])
        tag = '价格'
        query_restaurant = InterestingQuery(city=place['city'], address=address,
                                            ak=self.__ak__, sk=self.__sk__, tag=tag, records=100,
                                            price_section=price_section)

        favorites = get_favorites()
        if favorites is not None:
            self.__fill_restaurant_list__(origin_location, restaurants_list, favorites)

        urls = query_restaurant.get_hashed_urls()
        for url in urls:
            restaurants_response = requests.get(url)
            self.__fill_restaurant_list__(origin_location, restaurants_list, restaurants_response.text)

        return restaurants_list

    def __fill_restaurant_list__(self, origin_location, restaurants_list, restaurants_raw):
        restaurants = map_to_restaurants(restaurants_raw)
        for restaurant in restaurants:
            self.__fill_restaurant_details__(origin_location, restaurant)
            restaurants_list.append(restaurant)


class RestaurantsInAreaApiController(RestaurantsAllApiController):

    def __get_restaurants__(self, location: str, price_section: str = '0,35'):
        parts = location.split(',')
        if len(parts) <= 0 or len(parts) > 2:
            raise IOError

        restaurants_list = []

        origin_location = LocationPosition(latitude=float(parts[0]), longitude=float(parts[1]))
        tag = '食堂'
        query_restaurant = InterestingRadiusQuery(tag=tag, location=location, radius=1500,
                                                  ak=self.__ak__, sk=self.__sk__, records_count=100,
                                                  price_section=price_section)

        favorites = get_favorites()
        if favorites is not None:
            self.__fill_restaurant_list__(origin_location, restaurants_list, favorites)

        urls = query_restaurant.get_hashed_urls()
        for url in urls:
            restaurants_response = requests.get(url)
            self.__fill_restaurant_list__(origin_location, restaurants_list, restaurants_response.text)

        return restaurants_list
