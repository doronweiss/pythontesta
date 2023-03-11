import sys
import pathlib as pl

data="""
i586-pc-msdosdjgpp-gcc-5.4.0.exe
i586-pc-msdosdjgpp-gcc-ar.exe
i586-pc-msdosdjgpp-gcc-nm.exe
i586-pc-msdosdjgpp-gcc-ranlib.exe
i586-pc-msdosdjgpp-gcc.exe
i686-w64-mingw32-gcc-11.exe
i686-w64-mingw32-gcc-ar.exe
i686-w64-mingw32-gcc-nm.exe
i686-w64-mingw32-gcc-ranlib.exe
i686-w64-mingw32-gcc.exe
x86_64-pc-cygwin-gcc-11.exe
x86_64-pc-cygwin-gcc-ar.exe
x86_64-pc-cygwin-gcc-nm.exe
x86_64-pc-cygwin-gcc-ranlib.exe
x86_64-pc-cygwin-gcc.exe
x86_64-w64-mingw32-gcc-11.exe
x86_64-w64-mingw32-gcc-ar.exe
x86_64-w64-mingw32-gcc-nm.exe
x86_64-w64-mingw32-gcc-ranlib.exe
x86_64-w64-mingw32-gcc.exe
"""

lines = [ln for ln in data.split('\n') if len(ln)>0]
for token in lines:
    if len(token) == 0:
        continue
    exefl = pl.Path(token).with_suffix('')
    print ("# ******** {0} ********".format(exefl))
    print ("$ {0} -c -o uploadconnector.o uploadconnector.cpp".format(exefl))
    print ("{0} -o uploadconnector.dll -s -shared uploadconnector.o libUploadHelper.a".format(exefl))
