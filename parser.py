import re

def get_meta(content):
    meta = {}
    meta['title'] = get_meta_value(content, 'title')
    meta['author'] = get_meta_value(content, 'author')
    meta['date'] = get_meta_value(content, 'date')
    return meta

def get_meta_value(content, meta_prop):
    pattern = f'^{meta_prop}:\s+([^\s].+)'
    match = re.search(pattern, content, re.MULTILINE)
    if match:
        return match.group(1)

def has_pgp_signature(content):
    return bool(re.search('^-----BEGIN PGP SIGNED MESSAGE-----', content))

def get_content_without_signature(content):
    is_signed_content = has_pgp_signature(content)
    if is_signed_content:
        pattern = '-----BEGIN PGP SIGNED MESSAGE-----\nHash:[^\n]+\n(.*)-----BEGIN PGP SIGNATURE-----'
        match = re.search(pattern, content, flags=re.MULTILINE|re.DOTALL)
        if match:
            # TODO: remove - prefixes
            return match.group(1)
    else:
        return content

def get_content_without_meta(content):
    # This assumes the meta is the first thing in the content.
    # If there is no meta, this should not be called (as it will goof up).
    pattern = '^(.+?---)?.+?---\n'
    return re.sub(pattern, '', content, 1, flags=re.MULTILINE|re.DOTALL)

def unwrap(content):
    pattern = '([^\n])\n([^\n])'
    replacement = r'\1 \2'
    return re.sub(pattern, replacement, content, 0, flags=re.MULTILINE|re.DOTALL)

def get_sections(content):
    # for signed with dash
    pattern = r'\n- ---'
    result = re.split(pattern, content, 0, flags=re.MULTILINE|re.DOTALL)

    # if not signed
    pattern = r'\n---'
    result = re.split(pattern, '\n---'.join(result), 0, flags=re.MULTILINE|re.DOTALL)

    return [x.strip() for x in result]

def get_paragraphs(section):
    pattern = r'\n\n'
    result = re.split(pattern, section, 0, flags=re.MULTILINE|re.DOTALL)

    return [x.strip() for x in result]
