# -*- coding: utf-8 -*-
"""
Created on Wed Nov 26 13:35:15 2014

@author: user
"""

import os, sys
from enum import Enum

class MsgType (Enum):
    sent=0
    deliveryRep=1
    incoming=2
    unknown = 3

relevantPhones = ["2348144443019", "2348144443017"]
fileName = 'c:\\temp\\NLBLCommLibRunner.log'
try:
    fi = open (fileName,'r',encoding='Windows-1252',errors='replace')
except:
    print ("Could not open file: {0}".format(fileName))
    sys.exit()
ln = fi.readline()
#try:
while ln and ln != "":
    #ln = ln.replace (" ","")
    found = False
    for phStr in relevantPhones:
        if ln.find(phStr)>=0:
            found = True
            break
    #legal line - parse
    if found:
        ln = ln.replace("DEBUG - ", "").replace('[','').replace(']','')
        if ln.find ("Send TEX")>=0 or ln.find ("Send BINARY")>=0:
            mDirTp = MsgType.sent
        elif ln.find ("Delivery rep")>=0:
            mDirTp = MsgType.deliveryRep
        elif ln.find ("Incomming SMS") >= 0:
            mDirTp = MsgType.incoming 
        else:
            mDirTp = MsgType.unknown
        #if mDirTp != MsgType.unknown:
        #print ("sent: {0}, Phone: {1}".format(sentStr, phStr))
        print ("{0} : {1}".format(mDirTp, ln))
    ln = fi.readline()
#except:
 #   print ("Exception on line: {0}".format(lnidx))
fi.close();

#DEBUG - [11/4/2014 12:38:00 PM] Send TEXT SMS [OK = True, Options = 0, ID=5c5ffc11]=> 2348144443017, "Request rejected: NoSuchUnit, HPS: 0033"

