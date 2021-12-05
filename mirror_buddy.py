#!/usr/bin/env python3

#imports the needed modules
import httplib2
from bs4 import BeautifulSoup, SoupStrainer
import os

#pings the mirrors
def ping_mirror(url):
    for url in mirrors:
        os.popen(url)

#pulls the list of mirrors from mirrors.opensuse.org
def mirror_list(url, http):   
    response, content = http.request(url)
    mirrors = []

    for mirror in BeautifulSoup(content, features="lxml").findAll('a', href=True):
        mirrors.append(mirror['href'])

    mirrors.remove("https://bugzilla.opensuse.org/")
    mirrors.remove("https://github.com/openSUSE/mirrorbrain")

    print(mirrors)

mirror_list('https://mirrors.opensuse.org', httplib2.Http())


