# -*- coding: utf-8 -*-

import subprocess
import os
import sys
import platform
import time


class auto_adb():    
    def run(self, raw_command):
        command = '{} {}'.format('adb', raw_command)
        process = os.popen(command)
        output = process.read()
        #print output
        return output

    def adb_path(self):
        return self.adb_path
    

adb = auto_adb()
Max = 2550
BookName = "Nginx"
for i in range (1134,Max):
    imageName = BookName + ('_%04d.JPEG' % i)
    print 'Creating' + imageName
    adb.run('shell screencap -p /sdcard/'+ imageName)
    adb.run('pull /sdcard/'+imageName+' .')
    adb.run('shell input swipe 1000 500 0 500 100')
    #time.sleep(0.1)
    adb.run('shell rm -rf /sdcard/'+imageName)
    print 'Pull' + imageName + 'Success!'
