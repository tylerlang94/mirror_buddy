#!/usr/bin/env python3
# https://mirrors.opensuse.org      |     httplib2.Http()


#imports the needed modules
import httplib2
from bs4 import BeautifulSoup, SoupStrainer
import os

#pings the mirrors
def ping_mirror(hostname):
    response = os.system('ping -c 1 ' + hostname)

#pulls the list of mirrors from mirrors.opensuse.org
def mirror_list(url, http):   
    response, content = http.request(url)
    mirrors = []

    for mirror in BeautifulSoup(content, features="lxml").findAll('a', href=True):
        mirrors.append(mirror['href'])

    mirrors.remove("https://bugzilla.opensuse.org/")
    mirrors.remove("https://github.com/openSUSE/mirrorbrain")

    return mirrors

mirrors = mirror_list('https://mirrors.opensuse.org', httplib2.Http())

for mirror in mirrors: 
    ping_mirror(mirror)
    if mirror == 0:
        print(hostname)
    else:
        continue