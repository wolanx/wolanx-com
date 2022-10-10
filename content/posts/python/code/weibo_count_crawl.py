"""
微博 爬虫 h5
"""
import csv
import json
from datetime import datetime
from typing import List

import requests

headers = {
    "authority": "m.weibo.cn",
    "cache-control": "max-age=0",
    "sec-ch-ua": '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "upgrade-insecure-requests": "1",
    "sec-ch-ua-mobile": "?0",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
    "sec-fetch-site": "same-origin",
    "sec-fetch-mode": "same-origin",
    "sec-fetch-dest": "empty",
    "accept-language": "en,zh-CN;q=0.9,zh;q=0.8,en-US;q=0.7,af;q=0.6,ja;q=0.5,zh-TW;q=0.4,la;q=0.3",
    # 'cookie': 'WEIBOCN_FROM=1110006030; loginScene=102003; SUB=_2A25y-TfnDeRhGeVK41UQ8S7Lzz6IHXVuAlmvrDV6PUJbkdAKLWfSkW1NTEtA_Urkv7JNgmgGTVTVITj6xeOphl6d; _T_WM=69757421964; XSRF-TOKEN=23a1b0; MLOGIN=1; M_WEIBOCN_PARAMS=luicode%3D10000011%26lfid%3D2304133487110742_-_WEIBO_SECOND_PROFILE_WEIBO%26fid%3D2304133487110742_-_WEIBO_SECOND_PROFILE_WEIBO%26uicode%3D10000011',
    "cookie": "_T_WM=24683125646; WEIBOCN_FROM=1110006030; SUB=_2A25y-TVYDeRhGeBI7FEQ9ijNyz6IHXVuAlsQrDV6PUJbkdAKLRDHkW1NRmOxFWD7ee5Fye5-VFZ9ydRfSCCQUqtL; SCF=AivwLb--nifIPsUdBUye_P4402HsByCCtKQgFaWLZK0H7Xwf7UvOjPSSm40hwFOPspLFLLBhb5IdFa6s0QmNq8Y.; SSOLoginState=1610433800; MLOGIN=1; M_WEIBOCN_PARAMS=luicode%3D10000011%26lfid%3D2304136673166102_-_WEIBO_SECOND_PROFILE_WEIBO%26fid%3D2304136673166102_-_WEIBO_SECOND_PROFILE_WEIBO%26uicode%3D10000011; XSRF-TOKEN=3b44db",
}


def getCards(page):
    params = (
        # ('containerid', '2304133487110742_-_WEIBO_SECOND_PROFILE_WEIBO'),
        ("containerid", "2304136673166102_-_WEIBO_SECOND_PROFILE_WEIBO"),
        ("page_type", "03"),
        ("page", str(page)),
    )

    response = requests.get(
        "https://m.weibo.cn/api/container/getIndex", headers=headers, params=params
    )
    print("page", page, response.status_code)

    obj = json.loads(str(response.content, encoding="utf-8"))
    return obj.get("data").get("cards")


class Blog:
    def __init__(self, map) -> None:
        self.data = map

    def raw_text(self):
        return self.data.get("raw_text")

    def reads_count(self):
        return self.data.get("reads_count")

    def reposts_count(self):
        return self.data.get("reposts_count")

    def comments_count(self):
        return self.data.get("comments_count")

    def attitudes_count(self):
        return self.data.get("attitudes_count")

    def obj_ext(self):
        return self.data.get("obj_ext")

    def created_at(self):
        ymd: str = self.data.get("created_at")
        if len(ymd) == 5:
            return datetime.strptime("2021-" + ymd, "%Y-%m-%d")
        else:
            return datetime.strptime(ymd, "%Y-%m-%d")


def doCards(cards):
    ret = []
    for card in cards:
        if card.get("card_type") == 9:
            mblog = Blog(card.get("mblog"))
            ret.append(mblog)

    return ret


objArr = []
for page in range(0, 80):
    cards = getCards(page + 1)
    arr = doCards(cards)
    for one in arr:
        objArr.append(one)


def doReport(arr: List[Blog]):
    with open("a.csv", "w", newline="", encoding="utf_8_sig") as f:
        f_csv = csv.writer(f)
        for one in arr:
            title = str.replace(one.raw_text(), "\n", "")
            print(
                one.reads_count(),
                one.reposts_count(),
                one.comments_count(),
                one.attitudes_count(),
                title[:30],
            )
            f_csv.writerow(
                [
                    one.created_at().strftime("%Y-%m-%d"),
                    one.reads_count(),
                    one.reposts_count(),
                    one.comments_count(),
                    one.attitudes_count(),
                    title,
                ]
            )


doReport(objArr)
