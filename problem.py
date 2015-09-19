import os
import sys
import requests
from config import config

def cli_progress(filename, progress, bar_length=20):
    percent = progress / 100.0
    if percent > 1.0:
        percent = 1.0
    hashes = '#' * int(round(percent * bar_length))
    spaces = ' ' * (bar_length - len(hashes))
    sys.stdout.write('\r%s: [%s] %s%%' % (filename, hashes+spaces, round(percent*100)))
    sys.stdout.flush()

def download_pdf(pid):
    pid = str(pid)
    filename = pid+'.pdf'
    url = config.get('url', 'pdf') % (pid[:-2], filename)
    cli_progress(filename, 0.0)
    r = requests.get(url, stream=True)
    if r.status_code == 404:
        print ''
        raise Exception('problem pdf not found')
    size = float(r.headers['content-length'])
    cnt = 1
    path = 'downloads/'
    if not os.path.exists(path):
        os.makedirs(path)
    with open(path+filename, 'w') as f:
        for chunk in r.iter_content(chunk_size=1024):
            f.write(chunk)
            cli_progress(filename, cnt*1024.0/size*100)
            cnt += 1
    print ''

if __name__ == '__main__':
    download_pdf(11234)

