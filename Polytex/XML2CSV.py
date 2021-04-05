import sys

fileName = r"c:\Projects\Weldobot\AROW OMRON Error Codes.csv"
try:
    fi = open(fileName, 'r', encoding='Windows-1252', errors='replace')
except:
    print("Could not open file: {0}".format(fileName))
    sys.exit()