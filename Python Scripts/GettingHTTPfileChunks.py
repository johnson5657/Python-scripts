import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import base64
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

'''
this script will download ucs file from BIG-IP as known BIG_IP limit the download size of file to 1M
this script devide the file into 1M chunks and then download the file from BIg-IP 

'''

BIGIP = "10.171.70.67"
UCSNAME = "tmp_1.ucs"
Username = "admin"
Password = "kirti"
Base64Pharse = base64.b64encode((Username + ':' + Password).encode('ascii'))
Base64Pharse = str(Base64Pharse).split('b')[1]
Base64Pharse = Base64Pharse[1:len(Base64Pharse)-1]
headers = {'Authorization': 'Basic ' + str(Base64Pharse)}
session = requests.Session()
Response = session.get('https://' + BIGIP + '/mgmt/shared/file-transfer/ucs-downloads/' + UCSNAME, headers=headers,
                       verify=False)

ContentSofar = 0
ContentSize = (str(Response.headers['Content-Range']).split("/"))[1]
Range = (str(Response.headers['Content-Range']).split("/"))[0]
ChunkSize = int(Range.split("-")[1]) - int(Range.split("-")[0])
NumberOfChunks = int(int(ContentSize) / ChunkSize)
LastChunkSize = int(ContentSize) - NumberOfChunks * ChunkSize
f = open("Ucsfile.ucs", "a+b")
f.write(Response.content)
ContentSofar += ChunkSize
i = 1
while i < NumberOfChunks:
    NextChunkStart = ChunkSize + ContentSofar
    headers = {'Authorization': 'Basic ' + str(Base64Pharse),
               'Content-Range': str(ContentSofar + 1) + '-' + str(NextChunkStart) + '/' + str(ContentSize)}
    Response = session.get('https://' + BIGIP + '/mgmt/shared/file-transfer/ucs-downloads/' + UCSNAME, headers=headers,
                           verify=False)
    f.write(Response.content)
    ContentSofar += ChunkSize
    i += 1

headers = {'Authorization': 'Basic ' + str(Base64Pharse),
           'Content-Range': str(ContentSofar + 1) + '-' + str(int(ContentSize) - 1) + '/' + str(ContentSize)}
Response = session.get('https://' + BIGIP + '/mgmt/shared/file-transfer/ucs-downloads/' + UCSNAME, headers=headers,
                       verify=False)

f.write(Response.content)
f.close()
