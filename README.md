## pycom-micropython-us100
Driver for the US-100 sonar distance sensor, ported to run on Pycom distribution of Micropython.


### How to use:
This has been tested on a Pycom SiPy, however it should work for most Pycom Micropython based hardware. The US100 operates in either serial or 'HC-SR04' mode with trigger and echo pins.


#### Make sure the sensor is set to serial mode. To set this, bridge the two jumper pins on the back of the sensor with a jumper


### Pinout 
| Sensor | Device Only | Expansion Board |
| ---- |----- | --- |
| VCC | 3.3v | 3V3 |
| GND | GND| GND |
| TX | P4 (Tx) | G24 |
| RX | P3 (Rx)| G11 |

### Troubleshooting

If the device hangs or stops responding:
- Check the connections
- Swap the TX and RX pins (some sensors may be labelled incorrectly)
- Use the print statements in the US100.py file for debugging.  
