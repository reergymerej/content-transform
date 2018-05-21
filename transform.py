#!/usr/bin/env python3
import sys
import read_content

transform_type = sys.argv[1]
content = read_content.read(sys.argv[2])

if transform_type == 'json':
    import transform_json
    transformed_content = transform_json.transform(content)
else:
    print('I do not have that transform.', transform_type)
    transformed_content = 'XXX'


if len(sys.argv) > 3:
    output_file_path = sys.argv[3]
    with open(output_file_path, 'w') as transformed_file:
        transformed_file.write(transformed_content)
else:
    sys.stdout.write(transformed_content)
