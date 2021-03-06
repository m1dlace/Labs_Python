﻿#Написать скрипт trackmix.py, который формирует обзорный трек-микс альбома
#(попурри из коротких фрагментов mp3-файлов в пользовательской директории).
#Для манипуляций со звуковыми файлами можно использовать сторонние утилиты, например, FFmpeg.
#Пример вызова и работы скрипта: trackmix --source "C:\Muz\Album" --count 5 --frame 15 -l -e --- processing file 1: 01 - Intro.mp3 --- processing file 2: 02 - Outro.mp3 --- done!

import os
import os.path
import shutil
import datetime
import argparse
from glob import glob
import sys
import subprocess
import random

parser = argparse.ArgumentParser(description='Parser for Exercise 6')
parser.add_argument('-s', '--source', type=str, default=None, required=True)
parser.add_argument('-d', '--dest', type=str, default=None)
parser.add_argument('-c', '--count', type=int, default=None)
parser.add_argument('-f', '--frame', type=int, default=10)
parser.add_argument('-l', '--log', type=bool, default=False)
parser.add_argument('-e', '--extended', type=bool, default=False)
my_parser = parser.parse_args()

def isNone(smth):
    return True if smth is None else False

path = ''
destination_name = ''
countInt = None
frameInt = None
logBool = False
extendedBool = False

def check_all_variables(src, dst, cnt, frame, logs, extended):
    global path, destination_name, countInt, frameInt, logBool, extendedBool
    if isNone(src):
        print('No path')
    else:
        if isNone(dst):
            destination_name = src + 'mix.mp3'
        else:
            destination_name = dst

        if not isNone(cnt):
            countInt = cnt
        else:
            countInt = len(os.listdir(src))
        if not isNone(frame):
            frameInt = frame
        else:
            pass
        if isNone(logs):
            pass
        else:
            logBool = True
        if isNone(extended):
            pass
        else:
            extendedBool = True

def track_mix():
    check_all_variables(my_parser.source, my_parser.dest, my_parser.count, my_parser.frame, my_parser.log,
                        my_parser.extended)
    tracklist = list(glob.glob((os.path.join(my_parser.source, '*.mp3')).replace('\\\\', '/')))
    print(tracklist)
track_mix()