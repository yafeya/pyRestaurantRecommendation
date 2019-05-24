from urllib.parse import quote, quote_plus
import hashlib
from LocationPosition import LocationPosition
import time


class Query:
    domain_url = 'http://api.map.baidu.com'
    ak: str = ''
    sk: str = ''
    query_format = '{0}&output=json&ak={1}'

    # the url between domain url & output part
    # e.g. http://api.map.baidu.com/place/v2/search?query=<query>机&tag=<tag>&region=<city>&output=json&ak=<ak>
    #       the query_url for above url is 'place/v2/search?query=<query>机&tag=<tag>&region=<city>'
    def __get_hashed_url__(self, query_url: str):
        if self.ak == '' or self.sk == '' or query_url == '':
            raise ValueError

        query_str = self.__get_query_str__(query_url)
        encoded_str = quote(query_str, safe="/:=&?#+!$,;'@()*[]")
        raw_str = encoded_str + self.sk
        sn = hashlib.md5(quote_plus(raw_str).encode('utf8')).hexdigest()
        url = quote(self.domain_url + query_str + '&sn=' + sn, safe="/:=&?#+!$,;'@()*[]")
        return url

    def __get_query_str__(self, query_url):
        query_str = f'{query_url}&output=json&ak={self.ak}'
        return query_str


class InterestingQuery(Query):
    __city__: str = ''
    __address__: str = ''
    __tag__: str = ''
    __record_count__: int = 100
    __page_size__: int = 20

    def __init__(self, city: str, address: str, ak: str = '', sk: str = '', tag: str = '', records: int = 100):
        self.__city__ = city
        self.__address__ = address
        self.__tag__ = tag
        self.__record_count__ = records
        self.ak = ak
        self.sk = sk

    def __get_query_url__(self, page_num: int):
        page_size = self.__record_count__ if self.__record_count__ < self.__page_size__ else self.__page_size__
        query_url = f'/place/v2/search?query={self.__address__}&tag={self.__tag__}&region={self.__city__}' \
            f'&scope=2&page_size={page_size}&page_num={page_num}' \
            if self.__tag__ != '' else \
            f'place/v2/search?query={self.__address__}&region={self.__city__}&scope=2&page_size={page_size}' \
            f'&page_num={page_num}'

        return query_url

    def get_hashed_urls(self):
        page_count = int(self.__record_count__ / self.__page_size__)\
            if self.__record_count__ % self.__page_size__ == 0 \
            else int(self.__record_count__ / self.__page_size__) + 1

        url_list: list = list()

        for page_num in range(1, page_count + 1):
            query_url = self.__get_query_url__(page_num)
            hashed_url = self.__get_hashed_url__(query_url)
            url_list.append(hashed_url)

        return url_list


class PlaceQuery(Query):

    __location__: str = ''

    def __init__(self, location: str, ak: str = '', sk: str = ''):
        self.__location__ = location

        if ak != '':
            self.ak = ak

        if sk != '':
            self.sk = sk

    def __get_query_url__(self):
        query_url = f'/geocoder/v2/?location={self.__location__}'

        return query_url

    def get_hashed_url(self):
        query_url = self.__get_query_url__()
        hashed_url = self.__get_hashed_url__(query_url)
        return hashed_url


class IpLocationQuery(Query):
    __ip__: str = ''

    def __init__(self, ip, ak: str = '', sk: str = ''):
        self.__ip__ = ip
        if ak != '':
            self.ak = ak
        if sk != '':
            self.sk = sk

    def __get_query_str__(self, query_url):
        query_str = f'{query_url}&ak={self.ak}&coor=bd09ll'
        return query_str

    def __get_query_url__(self):
        query_url = f'/location/ip?ip={self.__ip__}'

        return query_url

    def get_hashed_url(self):
        query_url = self.__get_query_url__()
        hashed_url = self.__get_hashed_url__(query_url)
        return hashed_url


class RouteCalculationQuery(Query):
    __start__: LocationPosition = None
    __destination__: LocationPosition = None

    def __init__(self, start: LocationPosition, destination: LocationPosition, ak: str = '', sk: str = ''):
        if start is None or destination is None:
            raise ValueError

        self.__start__ = start
        self.__destination__ = destination

        if ak != '':
            self.ak = ak

        if sk != '':
            self.sk = sk

    def __get_query_url__(self):
        query_url = f'/directionlite/v1/walking?origin={self.__start__.get_location()}' \
            f'&destination={self.__destination__.get_location()}' \
            f'&timestamp={int(time.time())}'

        return query_url

    def __get_query_str__(self, query_url):
        query_str = f'{query_url}&ak={self.ak}'
        return query_str

    def get_hashed_url(self):
        query_url = self.__get_query_url__()
        hashed_url = self.__get_hashed_url__(query_url)
        return hashed_url

