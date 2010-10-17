/*
 * Based on Obdev's AVRUSB code and under the same license.
 *
 * TODO: Make a proper file header. :-)
 */
#ifndef __UsbStream_h__
#define __UsbStream_h__

#include <avr/pgmspace.h>
#include <avr/interrupt.h>
#include <string.h>

#include "usbdrv.h"

// TODO: Work around Arduino 12 issues better.
//#include <WConstants.h>
//#undef int()

typedef uint8_t byte;

#include <util/delay.h>     /* for _delay_ms() */

#define RING_BUFFER_SIZE 8


struct ring_buffer {
  unsigned char buffer[RING_BUFFER_SIZE];
  int head;
  int tail;
};





class UsbStreamDevice {
 private:
  ring_buffer *_rx_buffer;
  ring_buffer *_tx_buffer;

 public:
  UsbStreamDevice (ring_buffer *rx_buffer, ring_buffer *tx_buffer);

  void begin();
    
  // TODO: Deprecate update
  void update();

  void refresh();

  int available();
  int read();
  void write(byte c);
};

extern UsbStreamDevice UsbStream;

#endif // __UsbStream_h__
