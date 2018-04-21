# -*- coding: utf-8 -*-

import subprocess
import os
import sys
import platform
import time


class auto_adb():
    def __init__(self):
        try:
            adb_path = 'adb'
            subprocess.Popen([adb_path], stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)
            self.adb_path = adb_path
        except OSError:
            if platform.system() == 'Windows':
                adb_path = os.path.join('Tools', "adb", 'adb.exe')
                try:
                    subprocess.Popen(
                        [adb_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    self.adb_path = adb_path
                except OSError:
                    pass
            else:
                try:
                    subprocess.Popen(
                        [adb_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                except OSError:
                    pass
            print('未配置环境变量')
            exit(1)
            
    def run(self, raw_command):
        command = '{} {}'.format(self.adb_path, raw_command)
        process = os.popen(command)
        output = process.read()
        print output
        if output:
            return output
        print('未配置环境变量')
        exit(1)

    def adb_path(self):
        return self.adb_path
    

adb = auto_adb()
Max = 350
BookName = "Nginx"
for i in range (0,Max):
    imageName = BookName + ('_%04d.JPEG' % i)
    print imageName
    adb.run('shell screencap -p /sdcard/'+ imageName)
    adb.run('pull /sdcard/'+imageName+' .')
    adb.run('shell input swipe 1000 500 0 500 100')
    #time.sleep(0.1)
    adb.run('shell rm -rf /sdcard/'+imageName)
