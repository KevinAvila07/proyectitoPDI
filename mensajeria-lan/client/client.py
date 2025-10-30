import socket
import threading
import json
import time

class IMClient:
    def __init__(self, server_ip, server_port, name, recv_callback=None):
        self.server_ip = server_ip
        self.server_port = server_port
        self.name = name
        self.sock = None
        self.recv_callback = recv_callback
        self.running = False

    def connect(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.server_ip, self.server_port))
        reg = {'type': 'register', 'from': self.name}
        self.sock.sendall((json.dumps(reg) + "\n").encode('utf-8'))
        self.running = True
        threading.Thread(target=self._recv_loop, daemon=True).start()

    def _recv_loop(self):
        buffer = ""
        while self.running:
            try:
                data = self.sock.recv(1024)
                if not data:
                    break
                buffer += data.decode('utf-8')
                while '\n' in buffer:
                    line, buffer = buffer.split('\n', 1)
                    msg = json.loads(line)
                    if self.recv_callback:
                        self.recv_callback(msg)
            except:
                time.sleep(1)
                break
        self.running = False

    def send_message(self, to, body):
        msg = {'type': 'message', 'from': self.name, 'to': to, 'body': body}
        self.sock.sendall((json.dumps(msg) + "\n").encode('utf-8'))

    def request_list(self):
        req = {'type': 'list', 'from': self.name}
        self.sock.sendall((json.dumps(req) + "\n").encode('utf-8'))

    def close(self):
        self.running = False
        try:
            self.sock.close()
        except:
            pass
