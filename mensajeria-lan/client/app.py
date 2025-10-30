import tkinter as tk
from tkinter import messagebox
import configparser
import os
from client import IMClient

try:
    from win10toast import ToastNotifier
    toaster = ToastNotifier()
except:
    toaster = None

def load_config():
    cfg = configparser.ConfigParser()
    if not os.path.exists('config.ini'):
        cfg['DEFAULT'] = {'server_ip': '127.0.0.1', 'server_port': '5000', 'name': 'Cliente1'}
        with open('config.ini', 'w') as f:
            cfg.write(f)
    cfg.read('config.ini')
    return cfg['DEFAULT']['server_ip'], int(cfg['DEFAULT']['server_port']), cfg['DEFAULT']['name']

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Mensajería LAN")
        self.geometry("400x450")
        self.server_ip, self.server_port, self.name = load_config()
        self.client = IMClient(self.server_ip, self.server_port, self.name, self.on_recv)
        try:
            self.client.connect()
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo conectar: {e}")
        self.build_ui()

    def build_ui(self):
        tk.Label(self, text=f"Usuario: {self.name}").pack(pady=5)
        self.text = tk.Text(self, state='disabled')
        self.text.pack(expand=True, fill='both', padx=10, pady=10)
        frame = tk.Frame(self)
        frame.pack(fill='x', pady=5)
        self.to_entry = tk.Entry(frame)
        self.to_entry.pack(side='left', expand=True, fill='x')
        self.to_entry.insert(0, 'broadcast')
        self.msg_entry = tk.Entry(frame, width=25)
        self.msg_entry.pack(side='left')
        tk.Button(frame, text="Enviar", command=self.send).pack(side='left', padx=5)

    def send(self):
        to = self.to_entry.get().strip()
        msg = self.msg_entry.get().strip()
        if msg:
            self.client.send_message(to, msg)
            self.append_text(f"[Yo → {to}] {msg}")
            self.msg_entry.delete(0, 'end')

    def on_recv(self, msg):
        sender = msg.get('from')
        body = msg.get('body')
        self.append_text(f"[{sender}] {body}")
        if toaster:
            toaster.show_toast(f"Mensaje de {sender}", body, duration=4, threaded=True)

    def append_text(self, txt):
        self.text.configure(state='normal')
        self.text.insert('end', txt + "\n")
        self.text.configure(state='disabled')
        self.text.see('end')

if __name__ == '__main__':
    App().mainloop()
