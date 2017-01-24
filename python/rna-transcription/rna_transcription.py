

_COMPLEMENT = {
    'G': 'C',
    'C': 'G',
    'T': 'A',
    'A': 'U',
}


def to_rna(dna):
    try:
        return ''.join(_COMPLEMENT[n] for n in dna)
    except KeyError:
        return ''
