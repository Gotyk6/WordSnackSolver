from itertools import permutations
import itertools
import operator


def sort_uniq(sequence):
    return list(map(
        operator.itemgetter(0),
        itertools.groupby(sorted(sequence))))


def perm(word, size):
    perms = [''.join(p) for p in permutations(word, size)]
    return sort_uniq(perms)
