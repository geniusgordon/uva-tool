import requests
from config import config
from login import login

def submit():
    url = config.get('url', 'submit')
    with open('429.cpp', 'r') as f:
        code = f.read()
    headers = {
        'Accept-Charset': 'utf-8,ISO-8859-1',
        'Accept-Encoding': 'gzip,deflate',
        'Accept-Language': 'en-US,en;q=0.8',
        'User-Agent' : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) \
                        AppleWebKit/537.17 (KHTML, like Gecko) \
                        Chrome/24.0.1312.57 Safari/537.17",
        "Accept" : "text/html, application/xml, text/xml, */*",
    }
    data = {
        'localid': '429',
        'language': '5',
        'code': code,
    }
    # files= {
    #     'codeupl': open('429.cpp', 'rb')
    # }
    s = login()
    # r = s.post(url, data=data, files=files)
    # r = s.post(url, data=data, headers=headers)
    r = requests.post('http://httpbin.org/post', data=data, headers=headers)
    print(r.content)

if __name__ == '__main__':
    submit()

