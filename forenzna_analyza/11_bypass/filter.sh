#!/bin/bash

for i in {1..5}; do
    file="log_$i.txt"
    if [[ -f "$file" ]]; then
        echo "[*] Searching in $file"
        grep "\.exe" "$file"
    else
        echo "[-] File $file not found"
    fi
done

