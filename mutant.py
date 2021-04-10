from itertools import groupby
from numpy import array, fliplr


def all_equal(iterable):
    iterable.sort()
    g = groupby(iterable)
    return next(g, True) and not next(g, False)


def is_mutant(dna):
    """Check if DNA is from a mutant. Return boolean."""
    seq_counter = 0

    arr_dna = array([[char for char in x] for x in dna])

    dimension = arr_dna.shape

    # Check for rows
    start = end = 0
    for i in range(dimension[1]-3):
        start = i
        end = i + 4
        arr_seq = arr_dna[:, start:end]
        for seq in arr_seq:
            if all_equal(list(seq)):
                seq_counter += 1
                if seq_counter > 1:
                    return True

    # Check for columns
    start = end = 0
    for i in range(dimension[0]-3):
        start = i
        end = i + 4
        cols = [list(arr_dna[start:end, x]) for x in range(dimension[1]*-1, 0)]
        for seq in cols:
            if all_equal(seq):
                seq_counter += 1
                if seq_counter > 1:
                    return True

    # Check for diagonals
    for i in range(dimension[0]-3):
        start_i = i
        end_i = i + 4
        for j in range(dimension[1]-3):
            start_j = j
            end_j = j + 4
            arr_seq = arr_dna[start_i:end_i, start_j:end_j]
            if all_equal(list(arr_seq.diagonal())):
                seq_counter += 1
                if seq_counter > 1:
                    return True

            arr_seq_flipped = fliplr(arr_seq)
            if all_equal(list(arr_seq_flipped.diagonal())):
                seq_counter += 1
                if seq_counter > 1:
                    return True

    return False
