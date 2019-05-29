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
    price: float = 0
    rating: float = 0

    def to_json(self):
        return {
            'name': self.name,
            'location': self.location.to_json(),
            'distance': self.distance,
            'time': self.time,
            'province': self.province,
            'city': self.city,
            'address': self.address,
            'price': self.price,
            'rating': self.rating
        }


class Route:
    distance: int = 0
    time: int = 0


def map_to_restaurants(raw: str):
    restaurants = []

    if raw == '':
        raise ValueError

    try:
        json_response = dict(json.loads(raw))

        if json_response.__contains__('results') and json_response['results'] is not None:
            results = json_response['results']
            for result in results:
                restaurant = Restaurant()
                restaurant.name = result['name']
                restaurant.location = LocationPosition(latitude=result['location']['lat'],
                                                       longitude=result['location']['lng'])
                restaurant.province = result['province']
                restaurant.city = result['city']
                restaurant.address = result['address']
                detail_info = dict(result['detail_info'])
                restaurant.price = float(detail_info.get('price')) \
                    if detail_info.__contains__('price') else 0
                restaurant.rating = float(detail_info.get('overall_rating')) \
                    if detail_info.__contains__('overall_rating') else 0
                restaurants.append(restaurant)

    except ValueError:
        print('parse RestaurantQueryResult error')

    return restaurants


def map_to_place(raw: str):
    area = ''
    city = ''

    if raw == '':
        raise ValueError

    try:
        json_response = json.loads(raw)
        result = json_response['result']
        if result is not None:
            business = str(result['business'])
            parts = business.split(',')
            city = result['addressComponent']['city']
            if len(parts) > 0:
                area = parts[0]

    except ValueError:
        print('parse RestaurantQueryResult error')

    return {'city': city, 'area': area}


def map_to_route(raw: str):
    route = Route()

    if raw == '':
        raise ValueError

    try:
        json_response = json.loads(raw)
        result = json_response['result']
        if result is not None \
                and result['routes'] is not None \
                and len(result['routes']) > 0:
            routes = result['routes']
            route_response = routes.pop(0)
            route.distance = route_response['distance']
            route.time = route_response['duration']

    except ValueError:
        print('parse RestaurantQueryResult error')

    return route
