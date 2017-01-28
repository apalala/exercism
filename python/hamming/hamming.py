

def distance(aseq, bseq):
    if len(aseq) != len(bseq):
        raise ValueError('Sequence lengths differ')
    return sum(a != b for a, b in zip(aseq, bseq))