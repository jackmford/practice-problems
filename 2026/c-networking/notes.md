# notes

## reading beej's guide

- any I/O in Unix is done through a file descriptor (FD) (an integer associated with an open file), even networking
- the _socket()_ system routine provides the network FD

- a more consistent OSI model with Unix:
  - Application Layer (telnet, ftp, etc.)
  - Host-to-Host Transport Layer (TCP, UDP)
  - Internet Layer (IP and routing)
  - Network Access Layer (Ethernet, wi-fi, or whatever)

- ipv6 is 8, two byte chunks separated by colons
- network portion of the IP address is the _netmask_ (255.255.255.0 AND 192.0.2.12 == 192.0.2.0 (your subnet))
  - the new style does this same thing but in this notation: 192.0.2.12/30 -> indicating there are 30 network bits and 2 host bits
    - so 192.0.2.12, 192.0.2.13, 192.0.2.14, 192.0.2.15 would be available on the host
  - ipv6 -> 2001:db8:5413:4028::9db9/64 -> indicates the first 64 bits of the network, with 64 bits (/64) left for the host

- port == 16 bit number like a local address for the connection
- `cat /etc/services` file on Unix shows service port numbers

- _Big Endian_ wherein the "big" end of the number is stored first
  - big endian is also called _Network Byte Order_
  - computers store bytes in _Host Byte Order_, Intel is little-endian
- _Little Endian_ the bytes are stored "small" end first

- you can convert short (two bytes) and long (four bytes) numbers to Network Byte Order with various builtin functions in C
  - htons() -> host to network short
  - htonl() -> host to network long
  - ntohs() -> network to host short
  - ntohl() -> network to host long

- AF_INET (AF means Address Family)
- PF_INET (PF means Protocol Family)

- send() and recv() are for SOCK_STREAM (TCP) connections
- sendto() and recvfrom() are for SOCK_DGRAM (UDP) connections

- you can still use send() and recv() with a datagram socket that you connect() to, the kernel will just remember the destination port/ip for you instead of having to pass it like in sendto() and recvfrom()
