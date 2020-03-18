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

def legalFolder (root, fldr):
    if fldr[0]=='.':
        return False
    fn = os.path.join(root, fldr)
    res = os.path.isdir(fn)
    return res

def legalFile (root, file, ext):
    fn, fx = os.path.splitext(file)
    if fx!=ext:
        return False
    fn = os.path.join(root, file)
    res = os.path.isfile(fn)
    return res

def traverse (root):
    dirs = [x for x in os.listdir(root) if legalFolder(root, x)]
    files = [x for x in os.listdir(root) if legalFile(root, x, ".cs")]
    if len(dirs)>0:
        print ("{}\n".format(", ".join(dirs)))
    if len(files)>0:
        print ("{}\n".format(", ".join(files)))
    for dir in dirs:
        traverse (os.path.join(root, dir))

traverse(r'c:\Projects\Weldobot\AROW')