#!/bin/bash

if [ -z "$1" ]; then
    echo "Error: No file specified."
    echo "Usage: $0 image.png"
    exit 1
fi

TARGET_FILE="$1"

if [ ! -f "$TARGET_FILE" ]; then
    echo "Error: File '$TARGET_FILE' not found."
    exit 1
fi

echo "Cleaning file: $TARGET_FILE..."

exiftool -all= -overwrite_original "$TARGET_FILE"

magick "$TARGET_FILE" -blur 0x0.5 -quality 99 "$TARGET_FILE"

echo "Done! '$TARGET_FILE' successfully wiped and overwritten."