from dag import detect_cycle_and_toposort

graph1 = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['D'],
    'D': []
}
has_cycle1, result1 = detect_cycle_and_toposort(graph1)
assert has_cycle1 is False
assert set(result1) == {'A', 'B', 'C', 'D'}
assert result1.index('A') < result1.index('B') and result1.index('A') < result1.index('C')
assert result1.index('B') < result1.index('D') and result1.index('C') < result1.index('D')

graph2 = {
    'A': ['B'],
    'B': ['C'],
    'C': ['A'],
    'D': ['A']
}
has_cycle2, result2 = detect_cycle_and_toposort(graph2)
assert has_cycle2 is True
assert set(result2[:-1]) == {'A', 'B', 'C'}
assert result2[0] == result2[-1] 

graph3 = {
    'A': ['B'],
    'B': ['C', 'D'],
    'C': ['A'],
    'D': ['E'],
    'E': ['B']
}
has_cycle3, result3 = detect_cycle_and_toposort(graph3)
assert has_cycle3 is True

possible_cycles = [
    ['A', 'B', 'C', 'A'],
    ['B', 'C', 'A', 'B'],
    ['C', 'A', 'B', 'C'],
    ['B', 'D', 'E', 'B'],
    ['D', 'E', 'B', 'D'],
    ['E', 'B', 'D', 'E']
]
found = False
for cycle in possible_cycles:
    if result3 == cycle:
        found = True
        break
assert found, f"Не найден ожидаемый цикл, получен: {result3}"

graph4 = {}
has_cycle4, result4 = detect_cycle_and_toposort(graph4)
assert has_cycle4 is False
assert result4 == []

graph5 = {'A': []}
has_cycle5, result5 = detect_cycle_and_toposort(graph5)
assert has_cycle5 is False
assert result5 == ['A']

graph6 = {'A': ['A']}
has_cycle6, result6 = detect_cycle_and_toposort(graph6)
assert has_cycle6 is True
assert result6 == ['A', 'A']

graph7 = {
    'A': ['B'],
    'B': [],
    'C': ['D'],
    'D': []
}
has_cycle7, result7 = detect_cycle_and_toposort(graph7)
assert has_cycle7 is False
assert set(result7) == {'A', 'B', 'C', 'D'}
assert result7.index('A') < result7.index('B')
assert result7.index('C') < result7.index('D')

graph8 = {
    'A': ['B'],
    'B': ['A'],
    'C': ['D'],
    'D': []
}
has_cycle8, result8 = detect_cycle_and_toposort(graph8)
assert has_cycle8 is True
assert set(result8[:-1]) == {'A', 'B'}
assert result8[0] == result8[-1]

graph9 = {
    'A': ['C', 'D'],
    'B': ['D'],
    'C': ['E'],
    'D': ['E'],
    'E': []
}
has_cycle9, result9 = detect_cycle_and_toposort(graph9)
assert has_cycle9 is False
assert set(result9) == {'A', 'B', 'C', 'D', 'E'}
assert result9.index('A') < result9.index('C') and result9.index('A') < result9.index('D')
assert result9.index('B') < result9.index('D')
assert result9.index('C') < result9.index('E') and result9.index('D') < result9.index('E')

graph10 = {
    '1': ['2', '3', '4'],
    '2': ['5', '6'],
    '3': ['6', '7'],
    '4': ['7', '8'],
    '5': ['9'],
    '6': ['9', '10'],
    '7': ['10', '11'],
    '8': ['11'],
    '9': ['12'],
    '10': ['12'],
    '11': ['12'],
    '12': []
}
has_cycle10, result10 = detect_cycle_and_toposort(graph10)
assert has_cycle10 is False
assert len(result10) == 12
assert result10.index('1') < result10.index('2') and result10.index('1') < result10.index('3')
assert result10.index('2') < result10.index('5') and result10.index('5') < result10.index('9')
assert result10.index('9') < result10.index('12')