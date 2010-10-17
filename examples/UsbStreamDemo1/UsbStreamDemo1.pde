#include <UsbStream.h>
void setup() {
    UsbStream.begin();
    
    UsbStream.write(0xff);
}

int pins[] = {0,0,0,0,0,0,0,0,0,0,0,0,0,0};

void loop() {
  UsbStream.refresh();
  
  if (UsbStream.available() > 0) {
    int pin = UsbStream.read();
    pins[pin] = !pins[pin];
    digitalWrite(pin, pins[pin]);
    UsbStream.write(pin);
  }
}


