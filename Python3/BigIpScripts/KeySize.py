from f5.bigip import ManagementRoot
from f5.bigip.contexts import TransactionContextManager
import requests
import json

client = requests.session()
headers = {'Authorization': 'Basic YWRtaW46YWRtaW4='}
BIGIP_ADDRESS = "172.29.52.88"
bigip = ManagementRoot(BIGIP_ADDRESS, "admin", "admin")

ssl_keys = bigip.tm.sys.crypto.keys.get_collection()
ssl_certs = bigip.tm.sys.crypto.certs.get_collection()
ssl_profiles = bigip.tm.ltm.profile.client_ssls.get_collection()
ssl_profiles_server = bigip.tm.ltm.profile.server_ssls.get_collection()
virtual_servers = bigip.tm.ltm.virtuals.get_collection()

# print(ssl_profiles)

SSL_KEYS = {}
SSL_CRT_KEY_SIZE = {}
SSL_PROFILES = {}
VSs = {}
# print(ssl_keys)
for i in ssl_keys:
    #    print(i.keySize)
    #    print(i.keySize)
    #    print(i.keyType)
    #    print(i.name)
    SSL_KEYS.update({i.name: i.keySize})

# print(ssl_certs)

for i in ssl_certs:
    # print(dir(i))
    # print(i.raw["apiRawValues"]["certificateKeySize"])
    #print(i.raw["name"])
    SSL_CRT_KEY_SIZE.update({i.raw["name"]: i.raw["apiRawValues"]["certificateKeySize"]})
# print(SSL_CRT_KEY_SIZE)



for i in ssl_profiles:
    SSL_PROFILES.update({i.raw["name"]: i.raw["cert"]})
for i in ssl_profiles_server:
    SSL_PROFILES.update({i.raw["name"]: i.raw["cert"]})

for i in virtual_servers:
    Profile_List = []
    # print(i.name)
    profiles = (str(i.profilesReference["link"]).replace("localhost", BIGIP_ADDRESS))
    # print(profiles)
    json_profiles = client.get(profiles, verify=False, headers=headers)
    js = json.loads(json_profiles.content)
    number_of_profile_vs = len(js["items"])
    # below loop is going over the item list and getting each profile full path per VS
    for j in range(0, number_of_profile_vs):
        Profile_List.append(js["items"][j]["name"])
    # update the Vss dictionary with VS name and the profile list of that VS
    VSs.update({i.name: Profile_List})
#    print(VSs)
#    Profile_List.clear()
# print(VSs)  # this will print the VS dictionary each VS and the profile configure for it .
# Checking the profile in VS agains the matched SSL profile and the key size been used
for i, j in VSs.items():
    for profileName, profilePath in SSL_PROFILES.items():
        #print(profileName)
        if profileName in j:
            #print(profileName, profilePath)
            for crtPath, keysize in SSL_CRT_KEY_SIZE.items():
                if profilePath == crtPath:
                    print("Virtual Server Name: " + i, "SSL profile name: " + profileName,
                          "Crt key size is: " + keysize,"Cert name:"+crtPath)
                    print("===================================================================================================")

