# -*- coding: utf-8 -*-
__author__ = 'Субботин Андрей Владимирович'
import requests
import sqlite3
import gzip
import os
import json
import re
from datetime import datetime

CITY_LIST_FILE_URL = 'http://bulk.openweathermap.org/sample/city.list.json.gz'
_API_URL = 'https://api.darksky.net/forecast'

with open('./app.id', 'r') as f:
    _APP_ID = f.read()
print(_APP_ID)

class CheckEnv(object):
    def __init__(self, file_url = None, db_name = None):
        self.file_url = file_url
        self.db_name = db_name
        self.file_path = None
        self.file_create()

    def file_check(self):

        if self.file_url:
            file_exist = os.path.isfile(os.path.join(os.path.join(os.getcwd(), self.file_url.split('/')[-1])))

            if file_exist:
                return True
            else:
                return False

        elif self.db_name:
            file_exist = os.path.isfile(os.path.join(os.path.join(os.getcwd(), self.db_name)))

            if file_exist:
                return True
            else:
                return False

        else:
            print('Object is incorrect.')

    def file_create(self):

        if not self.file_check() and self.file_url:
            try:
                req = requests.get(self.file_url)
            except requests.RequestException as e:
                print('Bad internet connection. Exit.')
                exit(0)
            else:
                if req.status_code == 200:

                    with open(os.path.join(os.path.join(os.getcwd(), self.file_url.split('/')[-1])), 'wb') as f:
                        for pice in req:
                            f.write(pice)
                    self.file_path = os.path.join(os.path.join(os.getcwd(), self.file_url.split('/')[-1]))
                else:
                    raise requests.exceptions.HTTPError('Bad internet connection.')

        elif not self.file_check() and self.db_name:
            conn = sqlite3.connect(self.db_name)  # или :memory: чтобы сохранить в RAM
            cursor = conn.cursor()
            cursor.execute("""CREATE TABLE city_weather
                              (city_id_time PRIMARY KEY, city, country_code, date,
                               temp, summary)
                           """)
            self.file_path = os.path.join(os.getcwd(), self.db_name)
        else:
            print(f'File {self.file_url.split("/")[-1] if self.file_url else self.db_name} already exists.')
            self.file_path = os.path.join(os.path.join(os.getcwd(), self.file_url.split('/')[-1] if self.file_url else self.db_name))


class CityList(object):
    def __init__(self, user_city, citys_file, user_country=None):
        self.user_city = user_city
        self.user_country = user_country
        self.city_file = citys_file
        self.city_list = []
        self._search_param()

    def _search_param(self):


        with gzip.open(self.city_file.file_path, mode='r') as gzip_file:
            data = json.load(gzip_file)
        self.file_path = os.path.join(os.getcwd(), CITY_LIST_FILE_URL.split('/')[-1])

        for city in data:
            if re.findall(rf"[A-Z]*{self.user_city}[A-Z]*[a-z]*", city["name"]):
                if self.user_country and self.user_country == city["country"]:
                    d = datetime.today()
                    city['time'] = int(datetime(d.year, d.month, d.day, d.hour).timestamp())
                    self.city_list.append(city)
                if not self.user_country:
                    d = datetime.today()
                    city['time'] = int(datetime(d.year, d.month, d.day, d.hour).timestamp())
                    self.city_list.append(city)
        return self.city_list


class Forecast(object):
    def __init__(self, key, lat, lon, time=None, timeout=None, **queries):
        self._parameters = dict(key=key, latitude=lat, longitude=lon, time=time)
        self.current_forecat = self.refresh(timeout, **queries)

    @property
    def url(self):
        time = self._parameters['time']
        timestr = ',{}'.format(time) if time else ''
        uri_format = '{url}/{key}/{latitude},{longitude}{timestr}'

        return uri_format.format(url=_API_URL, timestr=timestr, **self._parameters)

    def refresh(self, timeout=None, **queries):
        self._queries = queries
        self.timeout = timeout
        request_params = {
            'params': self._queries,
            'headers': {'Accept-Encoding': 'gzip'},
            'timeout': timeout
        }

        try:
            response = requests.get(self.url, **request_params)
            response.encoding = 'UTF-8'

        except requests.RequestException as e:
            print('Bad internet connection. Exit.')
            exit(0)
        else:
            self.response_headers = response.headers
            if response.status_code is not 200:
                raise requests.exceptions.HTTPError('Bad response')
            return json.loads(response.text)


class WorkWithDB(object):
    def __init__(self, db_file, forecast=None, city=None):
        self.db_file = db_file
        self.user_citys = user_list_citys
        self.conn = sqlite3.connect(self.db_file.file_path)
        self.cur = self.conn.cursor()
        self.forecast = forecast
        self.city = city
        self.record = ''
        self.current_hour = str(int(datetime(datetime.today().year, datetime.today().month, datetime.today().day, datetime.today().hour).timestamp()))

    def insert_wether(self):
        if self.city:
            self.record = (str(self.city['id'])+'_' + str(self.forecast['time']), self.city['name'], self.city['country'], self.forecast['time'], self.forecast['temperature'], self.forecast['summary'])
            self.cur.execute("INSERT INTO city_weather VALUES (?,?,?,?,?,?)",  self.record)
            self.conn.commit()
            print('API answer:', self.record) if str(self.forecast['time']) == self.current_hour else None
            #print(self.current_hour, '!=', self.forecast['time'])

    def show_db(self):

        sql = "SELECT * FROM city_weather"
        self.cur.execute(sql)
        print(self.cur.fetchall())  # or use fetchone()

    def seek_records(self):

        d = datetime.today()
        id_current_hour: str = str(self.city['id']) + '_' + self.current_hour
        sql = "SELECT * FROM city_weather WHERE city_id_time=?"
        self.cur.execute(sql, [(id_current_hour)])
        return self.cur.fetchall()


if __name__ == '__main__':

    db_file = CheckEnv(db_name = 'SQLite.db')
    city_list_file = CheckEnv(file_url=CITY_LIST_FILE_URL)
    user_list_citys = CityList(user_city=input('Type your city name:\n').title(), user_country=input('Type your country code:\n').upper(), citys_file=city_list_file)

    if user_list_citys.city_list:

        for city_hourly in user_list_citys.city_list:
            show = WorkWithDB(db_file, city=city_hourly)
            answer = show.seek_records()
            if not answer:
                forecast = Forecast(_APP_ID, city_hourly['coord']['lat'], city_hourly['coord']['lon'], city_hourly['time'], 100, lang='en',
                         units='si').current_forecat

                for hourly_forecast in forecast["hourly"]["data"]:
                    save_f = WorkWithDB(db_file, hourly_forecast, city_hourly)
                    save_f.insert_wether()
            else:
                print('DB answer:', *answer)