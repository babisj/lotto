#!/usr/bin/env python
# -*- coding: UTF-8 -*-

__author__ = "Jimmy Song <jihwan.song@gmail.com>"
__date__ = "2016/07/04"
__version__ = "1.0.0"
__version_info__ = (1, 0, 0)
__license__ = "GPL"

################################################################################
import urllib2
import ast

################################################################################
class Lotto:
    _SUBJECTS = [
        '[로또] 꽝, 당신은 이번에도 기부천사~',
        '[로또] 1등, 아~~ 무도 모르게~농협 본점으로 고고고~!!!',
        '[로또] 2등, 아까비~ 인생역전 한 끗 차이 ㅠㅠ',
        '[로또] 3등, 맥북 하나 질러볼까?? ^^',
        '[로또] 4등, 5만 원, 치킨 5마리~~ 오예~',
        '[로또] 5등, 5천 원으로 한번 더 도전~~'
    ]
    _CONTENTS = [
        '꽝입니다. 다음 기회에...',
        '1등 당첨을 축하드립니다.',
        '2등 당첨을 축하드립니다.',
        '3등 당첨을 축하드립니다.',
        '4등 당첨을 축하드립니다.',
        '5등 당첨을 축하드립니다.'
    ]

    def __init__(self, myNums):
        self._myNums = myNums
        self._lastInfo = ast.literal_eval(
            urllib2.urlopen(
                'http://lotto.kaisyu.com/api?method=get&type=python'
            ).read()
        )
        self._rank = ast.literal_eval(
            urllib2.urlopen(
                    'http://lotto.kaisyu.com/api?method=check&type=python&numlist=[['
                    + myNums.replace(' ', '')
                    + ']]'
            ).read()
        )[0][0]

    def getSubject(self):
        return self._SUBJECTS[self._rank]

    def getContent(self):
        return \
            self._CONTENTS[self._rank] + '\n\n' \
            + '---------------------------------------------' + '\n' \
            + '회차 : ' + str(self._lastInfo['gno']) + '\n' \
            + '날짜 : ' + str(self._lastInfo['gdate']) + '\n' \
            + '당첨 : ' + str(self._lastInfo['nums']) + ' + ' + str(self._lastInfo['bnum']) + '\n' \
            + '수동 : [' + self._myNums + ']\n' \
            + '홈피 : https://www.nlotto.co.kr/\n' \
            + '---------------------------------------------' + '\n\n' \
            + '감사합니다.\n\n' \
            + '- 민지 아빠'
