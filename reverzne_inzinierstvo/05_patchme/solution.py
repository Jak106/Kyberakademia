# Encrypted values from binary
encrypted = [
    0xbbdb, 0xbbd9, 0xbc0b, 0xbbcf, 0xbc0a,
    0xbbcd, 0xbc0f, 0xbc0e, 0xbbcf, 0xbbc6, 0xbc44
]

def decrypt_FUN_0010121f(buf):
    for i in range(len(buf)):
        v = ~((buf[i] - 0xbc3b - i) & 0xFFFFFFFF) & 0xFFFFFFFF
        buf[i] = v

def decrypt_FUN_001011c5(buf):
    for i in range(len(buf)):
        buf[i] ^= i

def decrypt_FUN_00101149(buf):
    for i in range(len(buf)):
        v = (buf[i] + i) ^ 0xf1d6
        # Swap bytes (simulate htons)
        low = v & 0xFF
        high = (v >> 8) & 0xFF
        buf[i] = (low << 8) | high

# Begin decryption chain
buf = encrypted[:]
decrypt_FUN_0010121f(buf)
decrypt_FUN_001011c5(buf)
decrypt_FUN_00101149(buf)

# Reconstruct raw bytes
flag_bytes = []
for val in buf:
    flag_bytes.append(val & 0xFF)
    flag_bytes.append((val >> 8) & 0xFF)

# Decode the flag as UTF-8 or ASCII
try:
    flag = bytes(flag_bytes).decode('utf-8')
except UnicodeDecodeError:
    flag = bytes(flag_bytes).decode('latin-1')

print(f"[+] Decrypted Flag: {flag}")

