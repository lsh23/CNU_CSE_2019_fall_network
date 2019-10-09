import socket

def open_server_socket(IP):
    s_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s_socket.bind((IP.ipaddress, IP.port))
    s_socket.listen()
    return s_socket


def accept_client(s_socket):
    print("server_open...")

    while True:
        conn, addr = s_socket.accept()
        print("connected by ({0}) , {1}".format(addr[0],addr[1]))
        print("connect client... ",s_socket.getsockname()[1])
        data = conn.recv(1024).decode('utf-8')
        print("accept client socket")
        print("IP:{0}, data:{1}".format(addr[0],data))
        splited_data = data.split(" ")
        method = splited_data[0]
        # request_url = splited_data[1]
        # protocol = splited_data[2].split("\r")[0]
        # print("[{0}, {1}, {2}]".format(method,request_url,protocol))
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
        conn.sendall((message+html).encode('utf-8'))
        
        print(html)
        print("Send OK")
        conn.close()

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

