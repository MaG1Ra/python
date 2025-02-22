def a():
    sites = {
        'Moscow': (550, 370),
        'London': (510, 510),
        'Paris': (480, 480),
    }
    distances = {}
    for city1 in sites:
        distances[city1] = {}
        for city2 in sites:
            x1, y1 = sites[city1]
            x2, y2 = sites[city2]
            distances[city1][city2] = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    return distances
result = a()
print(f'Первое задание.\n{result}')