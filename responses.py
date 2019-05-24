from LocationPosition import LocationPosition
import json


class Restaurant:
    name: str = ''
    location: LocationPosition = None
    distance: int
    time: int
    province: str = ''
    city: str = ''
    address: str = ''
    price: float = ''
    rating: float = ''


class Route:
    distance: int = 0
    time: int = 0


def map_to_restaurants(raw: str):
    restaurants = [Restaurant]

    if raw == '':
        raise ValueError

    try:
        json_response = json.loads(raw)

        if json_response.results is not None:
            for result in json_response.results:
                restaurant = Restaurant()
                restaurant.name = result.name
                restaurant.location = LocationPosition(latitude=result.location.lat, longitude=result.location.lng)
                restaurant.province = result.province
                restaurant.city = result.city
                restaurant.address = result.address
                restaurant.price = float(result.detail_info.price)
                restaurant.rating = float(result.detail_info.overall_rating)
                restaurants.append(restaurant)

    except ValueError:
        print('parse RestaurantQueryResult error')
    else:
        print('parse RestaurantQueryResult error')

    return restaurants


def map_to_place(raw: str):
    place = ''

    if raw == '':
        raise ValueError

    try:
        json_response = json.loads(raw)
        if json_response.result is not None:
            business = str(json_response.result.business)
            parts = business.split(',')
            if len(parts) > 0:
                place = parts[0]

    except ValueError:
        print('parse RestaurantQueryResult error')
    else:
        print('parse RestaurantQueryResult error')

    return place


def map_to_route(raw: str):
    route = Route()

    if raw == '':
        raise ValueError

    try:
        json_response = json.loads(raw)
        if json_response.result is not None \
                and json_response.result.routes is not None \
                and len(json_response.result.routes) > 0:
            route_response = json_response.result.routes[0]
            route.distance = route_response.distance
            route.time = route_response.duration

    except ValueError:
        print('parse RestaurantQueryResult error')
    else:
        print('parse RestaurantQueryResult error')

    return route
