from urllib.parse import quote, quote_plus
import hashlib
import json
import requests
from query import InterestingQuery, PlaceQuery, IpLocationQuery, RouteCalculationQuery
from LocationPosition import LocationPosition


if __name__ == '__main__':
    # query_interesting = InterestingQuery(city='北京', address='五道口 食堂', ak='jLKWXCmDwGdfddhBvaB0GmqBr8K5gwum',
    #                        sk='ZphXAtI0goU2aRcOGFpzPsWmZOY00UNa', tag='价格', records=1)
    #
    # url_interesting = query_interesting.get_hashed_urls()
    # print('Interesting Query Response:')
    # for url in url_interesting:
    #     response = requests.get(url)
    #     print(response.text)
    #     break
    #
    # print('Place Query Response:')
    # location = '39.999734144579,116.33970166089'
    # query_place = PlaceQuery(location, ak='jLKWXCmDwGdfddhBvaB0GmqBr8K5gwum', sk='ZphXAtI0goU2aRcOGFpzPsWmZOY00UNa')
    # url_place = query_place.get_hashed_url()
    # response = requests.get(url_place)
    # print(response.text)

    # print('Route Calculation Query Response')
    # start = LocationPosition(latitude=39.999232, longitude=116.345447)
    # destination = LocationPosition(latitude=39.998654488535, longitude=116.34518331155)
    # query_route_cal = RouteCalculationQuery(start=start, destination=destination,
    #                               ak='jLKWXCmDwGdfddhBvaB0GmqBr8K5gwum', sk='ZphXAtI0goU2aRcOGFpzPsWmZOY00UNa')
    # url_route_cal = query_route_cal.get_hashed_url()
    # response = requests.get(url_route_cal)
    # print(response.text)

    import json

    d = {"a": 1, "b": 2}
    print(d)
    f = json.dumps(d)
    print(type(f))
    print(f)
    e = json.loads(f)
    print(type(e))
    print(e)

