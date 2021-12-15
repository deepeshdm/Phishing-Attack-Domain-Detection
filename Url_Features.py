
# This file contains all the feature extraction functions.
# Each function extracts a particular feature from URL

import re
from urllib.parse import urlparse


# First Directory Length
def fd_length(url):
    urlpath = urlparse(url).path
    try:
        return len(urlpath.split('/')[1])
    except:
        return 0


def digit_count(url):
    digits = 0
    for i in url:
        if i.isnumeric():
            digits = digits + 1
    return digits


def letter_count(url):
    letters = 0
    for i in url:
        if i.isalpha():
            letters = letters + 1
    return letters


def no_of_dir(url):
    urldir = urlparse(url).path
    return urldir.count('/')


# Use of IP or not in domain
def having_ip_address(url):
    match = re.search(
        # IPv4 in hexadecimal
        '(([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.'
        '([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\/)|'  # IPv4
        '((0x[0-9a-fA-F]{1,2})\\.(0x[0-9a-fA-F]{1,2})\\.(0x[0-9a-fA-F]{1,2})\\.(0x[0-9a-fA-F]{1,2})\\/)'
        '(?:[a-fA-F0-9]{1,4}:){7}[a-fA-F0-9]{1,4}', url)  # Ipv6
    if match:
        # print match.group()
        return -1
    else:
        # print 'No matching pattern found'
        return 1



def hostname_length(url):
    return len(urlparse(url).netloc)

def url_length(url):
    return len(urlparse(url).path)


# Gets all count features
def get_counts(url):

    count_features = []

    i = url.count('-')
    count_features.append(i)

    i = url.count('@')
    count_features.append(i)

    i = url.count('?')
    count_features.append(i)

    i = url.count('%')
    count_features.append(i)

    i = url.count('.')
    count_features.append(i)

    i = url.count('=')
    count_features.append(i)

    i = url.count('http')
    count_features.append(i)

    i = url.count('https')
    count_features.append(i)

    i = url.count('www')
    count_features.append(i)

    return count_features


