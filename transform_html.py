#!/usr/bin/env python3
import sys
import parser

def transform(content):
    content_without_signature = parser.get_content_without_signature(content)
    content_without_meta = parser.get_content_without_meta(content_without_signature)
    content_stripped = content_without_meta.strip()
    core_content = parser.unwrap(content_stripped)
    sections = parser.get_sections(core_content)
    sections_html = ''
    for section in sections:
        paragraphs_html = ''
        paragraphs = parser.get_paragraphs(section)
        for paragraph in paragraphs:
            paragraphs_html += f'<p>{paragraph}</p>'

        sections_html += f'<section>{paragraphs_html}</section>'

    transformed_content = f'<div class="content">{sections_html}</div>\n'

    return transformed_content

if __name__ == "__main__":
    content = sys.stdin.read()
    transformed_content = transform(content)
    sys.stdout.write(transformed_content)
