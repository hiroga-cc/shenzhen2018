# coding: utf-8
import re

DECORATED_ADDR = r"bitcoin:(\w+)\?.*"

def trim_addr(addr):
    m = re.match(DECORATED_ADDR, addr)
    if m == None:
        return None
    print("Trimed Address: ", m.group(1))
    return m.group(1)