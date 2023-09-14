import time

import requests
import json
from datetime import datetime
import pytz
from time import sleep


def add_to_activity(_authorization: str, _cookie: str, _batchid: str, _data: dict) -> int:
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7',
        'Authorization': _authorization,
        'Batchid': _batchid,
        'Connection': 'keep-alive',
        'Content-Length': '238',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': _cookie,
        'Host': 'elective.smbu.edu.cn',
        'Origin': 'https://elective.smbu.edu.cn',
        'Referer': f'https://elective.smbu.edu.cn/xsxk/elective/grablessons?batchId={_batchid}',
        'sec-ch-ua': '"Not/A)Brand";v="99", "Opera";v="101", "Chromium";v="115"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 OPR/101.0.0.0 (Edition Yx 05)',
    }

    url = 'https://elective.smbu.edu.cn/xsxk/elective/clazz/add'
    res = requests.post(url, data=_data,
                        headers=headers)
    # print(res.content.decode("UTF8"))
    return json.loads(res.content)['code']


if __name__ == '__main__':
    start_time = datetime.fromisoformat(input('Время в формате <ГГГГ-ММ-ДД ЧЧ:ММ:СС>:') + '+08:00')
    authorization = input('authorization: ')
    cookie = input('cookie: ')
    batchid = input('batchid: ')

    print()

    data = {
        'clazzType': input('clazzType: '),
        'clazzId': input('clazzId: '),
        'secretVal': input('secretVal: ')
    }

    print()

    diff = start_time - datetime.now(tz=pytz.timezone('PRC'))
    if diff.total_seconds() > 0:
        while diff.seconds > 180:
            print(f'До начала ещё {diff.seconds // 60} минут')
            time.sleep(60)
            diff = start_time - datetime.now(tz=pytz.timezone('PRC'))
        while diff.seconds > 20:
            print(f'До начала ещё {diff.seconds} секунд')
            time.sleep(10)
            diff = start_time - datetime.now(tz=pytz.timezone('PRC'))
        while 0 < diff.seconds <= 10:
            print(f'До начала ещё {diff.seconds} секунд')
            time.sleep(1)
            diff = start_time - datetime.now(tz=pytz.timezone('PRC'))

    cnt = 1
    print(f'Попытка {cnt}...')
    code = add_to_activity(_authorization=authorization,
                           _cookie=cookie,
                           _batchid=batchid,
                           _data=data)
    while code != 200:
        cnt += 1
        print(f'Ошибка {code}. Попытка {cnt}...')
        code = add_to_activity(_authorization=authorization,
                               _cookie=cookie,
                               _batchid=batchid,
                               _data=data)
        sleep(2)
    print('Успех!')
