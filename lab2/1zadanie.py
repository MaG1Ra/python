def first():
    """
    
    >>> first()
    Может быть 144 различных слов.

    """
    import itertools
    alphabet = "ABCDXYZ"
    s = 'XYZ'
    s1 = 'ABCD'
    ar = itertools.product(alphabet, repeat=4)
    arl = []
    for i in ar:
        arl.append(list(i))
    count = 0
    for e in arl:
        if e[0] in s and e[1] in s and e[2] in s1 and e[3] in s1:
            count += 1
    return print(f'Может быть {count} различных слов.')
first()
import doctest
doctest.testmod()