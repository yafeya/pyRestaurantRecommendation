from abc import abstractmethod
from urllib.parse import quote, quote_plus
import hashlib


class Query:
    domain_url = 'http://api.map.baidu.com'
    ak: str = ''
    sk: str = ''

    # the url between domain url & output part
    # e.g. http://api.map.baidu.com/place/v2/search?query=<query>机&tag=<tag>&region=<city>&output=json&ak=<ak>
    #       the query_url for above url is 'place/v2/search?query=<query>机&tag=<tag>&region=<city>'
    def __get_hashed_url__(self, query_url: str):
        if self.ak == '' or self.sk == '' or query_url == '':
            raise ValueError

        query_str = f'{query_url}&output=json&ak={self.ak}'
        encoded_str = quote(query_str, safe="/:=&?#+!$,;'@()*[]")
        raw_str = encoded_str + self.sk
        sn = hashlib.md5(quote_plus(raw_str).encode('utf8')).hexdigest()
        url = quote(self.domain_url + query_str + '&sn=' + sn, safe="/:=&?#+!$,;'@()*[]")
        return url


class PositionQuery(Query):
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
        query_url = f'/place/v2/search?query={self.__address__}&tag={self.__tag__}&region={self.__city__}' \
            f'&scope=2&page_size={self.__page_size__}&page_num={page_num}' \
            if self.__tag__ != '' else \
            f'place/v2/search?query={self.__address__}&region={self.__city__}&scope=2&page_size={self.__page_size__}' \
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

