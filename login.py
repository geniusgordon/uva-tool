import os
import pickle
import requests

from config import config
from pyquery import PyQuery

def get_user():
    user = config.items('user')
    return (user[0][1], user[1][1])

def get_data():
    url = config.get('url', 'index')
    r = requests.get(url)
    pq = PyQuery(r.content)
    fields = pq('form input')
    hidden = []
    for f in fields:
        if f.attrib['type'] == 'hidden':
            hidden.append((f.attrib['name'], f.attrib['value']))
    data = dict(hidden)
    user = get_user()
    data['username'] = user[0]
    data['passwd'] = user[1]
    data['remember'] = 'yes'

    return data

def login():
    url = config.get('url', 'login')
    s = load_session()
    if not s:
        s = requests.Session()
        data = get_data()
        r = s.post(url, data=data)
        if 'Logout' not in r.content:
            raise Exception('Login failed')
        print('Log in success')
        save_session(s)
    return s

def load_session():
    filename = os.path.join(os.path.abspath(__file__ + '/../'), 'session')
    if os.path.exists(filename):
        with open(filename, 'rb') as f:
            print('Load session')
            return pickle.load(f)
    return None

def save_session(s):
    filename = os.path.join(os.path.abspath(__file__ + '/../'), 'session')
    with open(filename, 'wb') as f:
        pickle.dump(s, f)

if __name__ == '__main__':
    s = login()
    r = s.get('https://uva.onlinejudge.org')
    print(r.content)

