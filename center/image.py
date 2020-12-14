import urllib.request
import string
import random
import os


def save_imager(url):
    avatar = urllib.request.urlopen(url)
    filename_charset = string.ascii_letters + string.digits
    filename_length = 10
    file_save_dir = 'media/'
    filename = ''.join(random.choice(filename_charset)
                       for s in range(filename_length))
    urllib.request.urlretrieve(url, os.path.join(file_save_dir, filename + '.png'))


def test():
    print("fasdfa")
    url = "https://platform-lookaside.fbsbx.com/platform/profilepic/?asid=1166678433784980&height=50&width=50&ext=1609645755&hash=AeT1Kj4cQDAs74uYJjA"
    a = save_imager(url)
    return a