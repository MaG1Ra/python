def third():
    """
    
    >>> third()
    [40000, 41472]
    
    """
    result = []
    for num in range(40000, 50000):
        nechet = [d for d in range(1, num + 1, 2) if num % d == 0]
    
        if len(nechet) == 5:
            result.append(num)
    return print(result)
third()
import doctest
doctest.testmod()