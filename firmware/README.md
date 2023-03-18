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

# Download Arduino micropython IDE

https://labs.arduino.cc/en/labs/micropython

# Upload scripts

Make sure you do `cp config_template.py config.py`, and replace placeholders with credentials in config.py
Open folder -> select `firmware` folder in the repo, upload `boot.py`,`main.py`, `config.py`

# Run scripts

In the terminal, run `do_connect()` to initialize WIFI connection
Choose main.py in the device file explor and click `Run` in the IDE
