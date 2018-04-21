# -*- coding: utf-8 -*-

import subprocess
import os
import sys
import platform
import time


Max = 2549
BookName = "Linux Server"
for i in range (0,Max):
    imageName = BookName + ('_%04d.JPG' % i)
    print imageName
    os.system('adb shell screencap -p /sdcard/'+ imageName)
    os.system('adb pull /sdcard/'+imageName+' .')
    os.system('adb shell input swipe 1000 500 0 500 100')
    #time.sleep(0.1)
    adb.run('adb shell rm -rf /sdcard/'+imageName)
