#!/usr/bin/env python3

import httplib2
from bs4 import BeautifulSoup, SoupStrainer
import os

def ping_mirror(url):
    for url in mirrors:
        os.popen(url)

url='https://mirrors.opensuse.org'
http = httplib2.Http()
    
response, content = http.request(url)

mirrors = []

for mirror in BeautifulSoup(content, features="lxml").findAll('a', href=True):
    mirrors.append(mirror['href'])

mirrors.remove("https://bugzilla.opensuse.org/")
mirrors.remove("https://github.com/openSUSE/mirrorbrain")

print(mirrors)


