"""Lazy-evaluation versions of zip, map, and filter.
"""

# xzip.py version 0.1
# Written 23 June 2003 by andi payn <payn@myrealbox.com>
# This work is released under the LGPL, version 2.1 or later

from __future__ import generators

def xzip(*sequences):
    """xzip(seq1 [, seq2 [...]]) ->
                        generator for [(seq1[0], seq2[0] ...), (...)]

       Returns a lazy range of tuples, where each tuple contains the
       i-th element from each of the argument sequences. The returned
       range is truncated in length to the length of the shortest
       argument sequence.
    """
    if not sequences:
        raise TypeError, ("xzip() requires at least one sequence",)
    for i in xrange(min([len(sequence) for sequence in sequences])):
        yield [sequence[i] for sequence in sequences]

def xmap(function, *sequences):
    """xmap(function, sequence[, sequence, ...]) -> generator

       Sequentially generates the results of applying the function to
       the argument sequence(s). If more than one sequence is given,
       the function is called with an argument list consisting of the
       corresponding item of each sequence, substituting None for
       missing values when not all sequences have the same length. If
       the function is None, return a list of the items of the
       sequence (or a list of tuples if more than one sequence).
    """
    if not sequences:
        raise TypeError, ("xmap() requires at least two args",)
    def get(seq, i):
        if i < len(seq): return seq[i]
        else: return None
    if function:
        for i in xrange(max([len(sequence) for sequence in sequences])):
            yield function(*[get(sequence,i) for sequence in sequences])
    else:
        for i in xrange(max([len(sequence) for sequence in sequences])):
            yield tuple([get(sequence,i) for sequence in sequences])
        
def xfilter(function, sequence):
    """xfilter(function, sequence) -> generator

       Sequentially generates those items of sequence for which
       function(item) is true. If function is None, generate the items
       that are true.
    """
    for item in sequence:
        if function:
            if function(item): yield item
        else:
            if item: yield item
