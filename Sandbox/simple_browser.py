"""Simple browser implementation."""
import socket

HOST = '127.0.0.1'
PORT = 8080

def make_request():
    """Makes a request to the server"""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))

        request = "GET / HTTP/1.1\r\nHost: localhost:8080\r\n\r\n"
        s.sendall(request.encode())

        resp = b""

        while True:
            data = s.recv(1024)
            if not data:
                break
            resp += data

        return resp.decode()

if __name__ == '__main__':
    response = make_request()
    print(response)
