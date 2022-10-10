"""
彩票自动查询
"""
import json
from typing import List, Tuple
from unittest import TestCase

import requests


class A1500:
    TWO_COLOR = 1  # 双色球：6 + 1
    BIG_LOTTO = 2  # 大乐透：5 + 2

    @classmethod
    def arr2twin(cls, arr: List[int], kind: int = 1) -> Tuple[int, int]:
        s = 7 - kind
        a = 0
        b = 0
        for o in arr[:s]:
            a |= 1 << o
        for o in arr[s:]:
            b |= 1 << o
        return a, b

    @classmethod
    def compare(cls, ab: List[int], zx: List[int], kind: int = 1):
        a, b = A1500.arr2twin(ab, kind)
        x, y = A1500.arr2twin(zx, kind)
        m = a & x
        n = b & y
        return bin(m).count("1"), bin(n).count("1")

    @classmethod
    def fetch(cls, kind: int, sn):
        if kind == cls.TWO_COLOR:
            params = (
                ("transactionType", "10001002"),
                ("lotteryId", "1"),
                ("issue", sn),  # 2022015
            )
        else:
            params = (
                ("transactionType", "10001002"),
                ("lotteryId", "281"),
                ("issue", sn),  # 22015
            )

        headers = {"Referer": "https://www.zhcw.com/"}
        r = requests.get("https://jc.zhcw.com/port/client_json.php", headers=headers, params=params, cookies={})

        try:
            res: dict = json.loads(r.text)
            arr: list = res.get("frontWinningNum").split(" ")
            arr.extend(res.get("backWinningNum").split(" "))

            ret = [int(o) for o in arr]
            print("issue: %s, openTime: %s, %s" % (sn, res.get("openTime"), ret))
            return ret
        except Exception:
            print("error", sn)
            return [0, 0, 0, 0, 0, 0, 0]


class TestLottery(TestCase):
    def test_TWO_COLOR(self):
        myArr = [
            [11, 13, 15, 17, 19, 21, 1],
            [12, 14, 16, 18, 20, 22, 2],
        ]

        target = A1500.fetch(kind=A1500.TWO_COLOR, sn="2022015")

        for me in myArr:
            res = A1500.compare(me, target, kind=A1500.TWO_COLOR)
            print(res, me)

    def test_BIG_LOTTO(self):
        myArr = [
            [11, 13, 15, 17, 19, 21, 1],
            [12, 14, 16, 18, 20, 22, 2],
        ]

        target = A1500.fetch(kind=A1500.BIG_LOTTO, sn="22015")

        for me in myArr:
            res = A1500.compare(me, target, kind=A1500.BIG_LOTTO)
            print(res, me)

    def test_NTime(self):
        for i in range(2022010, 2022019 + 1):
            myArr = [
                [11, 13, 15, 17, 19, 21, 1],
                [12, 14, 16, 18, 20, 22, 2],
            ]

            target = A1500.fetch(kind=A1500.TWO_COLOR, sn=i)

            for me in myArr:
                res = A1500.compare(me, target, kind=A1500.TWO_COLOR)
                print(res, me)

            print()
