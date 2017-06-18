#!/bin/bash
touch /home/chip/GarageDoor/0.x
if [ -e /home/chip/GarageDoor/log.out ]
then
    touch /home/chip/GarageDoor/1.x
    rm -f /home/chip/GarageDoor/GDLastLog.out
    cp /home/chip/GarageDoor/log.out /home/chip/GarageDoor/GDLastLog.out
else
    touch /home/chip/GarageDoor/2.x
fi

sudo python /home/chip/GarageDoor/main.py &>/home/chip/GarageDoor/log.out
