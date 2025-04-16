---
title: "Redes: La Base Invisible del Cloud Computing"
description: "Este post es sobre conceptos basicos de Redes"
publishDate: "15 April 2025"
tags: ["nube", "redes"]
draft: false
seriesId: citrus-docs
orderInSeries: 1
---
¿Por qué aprender redes?

Todo lo que haces en la nube, desde ejecutar una máquina virtual hasta desplegar una aplicación, ocurre en servidores que se comunican a través de la red.

Además, el hecho de que una correcta configuración de redes virtuales, balanceadores de carga, gateways y rutas optimizadas mejora significativamente el rendimiento de tus aplicaciones, son razones más que suficientes para aprender los conceptos básicos de redes.

Por eso, aquí te los muestro.


## Conceptos basicos

- **Protocolo**: Es el conjunto de reglas que las computadoras deben seguir para poder comunicarse.
- **Paquete**: Es la forma en que se dividen los datos para ser enviados por la red.
- **Nodo**: Cada computadora o dispositivo conectado a la red.
- **Puertos**: Son interfaces lógicas que permiten la conexión y diferenciación de servicios en una red.
- **Latencia**: El tiempo que demora un paquete en llegar a su destino.
- **LAN**: Red de Área Local. Es la red más básica, generalmente en un entorno doméstico o de oficina.
- **WLAN**: Es similar a la LAN, pero los dispositivos están conectados mediante Wi-Fi.
- **WAN**: Red de Área Amplia. Conecta distintas redes locales a través de grandes distancias, como lo hace Internet.
- **VLAN**: Red de Área Local Virtual. Permite segmentar una red física en múltiples redes lógicas.
- **Internet**: Es la interconexión de múltiples redes entre sí, a nivel mundial.
- **Hardware**:
  - **Host**: Dispositivos con los que el usuario interactúa (computadoras, teléfonos, etc.).
  - **Dispositivos de red**: Equipos que permiten la conexión (antenas, routers, switches, etc.).
  - **Adaptadores de red (NIC)**: Traducen la señal eléctrica o inalámbrica a un formato que la computadora puede procesar.

---

## Protocolos

- **Modelo OSI**: Modelo teórico compuesto por 7 capas que describen las etapas de una conexión de red.
- **Modelo TCP/IP**: Modelo práctico utilizado en redes reales.  
  - **TCP (Protocolo de Control de Transmisión)**: Se asegura de que los paquetes lleguen correctamente y establece la conexión.
  - **IP (Protocolo de Internet)**: Se encarga del enrutamiento, es decir, de encontrar la mejor ruta hacia el destino.
- Existen direcciones **IP dinámicas** y **estáticas**:
  - Las **estáticas** se usan en servicios o servidores que requieren una IP fija.
  - Las **dinámicas** se asignan automáticamente y suelen usarse en redes domésticas.
- **DNS (Sistema de Nombres de Dominio)**: Traduce nombres de dominio (como `google.com`) a direcciones IP que los dispositivos pueden entender.

---

## Conmutación

La **conmutación** es el proceso que permite interconectar dos hosts mediante un dispositivo de red, como un switch. Un **switch** recibe paquetes de datos de un dispositivo y los reenvía al destino correcto dentro de la misma red local.

La conmutación utiliza las **direcciones MAC**, que son códigos alfanuméricos únicos asignados de fábrica a cada dispositivo de red. Gracias a ellas, el switch sabe a qué dispositivo debe enviar los datos.

Las redes locales se diseñan de forma **jerárquica**, no horizontal, porque un diseño jerárquico permite que la red sea más escalable, ordenada y eficiente.

---

## Enrutamiento

Mientras la conmutación se usa dentro de una red local, el **enrutamiento** se encarga de conectar distintas redes entre sí.

Por ejemplo, si una red local A quiere comunicarse con una red local B o con Internet, ya no puede usar direcciones MAC. En ese caso, entra en juego el **router**, que utiliza una **tabla de enrutamiento** para decidir a dónde enviar los paquetes.

Tres conceptos clave en el enrutamiento:

- **Dirección IP**: Identifica de forma única a cada dispositivo en una red.
- **Máscara de red**: Indica al router si la dirección de destino pertenece a la misma red local o no.
- **Puerta de enlace predeterminada**: Es la dirección IP del router dentro de la red local. Todo el tráfico hacia redes externas se envía a esta dirección, para que el router lo encamine correctamente.
