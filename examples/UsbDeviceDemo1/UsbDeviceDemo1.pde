#include <UsbDevice.h>
#include <EEPROM.h>

byte value = 0;

void setup() {
    UsbDevice.begin();
}

void loop() {
  UsbDevice.refresh();
  
  value = EEPROM.read(0);
  
  if (value == 0) {
    digitalWrite(13, LOW);
  } else {
    digitalWrite(13, HIGH);    
  }
}


