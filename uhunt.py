import json
import requests
from config import config

def uname2uid(username):
    url = config.get('uhunt', 'uid') % username
    r = requests.get(url)
    return r.content

def ac_count(username):
    uid = uname2uid(username)
    url = config.get('uhunt', 'user') % uid
    r = requests.get(url)
    result = json.loads(r.content)
    return len(set([x[1] for x in result['subs'] if x[2] == 90]))

if __name__ == '__main__':
    print ac_count('geniusgordon')

