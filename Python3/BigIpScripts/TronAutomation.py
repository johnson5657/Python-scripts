import sys
import socket
import urllib
import urllib2
import requests
import smtplib
# import winsound
import random
import time
import re
from bs4 import BeautifulSoup
from time import strftime

tron_username = 'yshemesh'
tron_password = 'Chang6m6!'
client = requests.session()

headers = {'Referer': 'https://tron.f5net.com/login/',
           'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
           'Referrer Policy': 'no-referrer-when-downgrade'}

Get_token = client.get("https://tron.f5net.com/login/?next=/", verify=False, headers=headers)
print
Get_token.cookies

headers.update({'Referer': 'https://tron.f5net.com/login/?next=/'})

post_Data = {'username': tron_username, 'password': tron_password,
             'csrfmiddlewaretoken': str(Get_token.cookies['csrftoken']), 'next': '/'}

# print clie.post("https://tron.f5net.com/login/",verify=False,params=post_Data,headers=headers).headers <==== print the response headers to the post request.
client.post("https://tron.f5net.com/login/", verify=False, data=post_Data, headers=headers)
cases = client.get("https://tron.f5net.com/sr/search/?owner=ene&product=ltm", verify=False)
casesHtml = BeautifulSoup(cases.content, 'html.parser')
casesHtml = casesHtml.body
print
casesHtml.prettify()
case_list = casesHtml.find_all('td')
cases_dict = {}

for i in xrange(0, len(case_list)):
    #    print case_list[i].get_text() + "this is"+str(i)
    if i % 9 == 0:
        cases_dict.update({case_list[i + 1].get_text().encode('ascii', 'ignore'): case_list[i + 6].get_text().encode(
            'ascii', 'ignore')})
        # print type(case_list[i+6].get_text())  <=== return the type on an object
        # print type(case_list[i+6].get_text().encode('ascii','ignore'))  <=== convert to string from unicode
"""
in this section we will scan the ENE Q for cases we find interesting and notify ourselfs with an EMail
please fill in the desire details for mail system
"""
mail_server = 'smtp.gmail.com'
mail_server_port = 587
mail_server_user = 'USERNAME'
mail_server_password = 'PASSWORD'
sending_mail_address = 'USERNAME@gmail.com'
recipient_mail = ['ye.shemesh@f5.com', 'd.farhi@f5.com']

Key_words = ['http', 'ssl', 'bgp', 'ospf', 'http2']

server = smtplib.SMTP(mail_server, mail_server_port)
server.ehlo()
server.starttls()
server.login(mail_server_user, mail_server_password)

for SrNumber, SrTitle in cases_dict.iteritems():
    for index in Key_words:
        if index.lower() in str(SrTitle).lower():
            print
            SrTitle + " ----" + SrNumber
            msg = """\

From: %s
To: %s
Subject: Q Watchdog new case = %s

Hello, Baba gem

New ticket opened: %s

This Notification brought to you by Johnny Automation and scripting Inc
            """ % (sending_mail_address, recipient_mail, SrTitle, SrNumber)
            try:
                server.sendmail(sending_mail_address, recipient_mail, msg)
            except:
                print
                "fail to send mail"

server.close()







