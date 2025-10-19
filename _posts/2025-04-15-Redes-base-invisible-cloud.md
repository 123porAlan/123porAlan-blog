---
layout: post
title: Networking, the Invisible Foundation of Cloud Computing
date: 2025-04-15 15:01:35 +0300
last_modified_at: 2025-04-15
categories: [Quality Assurance]
---

Why learn networking?

Everything you do in the cloud, from running a virtual machine to deploying an application, occurs on servers that communicate over the network.

Furthermore, the fact that a correct configuration of virtual networks, load balancers, gateways, and optimized routes significantly improves the performance of your applications, are more than enough reasons to learn the basics of networking.

That's why I'm showing them to you here.

## Basic Concepts

- **Protocol**: It's the set of rules that computers must follow to be able to communicate.
- **Packet**: It's the way data is divided to be sent over the network.
- **Node**: Each computer or device connected to the network.
- **Ports**: These are logical interfaces that allow the connection and differentiation of services on a network.
- **Latency**: The time it takes for a packet to reach its destination.
- **LAN**: Local Area Network. It's the most basic network, usually in a home or office environment.
- **WLAN**: It's similar to LAN, but the devices are connected via Wi-Fi.
- **WAN**: Wide Area Network. Connects different local networks over large distances, as the Internet does.
- **VLAN**: Virtual Local Area Network. Allows segmenting a physical network into multiple logical networks.
- **Internet**: It is the interconnection of multiple networks with each other, worldwide.
- **Hardware**:
  - **Host**: Devices the user interacts with (computers, phones, etc.).
  - **Network devices**: Equipment that allows connection (antennas, routers, switches, etc.).
  - **Network Interface Controllers (NIC)**: They translate the electrical or wireless signal into a format the computer can process.

---

## Protocols

- **OSI Model**: A theoretical model composed of 7 layers that describe the stages of a network connection.
- **TCP/IP Model**: A practical model used in real networks.
  - **TCP (Transmission Control Protocol)**: It ensures that packets arrive correctly and establishes the connection.
  - **IP (Internet Protocol)**: It is responsible for routing, that is, finding the best path to the destination.
- There are **dynamic** and **static** IP addresses:
  - **Static** ones are used for services or servers that require a fixed IP.
  - **Dynamic** ones are assigned automatically and are usually used in home networks.
- **DNS (Domain Name System)**: Translates domain names (like `google.com`) into IP addresses that devices can understand.

---

## Switching

**Switching** is the process that allows two hosts to be interconnected using a network device, such as a switch. A **switch** receives data packets from one device and forwards them to the correct destination within the same local network.

Switching uses **MAC addresses**, which are unique alphanumeric codes assigned at the factory to each network device. Thanks to them, the switch knows which device to send the data to.

Local networks are designed **hierarchically**, not horizontally, because a hierarchical design allows the network to be more scalable, orderly, and efficient.

---

## Routing

While switching is used within a local network, **routing** is responsible for connecting different networks to each other.

For example, if a local network A wants to communicate with a local network B or with the Internet, it can no longer use MAC addresses. In that case, the **router** comes into play, which uses a **routing table** to decide where to send the packets.

Three key concepts in routing:

- **IP Address**: Uniquely identifies each device on a network.
- **Subnet Mask**: Tells the router whether the destination address belongs to the same local network or not.
- **Default Gateway**: It is the router's IP address within the local network. All traffic to external networks is sent to this address, so the router can route it correctly.
