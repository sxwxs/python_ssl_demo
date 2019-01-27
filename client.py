import socket
import ssl
import os

base_dir = os.path.dirname(os.path.realpath(__file__))

def connect_server():
    # 生成SSL上下文
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    # 加载信任根证书
    context.load_verify_locations(os.path.join(base_dir, 'CA_cert.crt'))
    context.load_cert_chain(os.path.join(base_dir, 'client.crt'), os.path.join(base_dir, 'client.pem'))
    # 与服务端建立socket连接
    with socket.create_connection(('127.0.0.1', 1507)) as sock:
        # 这里的server_hostname不是指服务端IP，而是指服务端证书中设置的CN
        with context.wrap_socket(sock, server_hostname='server') as ssock:
            # 向服务端发送信息
            msg = "Hello server".encode("utf-8")
            ssock.send(msg)
            # 接收服务端返回的信息
            msg = ssock.recv(1024).decode("utf-8")
            print(f"server says: {msg}")
            ssock.close()

if __name__ == "__main__":
    connect_server()