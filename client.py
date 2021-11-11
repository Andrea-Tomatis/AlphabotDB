'''
RaspberryPi Alphabot: client

@Andrea-Tomatis
'''

import socket as sck
import threading as thr
import time

SERVER = ('192.168.0.134', 5001)
'''
class Connection(thr.Thread):
    def __init__(self, port, s):
        thr.Thread.__init__(self)
        self.port = port
        self.s = s
        self.running = True
    def run(self):
        while self.running:
'''         


def main():
    s = sck.socket(sck.AF_INET, sck.SOCK_STREAM)
    s.connect(SERVER)

    s.sendall(input('tell me your nickname: ').encode())
    data, addr = s.recvfrom(SERVER[1])
    msg_received = data.decode()
    print(f"{msg_received}")
    
    while True:
        time.sleep(0.2)
        
        com = input('insert a command: ')
        duration = int(input('insert the duration: '))
        if duration > 0:
            body = com + ";" + str(duration)
        else:
            body = com
        msg = body.encode()
            
        s.sendall(msg)

        if body.startswith('exit'):
            conn.running = False
            s.close()
            conn.join()
            print('Thread killed succesfully')
            exit()
        
        data, addr = s.recvfrom(SERVER[1])
        msg_received = data.decode()
        print(f"{msg_received}")
    

if __name__ == '__main__':
    main()
