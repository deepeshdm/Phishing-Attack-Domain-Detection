from urllib.parse import urlparse
from tensorflow import keras
import re


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


# ------------------------------------------------------------------------

# This is the main function which takes a url
# and return its numerical features

def get_features(url):
    url_features = []

    # hostname length
    i = len(urlparse(url).netloc)
    url_features.append(i)

    # path length
    i = len(urlparse(url).path)
    url_features.append(i)

    i = fd_length(url)
    url_features.append(i)

    i = url.count('-')
    url_features.append(i)

    i = url.count('@')
    url_features.append(i)

    i = url.count('?')
    url_features.append(i)

    i = url.count('%')
    url_features.append(i)

    i = url.count('.')
    url_features.append(i)

    i = url.count('=')
    url_features.append(i)

    i = url.count('http')
    url_features.append(i)

    i = url.count('https')
    url_features.append(i)

    i = url.count('www')
    url_features.append(i)

    i = digit_count(url)
    url_features.append(i)

    i = letter_count(url)
    url_features.append(i)

    i = no_of_dir(url)
    url_features.append(i)

    i = having_ip_address(url)
    url_features.append(i)

    return url_features


# ------------------------------------------------------------------------

# This function takes the url and returns probability value

def get_prediction(url, model_path):
    print("Loading the model...")
    model = keras.models.load_model(model_path)

    print("Extracting features from url...")
    url_features = get_features(url)

    print("Making prediction...")
    prediction = model.predict([url_features])

    i = prediction[0][0] * 100
    i = round(i,3)
    print("There is ",i,"% chance,the url is malicious !")

    return i
