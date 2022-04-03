from f5.bigip import ManagementRoot
from f5.bigip.contexts import TransactionContextManager
import requests

bigip = ManagementRoot("10.171.70.67", "admin", "admin")

for i in range(1, 100):
    params = {'name': 'myTestVirtual' + str(i),
              'partition': 'Common',
              'destination': '192.168.184.' + str(i) + ':80',
              'mask': '255.255.255.255',
              'source': '0.0.0.0/32',
              'pool': 'BIG-IQ',
              'profiles': [
                  {'name': 'http'},
                  {'name': 'tcp'}
              ]
              }
    bigip.tm.ltm.virtuals.virtual.create(**params)
