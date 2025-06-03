import socket
import sys

def httpClient(server_host, server_port, filename):
    global client_socket
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((server_host, server_port))

        request = f"GET /{filename} HTTP/1.1\r\nHost: {server_host}\r\n\r\n"
        client_socket.sendall(request.encode())

        response = b""
        while True:
            part = client_socket.recv(1024)
            if not part:
                break
            response += part
        print(response.decode())
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client_socket.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Pemakaian: python client.py <server_host> <server_port> <file_to_request>")
        sys.exit(1)

    server_host = sys.argv[1]
    server_port = int(sys.argv[2])
    filename = sys.argv[3]

    httpClient(server_host, server_port, filename)