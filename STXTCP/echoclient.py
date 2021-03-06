import socket
import crcengine

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server
crcAlg = crcengine.new('crc16-modbus')


def calcCrc (data):
    return crcAlg(data)

def makebuff(s:str):
    bts = bytearray(s,'ascii')
    l = len(bts)
    buff = bytearray(3)
    buff[0]=255
    buff[1]=255
    buff[2]=l
    buff.extend(bts)
    crc = calcCrc(bts)
    crcb = crc.to_bytes(2, byteorder='little')
    print ("crc = {}  [{}, {}]".format(crc, crcb[0], crcb[1]))
    buff.extend(crcb)
    return buff

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    txt = "Saying hello"
    while str != "q":
        buff = makebuff (txt)
        s.sendall(buff)
        txt = input("Enter your text: ")
    s.close()


    # str = "my name is doron weiss"
    # buff = makebuff (str)
    # print (repr(buff))
    # #s.sendall(buff)
    # str = "you killed my pony"
    # buff = makebuff (str)
    # print (repr(buff))
    # #s.sendall(buff)
    # str = "prepare to die"
    # buff = makebuff (str)
    # print (repr(buff))
    # #s.sendall(buff)
    # # data = s.recv(1024)
    # # print('Received', repr(data))

