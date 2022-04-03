#!/usr/local/bin/python2.7

import urllib, json, sys, requests

alarms = []
response = urllib.urlopen("http://localhost:9200/websafe/alert/_search")
data = json.loads(response.read())
# dictionary_alarms = dict(data)
# print json.dumps(data,indent=3)
# for key,value in data.iteritems():
#       print key
#       if key=="hits":
# or k,v in value:
#                       print(k,v)
# for key,value in data.iteritems():
#       print key
#       if key=="hits":
# or k,v in value:
#                       print(k,v)
# for k, v in data.items():
#       if k == 'hits':
#               for alert in v['hits']:
#                       username = alert['_source'].get('username')
#                       if 'Unknown' in username:
#                               print('Alert: %s' % alert['_id'])
# import urllib, json
# f = open('file.json', 'r')
# data = json.loads(f.read())
# print json.dumps(data)
# print(type(data))
# one way
for k, v in data.items():
    if k == 'hits':
        for i in v['hits']:
            if 'fpmAlertDetails' in i['_source']:
                if 'username=*' or 'username=Unknown' in i['_source']['fpmAlertDetails']:
                    print(i['_source']['fpmAlertDetails'])
                    # print json.dumps(i['_source'],indent=1)
                    print(
                        "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    alarms.append(i['_id'])

# print alerts IDs
for i in alarms:
    print
    i
    requests.delete('http://localhost:9200/websafe/alert/' + i)
    print("alarm: " + i + "has been deleted from DB")

# second way
# for k, v in data.items():
#       if k == 'hits':
#               for alert in v['hits']:
#                       if not alert['_source']['query']:
#                               print('Alert: %s' % alert['_id'])


# import requests
# for i in alerts_id:
#       requests.delete('/endpoint/delete/' + i)


Yehonatan
Goldman | Enterprise
Network
Engineer
Working
days
Sunday - Thursday







