import sys
sys.path.append("c:\\Users\\User\\AppData\\Local\\Programs\\Python\\Python35-32\\Lib")
import win32api as wp
import time

#http://timgolden.me.uk/pywin32-docs/contents.html

try:
    fi = open ("c:\\temp\\wpfcb.txt",'w')
except:
    print ("Could not open file")
    sys.exit()

ac = len(sys.argv)
fi.write("Total of {0} args\n".format(ac))
if ac<3:
    print ("Bad usage")
    sys.exit(0)

hwnd = int(sys.argv[1])         # handle of window you send the messsage to
msgid = int(sys.argv[2])        # message number interpreted by the WPF application
for i in range (0,100):
    w=i
    l=0
    wp.SendMessage(hwnd, msgid, w, l)
    time.sleep(0.25)
w=1
l=1
wp.SendMessage(hwnd, msgid, w, l)
fi.close()
