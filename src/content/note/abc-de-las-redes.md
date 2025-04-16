---
title: ABC de las Redes
description: Introducción sencilla y visual al funcionamiento de las redes informáticas. 
publishDate: "2025-04-14T12:23:00Z"
draft: false
---


## 🌐 Conceptos básicos

```
[PC] --[Red LAN]-- [Switch] --[Router]--> 🌍 Internet
```

- **LAN**: Red local (casa, oficina).
- **WLAN**: LAN con Wi-Fi.
- **WAN**: Conexión entre varias LANs, como Internet.
- **VLAN**: LAN virtual separada lógicamente aunque esté en la misma red física.

---

## 🧠 Modelo OSI vs TCP/IP

### Modelo OSI (teórico)

```
[7] Aplicación
[6] Presentación
[5] Sesión
[4] Transporte
[3] Red
[2] Enlace de datos
[1] Física
```

### Modelo TCP/IP (real)

```
[4] Aplicación
[3] Transporte
[2] Internet
[1] Acceso a red
```

- OSI: Más detallado, para entender procesos.
- TCP/IP: El que se usa en Internet.

---

## ✉️ Proceso de envío de datos (simplificado)

```
[Usuario A]
   |
[Aplicación]  (HTTP, DNS, etc)
   ↓
[TCP/IP]      (Divide en paquetes)
   ↓
[Red]         (Switch y Router)
   ↓
[Usuario B]
```

Cada capa agrega su información (encabezados) → se encapsula el mensaje → se envía → se desencapsula en destino.

---

## 🔀 Conmutación (Switch + MAC)

```
+--------+       +--------+       +--------+
|  PC A  | <---> | Switch | <---> |  PC B  |
+--------+       +--------+       +--------+
       MAC A       usa MACs       MAC B
```

El switch crea una tabla interna tipo:

| Dirección MAC | Puerto |
|---------------|--------|
| MAC A         | 1      |
| MAC B         | 2      |

Así sabe hacia dónde reenviar paquetes.

---

## 🛰️ Enrutamiento (Router + IP)

```
[Red A] --- [Router A] --- Internet --- [Router B] --- [Red B]
          ↑ Tabla de enrutamiento       ↓
          Usa IP + Máscara + Gateway para decidir
```

El router consulta su tabla:

| Red destino   | Gateway       | Interfaz |
|---------------|---------------|----------|
| 192.168.1.0/24| 0.0.0.0       | Eth0     |
| 10.0.0.0/8    | 192.168.1.1   | Eth1     |

---

## 📬 Ejemplo de IP y máscara

Supón:

- IP: `192.168.1.10`
- Máscara: `255.255.255.0`

Eso indica que el host pertenece a la red `192.168.1.0`, y si quiere hablar con una IP como `192.168.2.10`, debe salir por la **puerta de enlace** (el router).

---

## 🔑 Resumen de elementos clave

| Concepto               | Ejemplo                         | Explicación rápida                               |
|------------------------|----------------------------------|--------------------------------------------------|
| Dirección IP           | 192.168.1.10                    | Identifica un dispositivo en la red              |
| Máscara de red         | 255.255.255.0                   | Define a qué red pertenece la IP                 |
| Puerta de enlace       | 192.168.1.1                     | IP del router para salir de la red local         |
| Dirección MAC          | A1:B2:C3:D4:E5:F6               | Identifica de forma única una tarjeta de red     |
| DNS                    | `google.com → 142.250.64.78`   | Traduce nombres a direcciones IP                 |


