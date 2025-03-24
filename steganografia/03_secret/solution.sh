#!/bin/bash

extract_archive() {
    local archive="$1"
    local extract_to="$archive"_extracted
    mkdir -p "$extract_to"
    
    case "$archive" in
        *.zip)
            unzip -o "$archive" -d "$extract_to" ;;
        *.tar)
            tar -xf "$archive" -C "$extract_to" ;;
        *.tar.gz|*.tgz)
            tar -xzf "$archive" -C "$extract_to" ;;
        *.tar.bz2)
            tar -xjf "$archive" -C "$extract_to" ;;
        *.tar.xz)
            tar -xJf "$archive" -C "$extract_to" ;;
        *.rar)
            unrar x -o+ "$archive" "$extract_to" ;;
        *.7z)
            7z x "$archive" -o"$extract_to" ;;
        *)
            echo "Unsupported format: $archive" ;;
    esac
}

recursively_extract() {
    local directory="$1"
    find "$directory" -type f \( -iname "*.zip" -o -iname "*.tar" -o -iname "*.tar.gz" -o -iname "*.tgz" -o -iname "*.tar.bz2" -o -iname "*.tar.xz" -o -iname "*.rar" -o -iname "*.7z" \) | while read -r file; do
        echo "Extracting: $file"
        extract_archive "$file"
        recursively_extract "$file"_extracted
    done
}

read -rp "Enter directory to scan for archives: " target_directory
recursively_extract "$target_directory"
