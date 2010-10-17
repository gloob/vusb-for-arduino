#include <UsbStream.h>
void setup() {
    UsbStream.begin();
}

byte bytes[2];
int offset = 0;

byte decrypt_(byte *bytes) {
    byte high = bytes[0];
    byte low = bytes[1];

    byte hr = high &0x0f;
    byte hen = high &0xf0;
    byte hn = hen ^ (hr << 4);

    byte lr = (low & 0xf0) >> 4;
    byte len_ = low & 0x0f;
    byte ln = len_ ^ lr;

    byte result = hn | ln;

    return result;
}

void loop() {
  UsbStream.refresh();
  
  if (UsbStream.available() > 0) {
    bytes[offset] = UsbStream.read();
    if (offset == 1) {
          UsbStream.write(decrypt_(bytes));
          offset = 0;
    } else {
       offset++;
    }    
  }
}


