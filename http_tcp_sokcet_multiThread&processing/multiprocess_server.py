from multiprocessing import Process
import socket
import os

def send_recv(client, address):
    msg = client.recv(1024)
    print("[client {} {}]".format(os.getpid(),msg.decode()))
    message = "HTTP/1.1 200 0K\r\n"
    html = """
        <!DOCTYPE html>
        <html>
            <head>
                <title>Page Title</title>
            </head>
         <body>

            <h1>This is a Heading</h1>
            <p>This is a paragraph.</p>
         </body>
        </html>
        """
        
    client.send((message+html).encode('utf-8'))
    client.close()


def main(FLAGS):
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversocket.bind(('', FLAGS.port))
    serversocket.listen(5)
    clients = list()

    while True:
        client, address = serversocket.accept()
        print("accept client from", address)
        proc = Process(target = send_recv, args=(client,address))
        proc.start()
        proc.join()

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('-p','--port',type=int,default=1234,help="input port number")

    FLAGS, _ = parser.parse_known_args()
    main(FLAGS)