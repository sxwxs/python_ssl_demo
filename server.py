import socket
import ssl
import os

base_dir = os.path.dirname(os.path.realpath(__file__))

def start_listen():
    # 生成SSL上下文
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    # 加载服务器所用证书和私钥
    context.load_cert_chain(os.path.join(base_dir, 'server.crt'), os.path.join(base_dir, 'server.pem'))
    context.load_verify_locations(os.path.join(base_dir, 'CA_cert.crt'))
    context.verify_mode = ssl.CERT_REQUIRED
    # 监听端口
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as sock:
        sock.bind(('127.0.0.1', 1507))
        sock.listen(5)
        print ('start listen...')
        with context.wrap_socket(sock, server_side=True) as ssock:
            while True:
                client_socket, addr = ssock.accept()
                msg = client_socket.recv(1024).decode("utf-8")
                print(f"client {addr} say：{msg}")
                msg = "Hello client".encode("utf-8")
                client_socket.send(msg)
                client_socket.close()

if __name__ == "__main__":
    start_listen()