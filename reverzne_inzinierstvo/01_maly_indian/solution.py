encrypted_bytes = [-0x65, -0x68, -0x62, -0x65, -0x61, -0x7b, -0x7b, 0xde, -0x28, -0x21, -0x3c, -0x32, -0x31, -0x28]

encrypted_bytes = [(b + 256) if b < 0 else b for b in encrypted_bytes]

decrypted_bytes = [b ^ 0xAA for b in encrypted_bytes]

password = ''.join(chr(b) for b in decrypted_bytes)

print("Decrypted Password:", password)
