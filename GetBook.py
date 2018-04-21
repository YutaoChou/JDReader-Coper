# -*- coding: utf-8 -*-

import subprocess
import os
import sys
import platform
import time


Max = 2549
BookName = "Linux Server"
for i in range (0,Max):
    imageName = BookName + ('_%04d.JPEG' % i)
    print imageName
    run('adb shell screencap -p /sdcard/'+ imageName,shell=True)
    run('adb pull /sdcard/'+imageName+' .',shell=True)
    run('adb shell input swipe 1000 500 0 500 100',shell=True)
    #time.sleep(0.1)
    run('adb shell rm -rf /sdcard/'+imageName,shell=True)
