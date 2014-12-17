import hashlib

def md5hasher(s):
    return hashlib.md5(s).hexdigest()
