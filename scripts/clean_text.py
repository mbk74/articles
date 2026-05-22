#!/usr/bin/env python3
import sys
import re

def strip_ai_markers(text):
    # Regex pattern to catch zero-width spaces, joiners, and hidden word fragments
    hidden_chars = re.compile(r'[\u200B-\u200D\uFEFF\u00AD\u2060]')
    cleaned = hidden_chars.sub('', text)
    
    # Optional: Normalize standard AI-favored typography back to basic text
    cleaned = cleaned.replace('—', '-').replace('“', '"').replace('”', '"')
    cleaned = cleaned.replace('‘', "'").replace('’', "'")
    return cleaned

if __name__ == "__main__":
    # Allows reading from a file or piping text directly in the terminal
    input_text = sys.stdin.read()
    sys.stdout.write(strip_ai_markers(input_text))