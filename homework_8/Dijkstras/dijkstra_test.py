from dijkstra import dijkstra, get_shortest_path

graph = {'A': {}}
dist, prev = dijkstra(graph, 'A')
assert dist['A'] == 0, "Тест 1: Расстояние до самой себя должно быть 0"
assert prev['A'] is None, "Тест 1: Предыдущая вершина для начальной должна быть None"

graph = {
    'A': {'B': 5},
    'B': {'A': 5}
}
dist, prev = dijkstra(graph, 'A')
assert dist['A'] == 0, "Тест 2: Расстояние до A должно быть 0"
assert dist['B'] == 5, "Тест 2: Расстояние до B должно быть 5"
assert get_shortest_path(prev, 'B') == ['A', 'B'], "Тест 2: Путь до B должен быть ['A', 'B']"

graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1, 'E': 3},
    'E': {'D': 3}
}
dist, prev = dijkstra(graph, 'A')
assert dist['D'] == 4, f"Тест 3: Расстояние до D должно быть 4, получено {dist['D']}"
assert get_shortest_path(prev, 'D') == ['A', 'B', 'C', 'D'], "Тест 3: Путь до D должен быть ['A', 'B', 'C', 'D']"

graph = {
    'A': {'B': 1},
    'B': {'C': 2},
    'C': {'A': 3, 'D': 1},
    'D': {}
}
dist, prev = dijkstra(graph, 'A')
assert dist['D'] == 4, f"Тест 4: Расстояние до D должно быть 4, получено {dist['D']}"
assert get_shortest_path(prev, 'D') == ['A', 'B', 'C', 'D'], "Тест 4: Путь до D должен быть ['A', 'B', 'C', 'D']"

graph = {
    'A': {'B': 1},
    'B': {'C': 2},
    'C': {},
    'D': {'E': 1},
    'E': {}
}
dist, _ = dijkstra(graph, 'A')
assert dist['D'] == float('infinity'), "Тест 5: Расстояние до недостижимой вершины D должно быть infinity"
assert dist['E'] == float('infinity'), "Тест 5: Расстояние до недостижимой вершины E должно быть infinity"

graph = {
    'A': {'B': 1},
    'B': {'C': -2},
    'C': {'D': 3},
    'D': {}
}
dist, prev = dijkstra(graph, 'A')
assert dist['D'] == 2, "Тест 6: Расстояние до D должно быть 2 (1 + (-2) + 3)"
assert get_shortest_path(prev, 'D') == ['A', 'B', 'C', 'D'], "Тест 6: Путь до D должен быть ['A', 'B', 'C', 'D']"

graph = {
    'A': {},
    'B': {},
    'C': {},
    'D': {}
}
dist, _ = dijkstra(graph, 'A')
assert dist['A'] == 0, "Тест 7: Расстояние до A должно быть 0"
assert dist['B'] == float('infinity'), "Тест 7: Расстояние до B должно быть infinity"
assert dist['C'] == float('infinity'), "Тест 7: Расстояние до C должно быть infinity"
assert dist['D'] == float('infinity'), "Тест 7: Расстояние до D должно быть infinity"

graph = {
    'A': {'B': 1, 'C': 2, 'D': 3},
    'B': {'A': 1, 'C': 4, 'D': 5},
    'C': {'A': 2, 'B': 4, 'D': 6},
    'D': {'A': 3, 'B': 5, 'C': 6}
}
dist, prev = dijkstra(graph, 'A')
assert dist['D'] == 3, "Тест 8: Расстояние до D должно быть 3"
assert get_shortest_path(prev, 'D') == ['A', 'D'], "Тест 8: Путь до D должен быть ['A', 'D']"

graph = {
    'A': {'B': 0, 'C': 2},
    'B': {'C': 0, 'D': 1},
    'C': {'D': 3},
    'D': {}
}
dist, prev = dijkstra(graph, 'A')
assert dist['D'] == 1, f"Тест 9: Расстояние до D должно быть 1, получено {dist['D']}"
assert get_shortest_path(prev, 'D') == ['A', 'B', 'D'], "Тест 9: Путь до D должен быть ['A', 'B', 'D']"

graph = {
    '1': {'2': 7, '3': 9, '6': 14},
    '2': {'1': 7, '3': 10, '4': 15},
    '3': {'1': 9, '2': 10, '4': 11, '6': 2},
    '4': {'2': 15, '3': 11, '5': 6},
    '5': {'4': 6, '6': 9},
    '6': {'1': 14, '3': 2, '5': 9}
}
dist, prev = dijkstra(graph, '1')
assert dist['1'] == 0
assert dist['2'] == 7
assert dist['3'] == 9
assert dist['4'] == 20
assert dist['5'] == 20
assert dist['6'] == 11
assert get_shortest_path(prev, '5') == ['1', '3', '6', '5']
