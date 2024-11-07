import time as t
from time import time

def cur_timestamp_ms():
    return int((time() * 1000))

def cur_timestamp_seconds():
    return int(time())

def get_unix_in_seconds():
    return int(t.time())
