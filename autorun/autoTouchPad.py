#!/usr/bin/python3
import os
import re
import sys

arg = 'off'

msg = os.popen("xinput --list").read()
touchPadID = re.findall(r'TouchPad\s*id=(\d*)', msg)
# print("finally find the touchpad id :", touchPadID)
print('find the pad device ID ', touchPadID)

if len(sys.argv) > 1:
    arg = sys.argv[1]
    if arg == "on":
        os.popen('xinput enable {}'.format(touchPadID[0]))
        print("enable the touchpad successfully....")
        os._exit(0)
    elif arg == "off":
        os.popen("xinput disable {}".format(touchPadID[0]))
        print("disable the touchpad successfully....")
        os._exit(0)

if "Mouse" in msg :
    os.popen("xinput disable {}".format(touchPadID[0]))
    print("disable the touchpad successfully....")
else:
    os.popen('xinput enable {}'.format(touchPadID[0]))
    print("enable the touchpad successfully....")