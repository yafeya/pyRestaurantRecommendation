from urllib.parse import quote, quote_plus
import hashlib
import json
import requests
from query import PositionQuery


if __name__ == '__main__':
    query1 = PositionQuery(city='北京', address='五道口 食堂', ak='jLKWXCmDwGdfddhBvaB0GmqBr8K5gwum',
                           sk='ZphXAtI0goU2aRcOGFpzPsWmZOY00UNa', tag='价格', records=30)
    # query2 = PositionQuery(city='北京', address='五道口 食堂', ak='jLKWXCmDwGdfddhBvaB0GmqBr8K5gwum',
    #                        sk='ZphXAtI0goU2aRcOGFpzPsWmZOY00UNa', records=15)

    print('Query1: ')
    query1_urls = query1.get_hashed_urls()
    for url in query1_urls:
        response = requests.get(url)
        print(response)

    # print('Query2: ')
    # query2_urls = query1.get_hashed_urls()
    # for url in query2_urls:
    #     response = requests.get(url)
    #     print(response)

