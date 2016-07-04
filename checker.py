#!/usr/bin/env python
# -*- coding: UTF-8 -*-

__author__ = "Jimmy Song <jihwan.song@gmail.com>"
__date__ = "2016/07/04"
__version__ = "1.0.0"
__version_info__ = (1, 0, 0)
__license__ = "GPL"

################################################################################
import sys
import urllib2
import ast
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

MY_LOTTO_NUM = '1, 2, 3, 4, 5, 6'

SUBJECTS = [
        '꽝, 당신은 이번에도 기부천사~', 
        '1등, 아~~ 무도 모르게~농협 본점으로 고고고~!!!', 
        '2등, 아까비~ 인생역전 한 끗 차이 ㅠㅠ', 
        '3등, 맥북하나 질러볼까?? ^^', 
        '4등, 5만원, 치킨 5마리~~ 오예~', 
        '5등, 5천원으로 한번 더 도전~~'
    ]

CONTENTS = [
        '꽝입니다. 다음 기회에...',
        '1등 당첨을 축하드립니다.',
        '2등 당첨을 축하드립니다.',
        '3등 당첨을 축하드립니다.',
        '4등 당첨을 축하드립니다.',
        '5등 당첨을 축하드립니다.'
    ]

################################################################################
def getLottoResult():
    global lastLotto, lottoResult
 
    lastLotto = ast.literal_eval(
        urllib2.urlopen(
            'http://lotto.kaisyu.com/api?method=get&type=python'
        ).read()
    )

    lottoResult = ast.literal_eval(
        urllib2.urlopen(
                'http://lotto.kaisyu.com/api?method=check&type=python&numlist=[[' 
                + MY_LOTTO_NUM.replace(' ','')
                + ']]'
        ).read()
    )[0][0]

################################################################################
def sendGmail():
    msg = MIMEMultipart('alternative')
    msg['To'] = 'jihwan.song@gmail.com'
    msg['Subject'] = '[로또] ' + SUBJECTS[lottoResult]
    msg.attach(MIMEText(
        CONTENTS[lottoResult] + '\n\n'
        '---------------------------------------------' + '\n'
        + '회차 : ' + str(lastLotto['gno']) + '\n'
        + '날짜 : ' + lastLotto['gdate'] + '\n'
        + '당첨 : ' + str(lastLotto['nums']) + ' + ' + str(lastLotto['bnum']) + '\n'
        + '수동 : [' + MY_LOTTO_NUM + ']\n'
        + '---------------------------------------------' + '\n\n'
        + '감사합니다.\n\n'
        + '- 민지 아빠', 
        'plain'))
    mailServer = smtplib.SMTP('smtp.gmail.com', 587)
    mailServer.ehlo()
    mailServer.starttls()
    mailServer.ehlo()
    mailServer.login('jihwan.song@gmail.com', 'xxxx xxxx xxxx xxxx')
    mailServer.sendmail('jihwan.song@gmail.com', 'jihwan.song@gmail.com', msg.as_string())
    mailServer.close()

################################################################################
if __name__ == '__main__':
    getLottoResult()
    sendGmail()
