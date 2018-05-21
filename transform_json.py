#!/usr/bin/env python3
import sys
import json
import parser
import read_content

# TODO - It is not our concern how the content is read.
# Purely for convenience, we're reading it in here.  This should probably be
# removed as it's not part of our objective.
content = read_content.read(sys.argv[1])


# understand parts
# This part will vary greatly based on the content.
content_without_signature = parser.get_content_without_signature(content)

meta = {}
meta['title'] = parser.get_meta_value(content_without_signature, 'title')
meta['author'] = parser.get_meta_value(content_without_signature, 'author')
meta['date'] = parser.get_meta_value(content_without_signature, 'date')

content_without_meta = parser.get_content_without_meta(content_without_signature)
content_stripped = content_without_meta.strip()
core_content = parser.unwrap(content_stripped)


# spit out result
# This part would vary based on the system content is being processed for.
transformed_content = json.dumps({
    'meta': meta,
    'content': core_content,
    })


# This isn't really a concern for this, but it's another convenience.
if len(sys.argv) > 2:
    output_file_path = sys.argv[2]
    with open(output_file_path, 'w') as transformed_file:
        transformed_file.write(transformed_content)
else:
    sys.stdout.write(transformed_content)
