import socket
import threading
import json

HOST = '0.0.0.0'
PORT = 5000
clients = {}
lock = threading.Lock()

def broadcast(msg_json, exclude=None):
    data = (json.dumps(msg_json) + "\n").encode('utf-8')
    with lock:
        for cid, (conn, _) in clients.items():
            if exclude and cid == exclude:
                continue
            try:
                conn.sendall(data)
            except:
                pass

def handle_client(conn, addr):
    buffer = ""
    client_id = None
    try:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            buffer += data.decode('utf-8')
            while '\n' in buffer:
                line, buffer = buffer.split('\n', 1)
                try:
                    msg = json.loads(line)
                except:
                    continue
                t = msg.get('type')
                if t == 'register':
                    client_id = msg.get('from')
                    with lock:
                        clients[client_id] = (conn, addr)
                    print(f"{client_id} conectado desde {addr}")
                elif t == 'message':
                    to = msg.get('to')
                    if to == 'broadcast':
                        broadcast(msg)
                    else:
                        with lock:
                            target = clients.get(to)
                        if target:
                            try:
                                target[0].sendall((json.dumps(msg) + "\n").encode('utf-8'))
                            except:
                                pass
                elif t == 'list':
                    with lock:
                        names = list(clients.keys())
                    resp = {
                        'type': 'list_response',
                        'from': 'server',
                        'to': msg.get('from'),
                        'body': names
                    }
                    conn.sendall((json.dumps(resp) + "\n").encode('utf-8'))
    finally:
        with lock:
            if client_id and client_id in clients:
                del clients[client_id]
        conn.close()
        print(f"Desconectado: {addr}")

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(50)
    print(f"Servidor escuchando en {HOST}:{PORT}")
    try:
        while True:
            conn, addr = s.accept()
            threading.Thread(target=handle_client, args=(conn, addr), daemon=True).start()
    except KeyboardInterrupt:
        s.close()

if __name__ == '__main__':
    main()
