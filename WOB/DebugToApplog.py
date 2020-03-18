import os

# def legalFolder (fldr):
#     #bn = os.path.basename(fldr)
#     #return bn[0]!='.'
#     res = fldr.find('.')
#     return res <0
#
# rootDir = r'c:\Projects\Weldobot\AROW'
# for dirName, subdirList, fileList in os.walk(rootDir):
#     print('Found directory: %s' % dirName)
#     subdirList = [x for x in subdirList if legalFolder(x)]
#     if legalFolder(dirName):
#         for fname in fileList:
#             print('\t%s' % fname)

def traverse (root):
    dirs = list(filter(lambda x: os.path.isdir(x), os.listdir(root)))
    files = list(filter(lambda x: os.path.isfile(x), os.listdir(root)))
    print ("{}".format(",".join(dirs)))
    print ("{}".format(",".join(files)))

traverse(r'c:\Projects\Weldobot\AROW')