# Trasnform Content

This reads plain text content and spits out html.  Like Markdown, but probably
not as good.  ;)

Actually, it's not quite like markdown.  This only concerned with interpreting
content's structure and generating another structure with the content folded in.

transform(content) => json
transform2(content) => html
transform3(content) => html with utility classes


## Usage

```sh
# read source
./read_content.py content/utility-css.txt

# read source, print to stdout
./transform_json.py content.txt

# read source, print to stdout, and make it pretty
./transform_json.py content.txt | python3 -m json.tool

# read source, print to foo.json
./transform_json.py content.txt > foo.json
# or
./transform_json.py content.txt foo.json
```
