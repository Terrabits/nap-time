# Nap Time

An IoT noise machine and temperature control device in one.

## Requirements

- Raspberry pi (with 3.5 mm audio out)
- SD memory card
- Micro-usb power supply
- DS18B20 one-wire digital temperature sensor
- 4.7 KΩ or 10 KΩ resistor
- An Op-Amp / audio amplifier
- 4-8 Ohm speaker
- [Oittm WiFi Smart Plug B072F1WBS3](https://www.oittm.com/Oittm-Wifi-Smart-Light-Plug-)
- Raspbian lite

## Steps

Apply raspbian lite to SD memory card (MacOS).

```shell
diskutil list # note disk id <i>
diskutil unmountDisk /dev/disk<i>
sudo dd bs=1m if=path/to/raspbian.img of=/dev/rdisk<i> conv=sync
# image mounts to /Volumes/boot
touch /Volumes/boot/ssh
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
network={
    ssid="YOUR_NETWORK_NAME"
    psk="YOUR_PASSWORD"
    key_mgmt=WPA-PSK
}
EOF
```

Put the SD card into the Pi and power up. Wait until Pi connects to your wifi, then SSH into it and do the following:

```shell
passwd # set new password for user pi
sudo apt-get update
sudo apt-get upgrade
sudo raspi-config # change hostname
sudo echo "dtoverlay=w1-gpio" >> /boot/config.txt
sudo reboot
```

After reboot, hostname should be updated and temperature sensor should be available.

```shell
sudo modprobe w1-gpio
sudo modprobe w1-therm
ls /sys/bus/w1/devices # Should display as 28-XXXXXXXXXXXX
cd /sys/bus/w1/devices/28-XXXXXXXXXXXX
cat w1_slave
```

## References

- [Raspberry Pi DS18B20 Temperature Sensor Tutorial](http://www.circuitbasics.com/raspberry-pi-ds18b20-temperature-sensor-tutorial/)
- [TI LM386 Datasheet](http://www.ti.com/lit/ds/symlink/lm386.pdf)
- [Hacking ESP8266 smart plug – serial adaper](https://notenoughtech.com/featured/esp8266-smart-plug/)
- [Github: Terrabits/make-noise](https://github.com/Terrabits/make-noise)
