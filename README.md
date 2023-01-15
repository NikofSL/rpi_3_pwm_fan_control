# Raspberry pi PWM fan control

# Prerequisites
1. Raspberry PI 3 with instaled Raspbian or other Linux distribution
2. Fan with two wire
3. 1x Transistor - 2N2222
4. 1x Resistor - 1K ohm
5. Jumper cables

# Installation

```shell
sudo apt update
sudo apt upgrade -y
sudo apt install -y python3-pip
sudo python3 -m pip install --upgrade pip
sudo pip3 install RPi.GPIO
```
