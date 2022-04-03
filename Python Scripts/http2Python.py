from hyper import HTTPConnection

conn = HTTPConnection('10.170.173.96:443')
conn.request('GET', '/get')
resp = conn.get_response()

print(resp.read())