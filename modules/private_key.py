from pathlib import Path

def run():
    homepath = Path.home()
    private_key = homepath / '.ssh' / 'id_rsa'

    with open(private_key, 'r') as f:
        key = f.read()
    return key
