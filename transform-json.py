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
meta = {}
meta['title'] = parser.get_meta_value(content, 'title')
meta['author'] = parser.get_meta_value(content, 'author')
meta['date'] = parser.get_meta_value(content, 'date')

parsed_content = {}
parsed_content['without_signature'] = parser.get_content_without_signature(content)



# spit out result
# This part would vary based on the system content is being processed for.
result = json.dumps({
    'meta': meta,
    'content': parsed_content['without_signature'],
    })


# TODO - Move writing of file out of here.
with open('content-separation.json', 'w') as transformed_file:
    transformed_file.write(result)
