'''
RaspberryPi Alphabot: client

@Andrea-Tomatis
@Nicolo-Cora
'''

import socket as sck
import threading as thr
import time


# server address and port
SERVER = ('192.168.0.134', 5001)



# prints the messages sent by the server
def receive_message(s):
    data, addr = s.recvfrom(SERVER[1])
    msg_received = data.decode()
    print(f"{msg_received}")



# returns the command typed in by the user
def type_command():
    # type of the command
    com = input('insert a command: ')
    # duration of the command
    duration = int(input('insert the duration: '))
    
    # if the duration is equal to or less than 0 the command is sent without duration.
    # The server knows he has to run a DB sequence.
    if duration > 0:
        body = com + ";" + str(duration)
    else:
        body = com
    
    return body.encode()
    
    
    
def main():
    
    # create a socket and enstablish a connection with the server
    s = sck.socket(sck.AF_INET, sck.SOCK_STREAM)
    s.connect(SERVER)
    
    # ask the user his nickname and send it to the server
    s.sendall(input('tell me your nickname: ').encode())
    data, addr = s.recvfrom(SERVER[1])
   
    # wait for the server response
    msg_received = data.decode()
    print(f"{msg_received}")
    
    
    # this infinite loop is executed until the user types the string "exit"
    while True:
        
        # send an order to the server
        msg = type_command()
        s.sendall(msg)

        if msg.startswith('exit'):
            s.close()
            print('Thread killed succesfully')
            exit()
        
        receive_message(s)

   
if __name__ == '__main__':
    main()
