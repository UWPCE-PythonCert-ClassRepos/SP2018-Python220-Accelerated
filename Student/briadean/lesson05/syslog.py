#!/usr/bin/env python3

import logging
import time
import threading
import socketserver

"""
Tiny Syslog Server in Python.

This is a tiny syslog server that is able to receive UDP based syslog
entries on a specified port and save them to a file.
That's it... it does nothing else...
There are a few configuration parameters.
"""

LOG_FILE = 'yourlogfile.log'
HOST = '0.0.0.0'
TCP_PORT = 1514
UDP_PORT = 514

# NO USER SERVICEABLE PARTS BELOW HERE...

listening = False

logging.basicConfig(level=logging.INFO, format='%(message)s', datefmt='', filename=LOG_FILE, filemode='a')


class SyslogUDPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        # data = bytes.decode(self.request[0].strip())
        data = self.request[0].strip()
        # socket = self.request[1]
        print( "%s : " % self.client_address[0], str(data))
        logging.info(str(data))


class SyslogTCPHandler(socketserver.BaseRequestHandler):

    End = '\n'

    def join_data(self, total_data):
        final_data = ''.join(total_data)
        for data in final_data.split(self.End):
            print( "%s : " % self.client_address[0], str(data))
            logging.info(str(data))

    def handle(self):
        total_data = []
        while listening:
            data = self.request.recv(8192).strip()
            if not data: break
            if self.End in data:
                split_index = data.rfind(self.End)
                total_data.append(data[:split_index])
                self.join_data(total_data)
                del total_data[:]
                total_data.append(data[split_index + 1:])
            else:
                total_data.append(data)
        if len(total_data) > 0:
            self.join_data(total_data)
        # logging.info(str(data))


if __name__ == "__main__":
    listening = True
    try:
        # UDP server
        udpServer = socketserver.UDPServer((HOST, UDP_PORT), SyslogUDPHandler)
        udpThread = threading.Thread(target=udpServer.serve_forever)
        udpThread.daemon = True
        udpThread.start()
        # udpServer.serve_forever(poll_interval=0.5)

        # TCP server
        tcpServer = socketserver.TCPServer((HOST, TCP_PORT), SyslogTCPHandler)
        tcpThread = threading.Thread(target=tcpServer.serve_forever)
        tcpThread.daemon = True
        tcpThread.start()

        while True:
            time.sleep(1)
        # tcpServer.serve_forever(poll_interval=0.5)
    except (IOError, SystemExit):
        raise
    except KeyboardInterrupt:
        listening = False
        udpServer.shutdown()
        udpServer.server_close()
        tcpServer.shutdown()
        tcpServer.server_close()
        print("Crtl+C Pressed. Shutting down.")
