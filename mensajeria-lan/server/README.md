# Servidor de Mensajería LAN

Servidor TCP simple que enruta mensajes entre clientes en la red local.

## Ejecución local
```bash
python server.py
```

## Docker
```bash
docker build -t mensajeria-lan-server .
docker run -d -p 5000:5000 mensajeria-lan-server
```
