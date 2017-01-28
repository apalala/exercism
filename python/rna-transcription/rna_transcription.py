

_COMPLEMENT = dict(zip('GCTA', 'CGAU'))


def to_rna(dna):
    try:
        return ''.join(_COMPLEMENT[n] for n in dna)
    except KeyError:
        return ''
