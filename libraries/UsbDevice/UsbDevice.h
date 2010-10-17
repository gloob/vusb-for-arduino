/*
 * Based on Obdev's AVRUSB code and under the same license.
 *
 * TODO: Make a proper file header. :-)
 */
#ifndef __UsbDevice_h__
#define __UsbDeviceh__

#include <avr/pgmspace.h>
#include <avr/interrupt.h>
#include <string.h>

#include "usbdrv.h"

// TODO: Work around Arduino 12 issues better.
//#include <WConstants.h>
//#undef int()

typedef uint8_t byte;

#include <util/delay.h>     /* for _delay_ms() */

class UsbGenericDevice {
 public:
  UsbGenericDevice () {
  }

  void begin() {
    // disable timer 0 overflow interrupt (used for millis)
    TIMSK0&=!(1<<TOIE0);

    cli();

    usbInit();
      
    usbDeviceDisconnect();
    uchar   i;
    i = 0;
    while(--i){             /* fake USB disconnect for > 250 ms */
        _delay_ms(1);
    }
    usbDeviceConnect();

    sei();
  }
    
  // TODO: Deprecate update
  void update() {
    refresh();
  }

  void refresh() {
    usbPoll();
  }
    
};

UsbGenericDevice UsbDevice = UsbGenericDevice();

#endif // __UsbDevice_h__
