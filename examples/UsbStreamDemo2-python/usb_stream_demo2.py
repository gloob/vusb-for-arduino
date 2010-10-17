#/usr/bin/python

#
# Written for PyUSB 1.0 (w/libusb 1.0.3)
#
# Includes functionality to retrieve string descriptors
#
# Author: follower@rancidbacon.com
#
# Version: 20091021
#

#
# Assumes 'UsbStreamDemo1.pde' is loaded on Arduino and 
# LEDs are present on pins 11, 12 and 13.
#

import usb # 1.0 not 0.4

import sys
sys.path.append("..")

from arduino.usbdevice import ArduinoUsbDevice


def decrypty_(byte1, byte2):
    """
    """
    theDevice.write(byte1)
    theDevice.write(byte2)
    return chr(theDevice.read())


if __name__ == "__main__":

    if len(sys.argv) > 1:
        source = sys.argv[1]
    else:
        source = "13e971c3bd7ef968ac92174cbd63ca1ddb849f1e3161beb0a926b8e4af1c1338cecb02f34622a89e137c468f9e7060c33402ac3f8e044216bd96aca4062702f89cc7216ccfc9afb6"


    theDevice = ArduinoUsbDevice(idVendor=0x16c0, idProduct=0x05df)

    print "Found: 0x%04x 0x%04x %s %s" % (theDevice.idVendor, 
                                          theDevice.idProduct,
                                          theDevice.productName,
                                          theDevice.manufacturer)

    bytes = [int(i + j, 16) for i,j in zip(source[::2], source[1::2])]
    un = "".join([decrypty_(byte1, byte2)
                  for byte1, byte2 in zip(bytes[::2], bytes[1::2])])
    
    print eval(un)

    raise SystemExit


    try:
        print "Read: 0x%02x" % theDevice.read()
    except:
        # TODO: Check for exception properly
        print "No data read."


    import sys
    import time
    import random

    if sys.argv[1:]:
        sequence = sys.argv[1:]
    else:
        sequence = [11,12,13]* 20
        random.shuffle(sequence)

    print "Look over there, flashing lights!"
        
    for pin in sequence:
        pin = int(pin)

        theDevice.write(pin)

        if pin != theDevice.read():
            print "Pin response didn't match."

        time.sleep(0.2)

    print
    
                                

