import re

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
