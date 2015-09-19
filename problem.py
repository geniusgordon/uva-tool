import os
import sys
import requests
import subprocess
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

def write(pid):
    filename = 'downloads/%s.pdf' % pid
    if not os.path.exists(filename):
        download_pdf(pid)
    with open(os.devnull, 'w') as f:
        subprocess.call(['xdg-open', filename], stderr=f)
    filename = 'codes/%s.cpp' % pid
    includes = config.get('problem', 'includes').split(',')
    template = 'int main()\n{\n\treturn 0;\n}\n\n'
    if not os.path.exists('codes/'):
        os.makedirs('codes/')
    if not os.path.exists(filename):
        with open(filename, 'w') as f:
            for include in includes:
                f.write('#include <%s>\n' % include.strip())
            f.write('using namespace std;\n\n')
            f.write(template)
    os.system('vim ' + filename)
    os.system('vim input')
    ret = os.system('g++ -g ' + filename)
    if ret == 0:
        os.system('./a.out < input > output')
        os.system('cat output')

if __name__ == '__main__':
    # download_pdf(11234)
    write(123)

