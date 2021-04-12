import hashlib

import api.schemas as schemas


def hash_md5(human_dna: schemas.HumanDNA):
    """Generate hash MD5 from HumanDNA."""
    str_dna = ''.join(human_dna.dna)

    return str_dna, hashlib.md5(str_dna.encode())
