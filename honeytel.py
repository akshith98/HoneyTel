#import socket
import sys
import threading
import socketserver

import string
import random
import logging
import datetime
from logging import handlers
from configobj import ConfigObj
from socket import *
#from socket import AF_INET, SOCK_STREAM
from _thread import *


LOG_FILE = "/opt/honeytel/tel.log"


''' 
Open UDP Trigger Ports on the host.

'''

class ThreadedUDPRequestHandler(socketserver.BaseRequestHandler):
 
    def handle(self):
        pass
 
class ThreadedUDPServer(socketserver.ThreadingMixIn, socketserver.UDPServer):
    pass

def udplistener(PORTS):
    for PORT in UDPPORTS:
 
        server = ThreadedUDPServer((HOST, PORT), ThreadedUDPRequestHandler)
        #ip, port = server.server_address
        servers.append(server)
        # Start a thread with the server -- that thread will then start one
        # more thread for each request
        server_thread = threading.Thread(target=server.serve_forever)
        # Exit the server thread when the main thread terminates
        server_thread.daemon = True
        server_thread.start()
        server_threads.append(server_thread)
 
        #print("Server loop running in:", server_thread.name)
        print(" [*] UDP serving at Port:", PORT)


''' 
Open TCP Trigger Ports on the host.

'''
 
class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):
 
    def handle(self):
        pass
 
class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

def tcplistener(PORTS):
    for PORT in TCPPORTS:
 
        server = ThreadedTCPServer((HOST, PORT), ThreadedTCPRequestHandler)
        #ip, port = server.server_address
        servers.append(server)
        # Start a thread with the server -- that thread will then start one
        # more thread for each request
        server_thread = threading.Thread(target=server.serve_forever)
        # Exit the server thread when the main thread terminates
        server_thread.daemon = True
        server_thread.start()
        server_threads.append(server_thread)
 
        #print("Server loop running in:", server_thread.name)
        print(" [*] TCP serving at Port:", PORT)
        

'''
    Logger Implemation for Telnet Honeypot
    
'''

class LogOperation(object):
    """
    Logger Class
    """
    __LOGGER = None

    def __init__(self):
        """
        :param log_file: Log File defination

        """
        global LOG_FILE
        self.__LOGGER = logging.getLogger(__name__)
        self.__LOGGER.setLevel(logging.INFO)
        HANDLER = logging.handlers.RotatingFileHandler(
            LOG_FILE, maxBytes=20 * 1024 * 1024, backupCount=5)
        HANDLER.setLevel(logging.INFO)
        FORMATTER = logging.Formatter(
            '%(asctime)s.%(msecs)03d [%(process)s] %(levelname)s: - '
            '%(message)s', "%d/%m/%Y %H:%M:%S")
        HANDLER.setFormatter(FORMATTER)
        if self.__LOGGER.hasHandlers():
            self.__LOGGER.handlers.clear()
        self.__LOGGER.addHandler(HANDLER)


    def log_error(self, message):
        """
        Error logger
        :param message: Error log message

        """
        self.__LOGGER.error("Error : " + str(message))

    def log_info(self, message):
        """
        Normal logger
        :param message: Log message
        """
        self.__LOGGER.info(message)


'''
Telnet HoneyPot with minimal fuctionality.

'''

