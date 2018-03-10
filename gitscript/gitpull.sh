#!/bin/bash
cd /home/ec2-user/PhoneFlash
git pull
echo Pull finished
./build.sh
