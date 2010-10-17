#!/usr/bin/python

import sys
import random

def encrypty_(byte):
    """
    """
    hn = byte & 0xf0
    ln = byte & 0x0f

    hr = random.randint(0,15)
    lr = random.randint(0,15)

    high = (hn ^ (hr << 4)) | hr
    low = (ln ^ lr) | (lr << 4)

    return (high, low)


def decrypty_(bytes):
    """
    """
    high = bytes[0]
    low = bytes[1]

    hr = high &0x0f
    hen = high &0xf0
    hn = hen ^ (hr << 4)

    lr = (low & 0xf0) >> 4
    len_ = low & 0x0f
    ln = len_ ^ lr

    byte = hn | ln

    return byte



if __name__ == "__main__":

    if len(sys.argv) > 1:
        plain = sys.argv[1]
    else:
        plain = "'oinkhello'[4:]+', '+'worldgone'[:5]"

    result = []

    for char in plain:
        result.extend(encrypty_(ord(char)))

    e = "".join(["%02x" %i for i in result])

    print e


    bytes = [int(i + j, 16) for i,j in zip(e[::2], e[1::2])]
    un = "".join([chr(decrypty_((byte1, byte2))) 
                  for byte1, byte2 in zip(bytes[::2], bytes[1::2])])

    if eval(un) != eval(plain):
        print "Something didn't work."

    
    