class TelnetServer:

    def __init__(self):
        global host, port, log_th, conf_th, MENU_MESSAGE
        self.host = host
        self.port = port
        self.log_th = log_th
        self.telnet_message_path = 'Telnet'

    def recv_message(self, conn):
        bytes_received = conn.recv(4096)
        ex = bytes_received.decode('ISO-8859-1')
        return ex.encode('ascii', 'ignore').decode()

    def send_message(self, conn, message, dis_newline):
        if dis_newline:
            message = message + "\n"
        conn.send(bytes(message.encode()))

    def login_interface(self, conn, id, client_ip, client_port):

        message = "Username: "
        self.send_message(conn=conn, message=message, dis_newline=False)
        username = self.recv_message(conn)
        commands = "Client {}, username '{}' entered".format(client_ip, username)
        self.log_th.log_info('{} - {}:{} client username entered : {} '.format(
            id, client_ip, client_port, username))

        message = "Password: "
        self.send_message(conn=conn, message=message, dis_newline=False)
        password = self.recv_message(conn)
        commands = "Client {}, password '{}' entered".format(client_ip, password)
        self.log_th.log_info('{} - {}:{} client password entered : {} '.format(
            id, client_ip, client_port, password))
            
        message = "OK"
        self.send_message(conn=conn, message=message, dis_newline=True)

    

    def telnet_thread(self, conn, addr):
        client_ip = addr[0]
        client_port = str(addr[1])
        self.log_th.log_info('{}:{} connected to proxy socket'.format(client_ip, client_port))  

        self.login_interface(conn=conn, id=id, client_ip=client_ip, client_port=client_port)

        empty_try = 0
        while True:
            msg = self.telnet_message_path + '>'
            self.send_message(conn=conn, message=msg, dis_newline=False)

            command = self.recv_message(conn)
            if command == "":
                if empty_try > 5:
                    break
                else:
                    empty_try += 1
            self.log_th.log_info('{} - {}:{} client command entered : {} '.format(
                id, client_ip, client_port, command))
            command = command.strip()
            if command == "logout":
                break
            else:
                self.send_message(conn=conn, message="ERROR : Unrecognized command", dis_newline=True)

        self.log_th.log_info('{}:{} disconnected'.format(client_ip, client_port))
        conn.shutdown(SHUT_RD)
        conn.close()
        


def start_telnet():
    #s = socket(AF_INET, SOCK_STREAM)
    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        #s = socket.socket(AF_INET,SOCK_STREAM)
        s.bind(('0.0.0.0', 23))
        s.listen()
        #conn,addr = s.accept()
        log_th.log_info('{}:{} socket started..'.format('0.0.0.0', str(23)))
        #while True:
        #    data=conn.recv(1024)
        #    if data == b'\r\n':
        #        s.close()
        #        s.exit()
        print(" [*] TCP serving at Port: 23")
    except socket.error as message:
        if s:
            s.shutdown(socket.SHUT_RD)
            s.close()
            log_th.log_error("Could not open socket:", message)
        sys.exit(1)
    while 1:
        conn, client_addr = s.accept()
        print("\n")
        print('honeypot has been visited by ' + client_addr[0])
        start_new_thread(TelnetServer().telnet_thread, (conn, client_addr))

def server_init(log_set):
    global log_th, host, port
    log_th = log_set
    host = '0.0.0.0'
    port = 23

log_ops = LogOperation()
server_init(log_set=log_ops)

def banner():
    print("\n")
    print("\n  ------------------------------------------------------------------------------------------------------------------")
    print("\n |              HonyTel is a honeypot and monitering tool. HonyTel opens ""trigger"" ports on the host                  |")
    print("\n |              that an attacker would connect to. HonyTel for now only has a telnet honeypot. This                 |")
    print("\n |              honeypot can log attacker commands and moniter potential port scans.                                |")
    print("\n  -------------------------------------------------------------------------------------------------------------------")
    print("\n")
 
if __name__ == "__main__":
    HOST = ""
 
    servers = []
 
    server_threads = []

    TCPPORTS = [22,1433,8080,21,5060,5061,5900,25,110,1723,1337,10000,5800,44443,16993]

    UDPPORTS = [123,5060,5061,3478]

    banner()

    udplistener(UDPPORTS)
    print("\n")
    tcplistener(TCPPORTS)
   
    start_telnet()



 
while True:
    try:
        pass
    except KeyboardInterrupt:
        print("\nKilling all servers...")
        for server in servers:
            server.shutdown()
        sys.exit(0)