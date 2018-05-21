#!/usr/bin/env python3
import json
import re

# read in content
# This will be the same across content types.  I don't care where the content is
# stored; db, file, stream.  That's a job for another part of the system.  At
# this point, we've got the content loaded up ready to send in here.
with open('content-separation.txt') as content_file:
    content = content_file.read()
# TODO - Move reading of file out of here.


# understand parts
# This part will vary greatly based on the content.
parsed_content = {}

title_match = re.search('^title:\s+([^\s].+)', content, re.MULTILINE)
title = None
if title_match:
    title = title_match.group(1)
    print(title)
parsed_content['title'] = title





parsed_content['without_signature'] = 'xxxxxxx'


# spit out result
# This part would vary based on the system content is being processed for.
result = json.dumps({
    'title': parsed_content['title'],
    'content': parsed_content['without_signature'],
    })


# TODO - Move writing of file out of here.
with open('content-separation.json', 'w') as transformed_file:
    transformed_file.write(result)
