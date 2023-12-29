"""Basic server"""
import socket

HOST = '127.0.0.1'
PORT = 8080

def handle_request(client):
    """Handles a client request"""
    request = client.recv(1012)
    print(request.decode())

    resp = "HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\n\r\nHello, World!"
    client.sendall(resp.encode())
    client.close()

def start_server():
    """Starts the server""" 
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen(1)
        print(f"Listening on {HOST}:{PORT}...")

        while True:
            conn, addr = s.accept()
            with conn:
                print(f"Connected by {addr}")
                handle_request(conn)

def make_request():
    """Makes a request to the server"""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))

        request = "GET / HTTP/1.1\r\nHost: localhost\r\n\r\n"
        s.sendall(request.encode())

        resp = b""

        while True:
            data = s.recv(1024)
            if not data:
                break
            resp += data

        return resp.decode()

if __name__ == '__main__':
    start_server()
    response = make_request()
    print(f'Response: {response}')
