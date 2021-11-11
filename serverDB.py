'''
RaspberryPi Alphabot: server

@Andrea-Tomatis
'''

import socket as sck
import threading as thr
import config
if config.DUMMY:
    from alphabot_dummy import AlphaBot
else:
    from alphabot import AlphaBot
import time
import sqlite3 
from sqlite3 import Error
import battery

lstClient = []



def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


class Client_Manager(thr.Thread):
    def __init__(self, addr, conn):
        thr.Thread.__init__(self)
        self.addr = addr
        self.conn = conn
        self.nickname = ''
        self.running = True
        self.commands = {'forward':robot.forward,
                         'backward':robot.backward,
                         'left' : robot.left,
                         'right' : robot.right,
                         'stop' : robot.stop,
                         'set_pwm_a' : robot.set_pwm_a(robot.PA),
                         'set_pwm_b' : robot.set_pwm_b(robot.PB),
                         'set_motor' : robot.set_motor}
    
    def run(self):
        while self.running:
            msg_received = self.conn.recv(config.BUF_SIZE)
            msg_received = msg_received.decode()
            if len(msg_received.split(';')) > 1:
                com, duration = msg_received.split(';')
                if com.startswith('exit') and self.running: 
                    self.running = False
                else:
                    print(f'{self.nickname}: {msg_received}')
                    
                    if com in self.commands:
                        self.commands[com]()
                        response = com
                        time.sleep(int(duration))
                        robot.stop()
                    elif com == 'man':
                        response = 'command list:\n-forward\n-backward\n-left\n-right\n-stop\n-set_motor\n-set_pwm_a\n-set_pwm_b\n-battery'
                    self.conn.sendall(response.encode())
            else:
                if msg_received == "battery":
                    self.conn.sendall(battery.check_battery().encode())
                else:
                    cur = create_connection('./movimenti.db').cursor()
                    try:
                        cur.execute(f'SELECT sequenza FROM Movimenti WHERE nome = "{msg_received}"')
                        mov = cur.fetchall()
                        mov = mov[0][0].split(';')
                        for m in mov:
                            m = m.split('_')
                            self.commands[m[0]]()
                            time.sleep(int(m[1]))
                            robot.stop()
                        self.conn.sendall(msg_received.encode())
                    except Exception as e:
                        self.conn.sendall(f'error executing {msg_received}'.encode())
                        print(e)

 

class Accettazione(thr.Thread):
    def __init__(self, s):
        thr.Thread.__init__(self)
        self.s = s
    
    def run(self):
        while True:
            conn, addr = self.s.accept()
            client = Client_Manager(addr, conn)
            nick = client.conn.recv(config.BUF_SIZE)
            client.nickname = nick.decode()
            print('new client saved: ' + nick.decode())
            conn.sendall("Client succefully connected".encode())
            lstClient.append(client)
            client.start()


def main():
    s = sck.socket(sck.AF_INET, sck.SOCK_STREAM)
    s.bind(('192.168.0.134', 5001))
    s.listen()
    
    global robot
    robot = AlphaBot()

    acc = Accettazione(s)
    acc.start()

    while True:
        for c in lstClient:
            if not c.running:
                c.conn.close()
                c.join()
                lstClient.remove(c)


if __name__ == "__main__":
    main()
