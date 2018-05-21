#!/usr/bin/env python3
import sys
import parser

def transform(content):
    content_without_signature = parser.get_content_without_signature(content)
    content_without_meta = parser.get_content_without_meta(content_without_signature)
    content_stripped = content_without_meta.strip()
    core_content = parser.unwrap(content_stripped)
    blocks = parser.get_blocks(core_content)
    mapped_blocks = ''
    for block in blocks:
        mapped_blocks += f'<div class="block">{block}</div>'

    transformed_content = f'<div class="content">{mapped_blocks}</div>\n'

    return transformed_content

if __name__ == "__main__":
    content = sys.stdin.read()
    transformed_content = transform(content)
    sys.stdout.write(transformed_content)
