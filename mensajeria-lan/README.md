# 💬 Proyecto Final - Mensajería LAN (Python)

Aplicación de mensajería instantánea para red local (LAN), desarrollada en **Python**, con interfaz **Win32 (tkinter)**, configuración por archivo **INI**, empaquetada como **EXE** y con servidor en **Docker**.

## 🧠 Características
- Comunicación LAN en tiempo real.
- Notificaciones en Windows (`win10toast`).
- Configuración en `config.ini`.
- Cliente GUI (tkinter).
- Servidor multiusuario (socket TCP).
- Dockerfile incluido.
- EXE e instalador Inno Setup.

## ⚙️ Ejecución

### 🔸 Servidor
```bash
cd server
python server.py
```

### 🔹 Cliente
Editar `config.ini` y ejecutar:
```bash
cd client
python app.py
```

### 🐳 Docker
```bash
docker build -t mensajeria-lan-server .
docker run -d -p 5000:5000 mensajeria-lan-server
```

## 📦 Generar EXE
```bash
pyinstaller --onefile --windowed app.py --name MensajeriaLAN
```

## 🧰 Instalador
Abrir `installer/inno_script.iss` con **Inno Setup** y compilar.

## 🗂️ Configuración
Archivo `config.ini`:
```ini
[DEFAULT]
server_ip = 192.168.1.10
server_port = 5000
name = Alumno1
```

## 📄 Licencia
MIT License © 2025
