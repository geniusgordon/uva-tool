import requests
from config import config
from login import login

def submit(s, pid, filename=None):
    url = config.get('url', 'submit')
    if not filename:
        filename = 'codes/%s.cpp' % pid
    with open(filename, 'r') as f:
        code = f.read()
    headers = {
        'Referer': url,
        'Accept-Charset': 'utf-8,ISO-8859-1',
        'Accept-Encoding': 'gzip,deflate',
        'Accept-Language': 'en-US,en;q=0.8',
        "Accept" : "text/html, application/xml, text/xml, */*",
    }
    data = {
        'localid': pid,
        'language': '5',
        'code': code,
    }
    r = s.post(url, data=data, headers=headers)
    print('Submit %s' % filename)

if __name__ == '__main__':
    submit()

