---
title: NetSec Notes
description: Network Security notes for my CS-GY 6823 course at NYU.
---

# Network Security Notes

## Finding IP Addresses
Commands used to get the IP address of a NIC. 

``` hl_lines="5 11"
$ ip address

1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host noprefixroute
       valid_lft forever preferred_lft forever
2: wlan0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default qlen 1000
    link/ether 48:68:4a:9f:04:9d brd ff:ff:ff:ff:ff:ff
    inet 192.168.10.104/24 brd 192.168.10.255 scope global dynamic noprefixroute wlan0
       valid_lft 52893sec preferred_lft 52893sec
    inet6 fe80::f75c:b3fa:2035:7ed2/64 scope link noprefixroute
       valid_lft forever preferred_lft forever
```

The previous `#!bash ip address` command is extreamly verbose. The `#!bash -br` flag is used for brevity. 
``` hl_lines="3 4"
$ ip -br address

lo               UNKNOWN        127.0.0.1/8 ::1/128
wlan0            UP             192.168.10.104/24 fe80::f75c:b3fa:2035:7ed2/64
```
Commands to get the IP address from a hostname.
``` hl_lines="4"
$ dig www.example.com
...
;; ANSWER SECTION:
www.example.com.	1054	IN	A	93.184.215.14
```
## Sending Packets
Netcat can be used as a simple UDP server. 
```
$ nc -lnuv 9090 
```
While the UDP server is listening on port 9090 we can send data via a simple UDP client. 

``` py title="simple-udp-client.py"
--8<-- "snippets/simple-udp-client.py"
```

## Receiving Packets
We can listen for data via a simple UDP server. 
``` py title="simple-udp-server.py"
--8<-- "snippets/simple-udp-server.py"
```

Netcat can be used as a simple UDP client.
```
$ nc -u 127.0.0.1 9090
```

## Routing Commands
Command to look at the routing table
```
$ ip route
```

Command to see which interface will send packets to a particulaar destination
```
$ ip route get 8.8.8.8
```

## Packet-Sending Tools
Netcat is a tool that can send UDP and TCP packets. 

```
$ nc <ip> <port>     # send TCP packet
$ nc -u <ip> <port>  # send UDP packet
```

Bash's pseudo device can send UDP and TCP packets.
```bash
// sending data via TCP
$ echo "data" > /dev/tcp/<ip>/<port>

// sending data via UDP
$ echo "data" > /dev/udp/<ip>/<port>
```

Telnet sends TCP packets.
```
$ telnet <ip>
```

Ping sends ICMP packets.
```
$ ping <ip>
```
## View open ports
```
$ netstat -tna 
```

## Packet Construction
<figure markdown="span">
   ![Layers of OSI](https://upload.wikimedia.org/wikipedia/commons/0/0e/Layers_of_OSI_modles.png)
   <figcaption><a href="https://commons.wikimedia.org/wiki/File:Layers_of_OSI_modles.png">Moeenrahi</a>, <a href="https://creativecommons.org/licenses/by-sa/4.0">CC BY-SA 4.0</a>, via Wikimedia Commons</figcaption>
</figure>

### Transport Layer
- Payload -> Transport Layer: 
- transport-layer header added. 
- UDP or TCP
> Most Important Information: Source/Destination Port Numbers. 
### Network Layer
- IP header is added.
- Routing happens here as well.
> Most Important Information: Source/Destination IP Addresses.
### Data-Link Layer
- MAC-layer header is added.
> Most Important Information: Source/Destination MAC Addresses. 

