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
            return match.group(1)
    else:
        return content
