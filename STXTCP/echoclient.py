import socket
import crcengine

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server
crcAlg = crcengine.new('crc16-modbus')


def calcCrc (data):
    return crcAlg(data)

def makebuff(s:str)->bytes:
    buff = [b'\xFF', b'\xFF']
    bts = bytearray(s,'ascii')
    l = len(bts)
    szb = l.to_bytes(4, byteorder='little')[0]
    bts.append(szb)
    buff.extend(bts)
    crc = calcCrc(bts[3:])
    crcb = crc.to_bytes(2, byteorder='little')
    buff.extend(crcb)
    return buff

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    str = "Hello, World"
    buff = makebuff (str)
    #print (repr(buff))
    s.sendall(buff)
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

