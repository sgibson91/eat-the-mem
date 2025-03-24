"""
https://stackoverflow.com/questions/6317818/eat-memory-using-python/43129808#43129808
"""

import os
import psutil
from datetime import datetime as dt

PROCESS = psutil.Process(os.getpid())
MEGA = 10 ** 6
MEGA_STR = " " * MEGA


def pmem():
    try:
        tot, avail, percent, used, free, active, inactive, buffers = psutil.virtual_memory()
    except ValueError:
        tot, avail, percent, used, free, active, inactive, buffers, cached, shared, slab = psutil.virtual_memory()
    
    tot, avail, used, free = tot / MEGA, avail / MEGA, used / MEGA, free / MEGA
    proc = PROCESS.memory_info()[1] / MEGA
    
    print(f"{dt.now().strftime('%Y-%m-%d %H:%M:%S')}: process = {proc}, total = {tot}, avail = {avail}, used = {used}, free = {free}, percent = {percent}")


def alloc_max_array():
    i = 0
    ar = []
    while True:
        print(f"{dt.now().strftime('%Y-%m-%d %H:%M:%S')}: iteration = {i}")
        try:
            ar.append(MEGA_STR + str(i))
        except MemoryError:
            break
        i += 1
    
    max_i = i - 1
    print(f"{dt.now().strftime('%Y-%m-%d %H:%M:%S')}: maximum array allocation: {max_i}")
    pmem()


def alloc_max_str():
    i = 0
    while True:
        print(f"{dt.now().strftime('%Y-%m-%d %H:%M:%S')}: iteration = {i}")
        try:
            a = " " * (i * 10 * MEGA)
            del a
        except MemoryError:
            break
        i += 1
    
    max_i = i - 1
    _ = " " * (max_i * 10 * MEGA)
    print(f"{dt.now().strftime('%Y-%m-%d %H:%M:%S')}: maximum string allocation: {max_i}")
    pmem()


if __name__ == "__main__":
    print(f"Program start time: {dt.now().strftime('%Y-%m-%d %H:%M:%S')}")
    pmem()
    alloc_max_str()
    alloc_max_array()
    print(f"Program end time: {dt.now().strftime('%Y-%m-%d %H:%M:%S')}")
