import sys
import win32api as wp

#http://timgolden.me.uk/pywin32-docs/contents.html

if len(sys.argv<3):
    print ("Bad usage")
    sys.exit(0)

hwnd = int(sys.argv[1])
msgid = int(sys.argv[2])
for i in range (0,5):
    w=i*20
    l=0
    wp.SendMessage(hwnd, msgid, w, l)
w=1
l=1
wp.SendMessage(hwnd, msgid, w, l)
