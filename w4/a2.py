def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    return len(dna)


def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """
    return len(dna1) > len(dna2)


def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    return dna.count(nucleotide)


def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """
    return dna2 in dna1

def is_valid_sequence(dna):
    """ (str) -> bool

    Return True if and only if the DNA sequence dna is valid
    
    >>> is_valid_sequence('ATCG')
    True
    >>> is_valid_sequence('ATcG')
    False
    >>> is_valid_sequence('ABCG')
    False
    """
    result = True
    for char in dna:
        if char not in 'ATCG':
            result = False
    return result

def insert_sequence(dna1, dna2, index):
    """ (str, str, int) -> str

    Return the DNA sequence obtained by inserting the second DNA sequence dna2
    into the first DNA sequence dna1 at the given index.

    >>> insert_sequence('CCGG', 'AT', 2)
    CCATGG
    >>> insert_sequence('CCGG', 'AT', 4)
    CCGGAT
    """
    dna = dna1[:index] + dna2 + dna1[index:]
    return dna

def get_complement(nucleotide):
    """ (str) -> str

    Return the nucleotide's complement
    
    >>> get_complement('A')
    T
    >>> get_complement('G')
    C
    """
    if nucleotide in 'AT':
        return 'A' if 'T' in nucleotide else 'T'
    if nucleotide in 'GC':
        return 'G' if 'C' in nucleotide else 'C'

def get_complementary_sequence(dna):
    """ (str) -> str

    Return the DNA sequence that is complementary to the given DNA sequence dna
    
    >>> get_complementary_sequence('ACGTACG')
    'TGCATGC'
    >>> get_complementary_sequence('ATCG')
    'TAGC'
    """
    sequence = ''
    for nucleotide in dna:
        sequence = sequence + get_complement(nucleotide)
    return sequence
