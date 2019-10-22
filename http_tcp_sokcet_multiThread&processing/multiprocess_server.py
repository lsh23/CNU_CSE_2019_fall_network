from multiprocessing import Process
import socket
import os

def send_recv(client, address):



def main(FLAGS):
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversocket.bind(('', FLAGS.port))
    serversocket.listen(5)
    clients = list()

    while True:
        #send and recv


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('-p','--port',type=int,default=1234,help="input port number")

    FLAGS, _ = parser.parse_known_args()
    main(FLAGS)