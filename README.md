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
# transform to json, print
./transform.py json content.txt

# transform to json, pretty print
./transform.py json content.txt | python3 -m json.tool

# transform to json, save to content.json
./transform.py json content.txt > content.json

# transform to html
./transform.py html content.txt
```
