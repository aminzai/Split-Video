#/bin/python
# -*- coding: UTF-8 -*-

import os
import sys
import datetime
import subprocess


#Youtube video length (Default: 15min)
yvl = 14

#==COMMAND NOTE==
#1:start time
#2:end   time
#3:input file name
#4:output file name
#5:count id
COMMAND = 'mencoder \
-ss %s:00 \
-endpos 00:%02d:00 \
-oac lavc -ovc lavc \
-of avi \
-forceidx %s \
-o %s_%02d.avi'

input_filename = sys.argv[1:]
def getVideoLength(fileName):
    """
    input: file name
    return: video length (int)
    """
    getLengthCommand = "mplayer -vo null -ao null -frames 0 -identify %s  2>/dev/null \
| grep ID_LENGTH=\
| sed 's/^ID_LENGTH=//'" % (fileName)
    #print getLengthCommand
    stdout,stdin = subprocess.Popen(args=getLengthCommand,
                              shell=True,
                              stdout=subprocess.PIPE
                             ).communicate()
    #print stdout
    return float(stdout[:-2])

def getSliceConut(fileName,videoLength):
    """
    input: file name, video slice length
    output: slice count
    """
    length = getVideoLength(fileName)
    return int(length/(videoLength*60))+1

def Runner():
    for x in input_filename:
        for i in range( getSliceConut(x,yvl)):
            cmd = COMMAND % (i*yvl,
                             yvl,
                             x,
                             ''.join(x.split('.')[:-1])
                             ,i)
            print 'Run:',cmd
            os.system(cmd)

if __name__ == '__main__':
    Runner()
