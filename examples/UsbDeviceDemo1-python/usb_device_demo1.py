#/usr/bin/python

#
# Written for PyUSB 1.0 (w/libusb 1.0.3)
#
# Includes functionality to retrieve string descriptors
#
# Author: follower@rancidbacon.com
#
# Version: 20091020
#

import usb # 1.0 not 0.4


def getStringDescriptor(device, index):
    """
    """
    response = device.ctrl_transfer(usb.util.ENDPOINT_IN,
                                    usb.legacy.REQ_GET_DESCRIPTOR,
                                    (usb.util.DESC_TYPE_STRING << 8) | index,
                                    0, # language id
                                    255) # length

    # TODO: Refer to 'libusb_get_string_descriptor_ascii' for error handling
    
    return response[2:].tostring().decode('utf-16')



if __name__ == "__main__":

    device = usb.core.find(idVendor=0x16c0, idProduct=0x05df)

    if not device:
        raise Exception("Device not found")

    print "0x%04x 0x%04x %s %s" % (device.idVendor, device.idProduct,
                             getStringDescriptor(device, device.iProduct),
                             getStringDescriptor(device, device.iManufacturer))

    # TODO: Tidy this all up:
    
    request_type = usb.util.build_request_type(usb.util.CTRL_IN,
                                               usb.util.CTRL_TYPE_CLASS,
                                               usb.util.CTRL_RECIPIENT_DEVICE)

    USBRQ_HID_GET_REPORT = 0x01
    USBRQ_HID_SET_REPORT = 0x09
    USB_HID_REPORT_TYPE_FEATURE = 0x03

    response = device.ctrl_transfer(request_type,
                                    USBRQ_HID_GET_REPORT,
                                    (USB_HID_REPORT_TYPE_FEATURE << 8) | 0,
                                    0, # ignored
                                    128) # length

    for byte in response:
        print "0x%02x" % byte,
    
    print

    response[0] = not response [0]

    print 

    request_type = usb.util.build_request_type(usb.util.CTRL_OUT,
                                               usb.util.CTRL_TYPE_CLASS,
                                               usb.util.CTRL_RECIPIENT_DEVICE)

    bytes_sent = device.ctrl_transfer(request_type,
                                      USBRQ_HID_SET_REPORT,
                                      (USB_HID_REPORT_TYPE_FEATURE << 8) | 0,
                                      0, # ignored (report id?)
                                      response)

    print
    
                                

