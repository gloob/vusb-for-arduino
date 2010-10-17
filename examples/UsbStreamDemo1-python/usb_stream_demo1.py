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


if __name__ == "__main__":

    theDevice = ArduinoUsbDevice(idVendor=0x16c0, idProduct=0x05df)

    print "Found: 0x%04x 0x%04x %s %s" % (theDevice.idVendor, 
                                          theDevice.idProduct,
                                          theDevice.productName,
                                          theDevice.manufacturer)


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
    
                                

