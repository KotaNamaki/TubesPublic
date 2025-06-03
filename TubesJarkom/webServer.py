import socket
import threading

class Webserver:
    def __init__(self, host = '', port= 4040):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    def start(self):
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        print("Server Listen at port:", self.port)
        try:
            while True:
                try:
                    client_socket, client_address = self.server_socket.accept()
                    print(f"Koneksi dari {client_address} telah berhasil dibuka!")
                    client_thread = threading.Thread(
                        target = self.handle_client,
                        args = (client_socket,)
                    )
                    client_thread.start()
                except socket.timeout:
                    continue
        except KeyboardInterrupt:
            print("Shutting down server....")
            self.server_socket.close()
            print("Server closed!")
    def handle_client(self, client_socket):
        request_data = client_socket.recv(1024).decode()
        if not request_data:
            print("Client disconnected!")
            client_socket.close()
            return
        request_lines = request_data.split('\r\n')
        request_line = request_lines[0]
        method, path, _ = request_line.split()

        if method != 'GET':
            response = f"HTTP/1.1 405 Method Not Allowed\r\n\r\n"
            client_socket.sendall(response.encode())
            client_socket.close()
            return

        if path == '/':
            path = '/index.html'

        if path == '/notify':
            message = "Message send receive"
            response = (
                "HTTP/1.1 200 OK\r\n"
                f"Content-Length: {len(message)}\r\n"
                "Content-Type: text/plain\r\n"
                "\r\n"
                + message
            )
            client_socket.sendall(response.encode())
            client_socket.close()
            return

        try:
            with open('.' + path, 'rb') as file:
                content = file.read()
                response_headers = (
                    "HTTP/1.1 200 OK\r\n"
                    f"Content-Length: {len(content)}\r\n"
                    "Content-Type: text/html\r\n"
                    "\r\n"
                ).encode()
                client_socket.sendall(response_headers + content)
        except FileNotFoundError:
            response = (
                "HTTP/1.1 404 Not Found\r\n"
                "Content-Type: text/html\r\n"
                "\r\n"
                "<html><body><h1>404 Not Found</h1></body></html>"
            )
            client_socket.sendall(response.encode())
        except Exception as e:
            print(f"Error {e}")
            response = (
                "HTTP/1.1 500 Internal Server Error\r\n"
                "Content-Type: text/html\r\n"
                "\r\n"
                "<html><body><h1>500 Internal Server Error</h1></body></html>"
            )
            client_socket.sendall(response.encode())
        finally:
            client_socket.close()

if __name__ == "__main__":
    webserver = Webserver()
    webserver.start()