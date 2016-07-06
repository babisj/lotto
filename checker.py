#!/usr/bin/env python
# -*- coding: UTF-8 -*-

__author__ = "Jimmy Song <jihwan.song@gmail.com>"
__date__ = "2016/07/04"
__version__ = "1.0.0"
__version_info__ = (1, 0, 0)
__license__ = "GPL"

################################################################################
import sys
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import config
from lotto import Lotto

################################################################################
def usage():
    print('--------------------------------------------------')
    print('Usage:')
    print('  %s lottoNums recipient1 ... recipientN' % sys.argv[0])
    print('Example:')
    print('  %s \'1, 2, 3, 4, 5, 6\' alice@gmail.com bob@gmail.com eve@gmail.com' % sys.argv[0])
    print('--------------------------------------------------')
 
################################################################################
def sendResultViaGmail(lotto, recipients):
    msg = MIMEMultipart('alternative')
    msg['Subject'] = lotto.getSubject()
    msg.attach(MIMEText(lotto.getContent(), 'plain'))
    mailServer = smtplib.SMTP('smtp.gmail.com', 587)
    mailServer.ehlo()
    mailServer.starttls()
    mailServer.ehlo()
    mailServer.login(config.MY_EMAIL_ACCOUNT, config.MY_EMAIL_PASSWORD)
    for mailTo in recipients:
        del msg['To']
        msg['To'] = mailTo
        mailServer.sendmail(config.MY_EMAIL_ACCOUNT, mailTo, msg.as_string())
    mailServer.close()

################################################################################
if __name__ == '__main__':
    if len(sys.argv) == 1:
        usage()
        exit(1)
    else:
        lottoNums = sys.argv[1]
        recipients = sys.argv[2:]
        lotto = Lotto(lottoNums)
        sendResultViaGmail(lotto, recipients)
        exit(0)
