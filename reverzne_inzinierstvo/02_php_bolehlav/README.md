1. Onubfuscating this challenge took multiple steps. First there was original php script. I rewrote it into ```v1.py```. It contained XOR cypher to decrypt input. Decrypted string is b64 encoded.

2. After saving decoded output into ```v2.php``` i noticed interesting string encoded in b64 ```ZWNobyAtbiAiZmZmbGZhZmdna2ZkY2NjOWZiZmZnZWNlZmNmYWdkY2FjOWZuZW9nZ2NhZ2pjZGdiZmRnbSIgfCB0ciAnOWEtekEtWl97fTAtJyAnMC05YS16QS1aX3snIHwgeHhkIC1yIC1w``` i decoded this string.

3. Once i decoded this string i noticed shell command ```echo -n "ffflfafggkfdccc9fbffgecefcfagdcac9fneoggcagjcdgbfdgm" | tr '9a-zA-Z_{}0-' '0-9a-zA-Z_{' | xxd -r -p```

4. It translates the string, decodes it from hex and outputs the result which is the flag flag{```redacted```}
