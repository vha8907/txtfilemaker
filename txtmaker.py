import random
import os
import pathlib
from string import ascii_letters, digits


alphanumeric = list(ascii_letters) + list(digits)

def file_size(filename):
    return format_bytes(os.path.getsize(filename))

def format_bytes(size):
    # 2**10 = 1024
    power = 2 ** 10
    n = 0
    power_labels = {0 : '', 1: 'kilo', 2: 'mega', 3: 'giga', 4: 'tera'}
    while size > power:
        size /= power
        n += 1
    return '{} {}{}'.format(round(size,4),power_labels[n],"bytes")

kb = 1024 ** 1
mb = 1024 ** 2  # 1 Mb of text

def makefile():
    txt = ''.join([random.choice(alphanumeric) for i in range(kb * 10)])
    with open('textfile.txt', 'w+') as f:
        f.write(txt)
    print(file_size('textfile.txt'))

makefile()