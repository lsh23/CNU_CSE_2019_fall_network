import socket
from phue import Bridge



def load_index_html():
    with open('index.html','r', encoding='utf-8') as f:
        index_html = f.read()
        return index_html
def open_server_socket(IP):
    s_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s_socket.bind((IP.ipaddress, IP.port))
    s_socket.listen()
    return s_socket


def accept_client(s_socket,lights):
    print("server_open...")

    while True:
        conn, addr = s_socket.accept()
        print("connected by ({0}) , {1}".format(addr[0],addr[1]))
        print("connect client... ",s_socket.getsockname()[1])
        data = conn.recv(1024).decode('utf-8')
        # print("accept client socket")
        # print("IP:{0}, data:{1}".format(addr[0],data))


        method = data.split("\r\n")[0].split(' ')[0]
        print(data.split("\r\n"))
        # print(method)
        if method == "GET":
            message = "HTTP/1.1 200 0K\r\n\n"
            html = load_index_html()
            conn.sendall((message+html).encode('utf-8'))
            print("Send OK")
            conn.close()
        if method == "POST":
            post_message = data.split("\r\n")[-1]
            post_params = post_message.split("&")
            power_on = post_params[0].split("=")[1]
            brightness = post_params[1].split("=")[1]
            x = post_params[2].split("=")[1]
            y = post_params[3].split("=")[1]
            hue_num = post_params[4].split("=")[0].split("_")[1]
            message = "HTTP/1.1 200 0K\r\n\n"
            html = load_index_html()
            conn.sendall((message+html).encode('utf-8'))
            print(power_on,brightness,x,y,hue_num)
            controll_hue(hue_num,power_on,brightness,x,y,lights)
        # method = splited_data[0]
        # request_url = splited_data[1]
        # protocol = splited_data[2].split("\r")[0]
        # print("[{0}, {1}, {2}]".format(method,request_url,protocol))
        # print(html)
    # print(1)

def controll_hue(hun_num,power_on,brightness,x,y,lights):
    power_control(hun_num,power_on,lights)
    brightness_control(hun_num,brightness,lights)
    color_control(hun_num,x,y,lights)

def power_control(hub_num,power,lights):
    try:
        if power == "on":
            lights[int(hub_num)-1].on = True
        else:
            lights[int(hub_num)-1].on = False
    except Exception as e:
        print("error a occur with",e)

def brightness_control(hue_num,brgihtness,lights):
    try:
        lights[int(hue_num)-1].brightness = int(brgihtness)
    except Exception as e:
        print("error a occur with",e)

def color_control(hue_num, x,y,lights):
    try:
        lights[int(hue_num)-1].xy = [float(x),float(y)]
    except Exception as e:
        print("error a occur with",e)



def connect_bridge(bridge_ip):
    bridge = Bridge(bridge_ip)
    bridge.connect()
    return bridge

def main(FLAGS):
    print(FLAGS)
    bridge = connect_bridge(FLAGS.bridge)
    lights = bridge.lights
    print(lights)
    print(len(lights))
    server_socket = open_server_socket(FLAGS)
    accept_client(server_socket,lights)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--ipaddress', type=str,
                        default='localhost')
    parser.add_argument('-p', '--port', type=int,
                        default=1234)
    parser.add_argument('-b','--bridge', type=str,
                        default='192.168.0.14')
    FLAGS, _ = parser.parse_known_args()
    main(FLAGS)
