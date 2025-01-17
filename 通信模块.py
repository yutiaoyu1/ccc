import socket

def create_hotspot():
    # 模拟热点创建
    print("PC端热点已创建")

def connect_to_pc_hotspot():
    # 模拟连接到PC端热点
    print("已连接到PC端热点")

def connect_to_remote_server(server_ip, server_port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, server_port))
    return client_socket

def send_file_via_socket(client_socket, file_path):
    with open(file_path, 'rb') as file:
        data = file.read(4096)
        while data:
            client_socket.send(data)
            data = file.read(4096)
    file.close()
    client_socket.close()
    print("文件传输成功")
