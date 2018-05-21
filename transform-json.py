#!/usr/bin/env python3
import json
import parser

# read in content
# This will be the same across content types.  I don't care where the content is
# stored; db, file, stream.  That's a job for another part of the system.  At
# this point, we've got the content loaded up ready to send in here.
with open('content-separation.txt') as content_file:
    content = content_file.read()
# TODO - Move reading of file out of here.


# understand parts
# This part will vary greatly based on the content.
content_without_signature = parser.get_content_without_signature(content)

meta = {}
meta['title'] = parser.get_meta_value(content_without_signature, 'title')
meta['author'] = parser.get_meta_value(content_without_signature, 'author')
meta['date'] = parser.get_meta_value(content_without_signature, 'date')

core_content = parser.get_content_without_meta(content_without_signature)



# spit out result
# This part would vary based on the system content is being processed for.
result = json.dumps({
    'meta': meta,
    'content': core_content,
    })


# TODO - Move writing of file out of here.
with open('content-separation.json', 'w') as transformed_file:
    transformed_file.write(result)
