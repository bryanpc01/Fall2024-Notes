---
title: Subnetting Cheatsheet
description: A collection of subnetting reference resources. Resources include tables, subnetting methods, the magic number, and more.
---
# Subnetting Cheatsheet

## Reference Charts

### Binary Reference
|2^7^|2^6^|2^5^|2^4^|2^3^|2^2^|2^1^|2^0^|
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
|128 |64  |32  |16  |8   |4   |2   |1   |

<!-- ### Classful Address Ranges
|Class A             |Class B               |Class C                  |
|-------------------|-----------------------|-------------------------|
|1.0.0.0 - 126.0.0.0|128.0.0.0 - 191.255.0.0|192.0.1.0 - 223.255.255.0| -->

<!-- ### IPv4 Subnet Chart -->

<!-- ## The Magic Bit Method -->

## Reserved Addresses
### Private IP Addresses (RFC 1918)
|Address Block|Range|
|-----|------|
|10.0.0.0/8|10.0.0.0 - 10.255.255.255|
|172.16.0.0/12|172.16.0.0 - 172.31.255.255|
|192.168.0.0/16|192.168.0.0 - 192.168.255.255|

### Loopback Addresses (RFC 1122, Section 3.2.1.3)
|Address Block|Range|
|-----|------|
|127.0.0.0/8|127.0.0.0 - 127.255.255.255|

### Multicast Addresses (RFC 3171)
|Address Block|Range|
|-----|------|
|224.0.0.0/4|224.0.0.0 - 239.255.255.255|

<!-- ## Examples Problems
### Network Address
### Broadcast Address
### Number of Usable Hosts -->

## RFC References
### IETF Datatracker Website
>   The IETF Datatracker is the day-to-day front-end to the IETF database for people who work on IETF standards.
    It contains data about the documents, working groups, meetings, agendas, minutes, presentations, and more, of the IETF.  

[https://datatracker.ietf.org/](https://datatracker.ietf.org/)
### Useful RFCs
=== "RFC 917"
    <h2>Internet Subnets</h2>  
    
    Jeffrey Mogul  
    Computer Science Department  
    Stanford University  

    October 1984  

    [Link to RFC 917: IETF Datatracker](https://datatracker.ietf.org/doc/html/rfc917)

=== "RFC 950"
    <h2>Internet Standard Subnetting Procedure</h2>  

    J. Mogul (Stanford)  
    J. Postel (ISI)  

    August 1985  

    [Link to RFC 950: IETF Datatracker](https://datatracker.ietf.org/doc/html/rfc950)

=== "RFC 1918"
    <h2>Address Allocation for Private Internets</h2>  

    Y. Rekhter (Cisco Systems)  
    B. Moskowitz (Chrysler Corp.)  
    D. Karrenberg (RIPE NCC)  
    G. J. de Groot (RIPE NCC)  
    E. Lear (Silicon Graphics, Inc.)  

    February 1996  

    [Link to RFC 1918: IETF Datatracker](https://datatracker.ietf.org/doc/html/rfc1918)

=== "RFC 6890"
    <h2>Special-Purpose IP Address Registries</h2>  

    M. Cotton  
    L. Vegoda (ICANN)  
    R. Bonica, ED. (Juniper Networks)  
    B. Haberman (JHU)  

    April 2013  

    [Link to RFC 6890: IETF Datatracker](https://datatracker.ietf.org/doc/html/rfc6890#page-6)