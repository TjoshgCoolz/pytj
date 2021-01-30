import requests

def download(link, filename):
    r = requests.get(link, allow_redirects=True)
    open(filename, 'wb').write(r.content)
