from RestaurantApiControllers import RestaurantsAllApiController, RestaurantsInAreaApiController
from responses import Restaurant
import time


if __name__ == '__main__':
    location = '39.999734144579,116.33970166089'
    ak = 'jLKWXCmDwGdfddhBvaB0GmqBr8K5gwum'
    sk = 'ZphXAtI0goU2aRcOGFpzPsWmZOY00UNa'

    controller = RestaurantsInAreaApiController(ak=ak, sk=sk)
    start_time = time.time()
    restaurants = controller.__get_restaurants__(location, '50,80')
    sort_items = controller.__sort_restaurants__(restaurants)
    end_time = time.time()

    for sort_item in sort_items:
        restaurant = sort_item.get('restaurant')
        score = sort_item.get('score')
        print(f'{restaurant.name}: {restaurant.price}. distance: {restaurant.distance}, score: {score}')
    print(f'use: {end_time-start_time}')
