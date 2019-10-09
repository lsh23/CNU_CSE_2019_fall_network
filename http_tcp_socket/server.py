import socket

def open_server_socket(IP):
    s_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s_socket.bind((IP.ipaddress, IP.port))
    s_socket.listen()
    return s_socket


def accept_client(s_socket):
    print("server_open...")

def main(FLAGS):
    server_socket = open_server_socket(FLAGS)
    accept_client(server_socket)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--ipaddress', type=str,
                        default='localhost')
    parser.add_argument('-p', '--port', type=int,
                        default=1234)
    FLAGS, _ = parser.parse_known_args()
    main(FLAGS)

