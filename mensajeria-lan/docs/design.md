# Diseño del Sistema de Mensajería LAN

## Componentes
- **Servidor:** Administra las conexiones de los clientes y enruta mensajes.
- **Cliente:** Envía y recibe mensajes a través de sockets TCP.

## Protocolo
- Comunicación en formato JSON con campos:
  - `type`: tipo de mensaje (`register`, `message`, `list`).
  - `from`: emisor.
  - `to`: destinatario o `broadcast`.
  - `body`: texto del mensaje.

## Flujo Básico
1. Cliente se conecta y envía `register`.
2. Servidor lo registra y puede reenviar mensajes a otros clientes.
3. Los clientes se comunican entre sí o en modo broadcast.

## Requerimientos
- Python 3.11+
- LAN con IP fija para el servidor.
- Windows 10+ para cliente (notificaciones).
