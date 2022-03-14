import sys
import urllib
import requests
import smtplib
import time
import os.path

from BeautifulSoup import BeautifulSoup
from time import strftime

# Disable SSL warnings
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# User credentials
f5_username = 'ye.esh'
f5_password = 'your_password'
f5_emailaddr = 'ye.shemesh@f5.com'

# Tron URls
tron_url_1 = 'https://tron.f5net.com'
tron_url_2 = 'https://tron.stg.f5net.com'
tron_login = '%s/login' % tron_url_2
tron_product = 'LTM'
tron_ene_queue = "%s/sr/search/?owner=ENE&originator=&abstract=&created=&last-modified=&status=&substatus=" \
                 "&product=%s&sr=&contact=&serial=&account=&site=&area=&subarea=" \
                 % (tron_url_2, tron_product)

# SMTP
smtpserver = 'owa.f5.com'

# Queue Interval in seconds
queue_check_interval = 5

# Cases database
db = 'cases.db'

# Which string do you to search for in the SR subject? use lowercase
custom_search_string = 'http'


def sendmail(SR, BODY):
    FROM = f5_emailaddr

    TO = [f5_emailaddr]

    SUBJECT = "Q Watchdog - New HTTP LTM Ticket (%s)" % SR

    message = """\
From: %s
To: %s
Subject: %s


Hello,

New ticket opened: %s

F5 Support

""" % (FROM, ", ".join(TO), SUBJECT, BODY)

    server = smtplib.SMTP('owa.f5.com')
    server.sendmail(FROM, TO, message)
    server.quit()


def main():
    if os.path.exists(db):
        append_write = 'a'
    else:
        append_write = 'w+'

    print("Tron Queue Leading Monitor started...")
    while True:
        curtime = strftime("[%H:%M:%S]")
        print("%s Checking queue..." % curtime)
        """Since VPN disconnects quite often, resolve check before every attempt"""
        try:
            if urllib.urlopen(tron_url_1).getcode() == 200:
                client = requests.session()
                client.get(tron_login, verify=False)
                csrftoken = client.cookies['csrftoken']
                login_data = dict(username=f5_username, password=f5_password, csrfmiddlewaretoken=csrftoken, next='/')
                r = client.post(tron_login, data=login_data, headers=dict(Referer=tron_login))
                r = client.get(tron_ene_queue)
                soup = BeautifulSoup(r.text)

                table = soup.find("table", {"class": "sr-list queue"})
                for row in table.findAll('tr')[1:]:
                    col = row.findAll('td')
                    sr = col[0].find('a').get('href').split('/')[2]
                    customer = col[7].find('a').string
                    severity = col[3].string
                    version = col[5].string
                    description = col[6].string.strip()

                    if custom_search_string in description.lower():
                        if sr not in open(db, append_write).read():
                            with open(db, append_write) as dbfile:
                                dbfile.write(sr + '\n')
                            print("Sending email: %s, %s" % (sr, description))
                            sendmail(sr, description)
        except Exception as e:
            print
            e
        finally:
            time.sleep(queue_check_interval)


if __name__ == '__main__':
    main()








