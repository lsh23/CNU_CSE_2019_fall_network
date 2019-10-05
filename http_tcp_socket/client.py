import socket
FLAGS = None
class ClientSocket():

    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def socket_send_recv(self,FLAGS):
        self.socket.connect((FLAGS.url, FLAGS.port))
        request = "GET / HTTP/1.1\r\nHost:%s\r\n\r\n" % "localhost"
        self.socket.send(request.encode())
        data = self.socket.recv(4096)
        print(data.decode())

    def main(self,FLAGS):
        self.socket_send_recv(FLAGS)


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()

    parser.add_argument('-i', '--ip', type=str,
                        default='localhost')
    parser.add_argument('-p', '--port', type=int,
                        default=1234)
    parser.add_argument('-u', '--url', type=str,
                        default='localhost')
    FLAGS, _ = parser.parse_known_args()

    client_socket = ClientSocket()
    client_socket.main(FLAGS)
