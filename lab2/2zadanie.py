def second():
    """
    
    >>> second()
    Кол-во двоек: 3
    
    """
    z = 9**8 + 3**5 - 3**2
    count = 0
    while z > 0:
        v = z % 3
        if v == 2:
            count += 1
        z = z // 3
    return print(f'Кол-во двоек: {count}')
second()
import doctest
doctest.testmod()