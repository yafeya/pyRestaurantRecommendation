from RestaurantApiControllers import RestaurantsAllApiController, RestaurantsInAreaApiController
import time
import json
from rest_server import start_restful_server
from LocationPosition import LocationPosition


if __name__ == '__main__':
    # location = '39.999734144579,116.33970166089'
    # ak = 'jLKWXCmDwGdfddhBvaB0GmqBr8K5gwum'
    # sk = 'ZphXAtI0goU2aRcOGFpzPsWmZOY00UNa'
    #
    # controller = RestaurantsInAreaApiController(ak=ak, sk=sk)
    # start_time = time.time()
    # restaurants = controller.__get_restaurants__(location, '50,80')
    # end_time = time.time()
    #
    # j_restaurants = []
    # for restaurant in restaurants:
    #     j_restaurant = json.dumps(restaurant.to_json())
    #     j_restaurants.append(j_restaurant)
    # json_obj = json.dumps(j_restaurants)
    #
    # for restaurant in restaurants:
    #     print(f'{restaurant.name}: {restaurant.price}. distance: {restaurant.distance}')
    # print(f'use: {end_time-start_time}')
    start_restful_server()
