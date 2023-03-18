# Make sure python is installed

# Check if driver is working and device is connected

Run after USB is connected
On macOS: `ls -l /dev/tty.usb*`
On Linux: `ls -l /dev/ttyUSB0`

# Install esptool

`pip install --upgrade esptool`

# Erase flash (Do this if it's first time flashing the firmware or if you want to do a clean flash)

`esptool.py --chip esp32 -p /dev/ttyUSB0 erase_flash`

# Flash Firmware

Download lastest firmware here:`https://micropython.org/download/esp32/`
esp32-20220618-v1.19.1 is recommended

`esptool.py --chip esp32 -p /dev/ttyUSB0 write_flash -z 0x1000 esp32-20220618-v1.19.1.bin`

# Install PyMakr extensions of VS Code

VS Marketplace Link: https://marketplace.visualstudio.com/items?itemName=pycom.Pymakr

# Upload scripts

Go to pymakr extensions and connect device
Make sure you do `cp config_template.py config.py`, and replace placeholders with credentials in config.py
Right click `main.py`,`boot.py` and `config.py`, select pymakr -> upload to device

# Run scripts

Right click the device and select hard reset. The scripts will be running.:w
