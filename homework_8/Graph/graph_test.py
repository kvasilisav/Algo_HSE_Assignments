from graph import find_connected_components

assert find_connected_components({}) == []

assert find_connected_components({1: [1]}) == [{1}]

graph = {
    1: [],
    2: [],
    3: [],
    4: []
}
result = find_connected_components(graph)
assert len(result) == 4
assert {1} in result
assert {2} in result
assert {3} in result
assert {4} in result

graph = {
    1: [2, 3, 4],
    2: [1, 3, 4],
    3: [1, 2, 4],
    4: [1, 2, 3]
}
assert find_connected_components(graph) == [{1, 2, 3, 4}]

graph = {
    1: [2, 3],
    2: [1, 3],
    3: [1, 2],
    4: [5],
    5: [4],
    6: []
}
result = find_connected_components(graph)
assert len(result) == 3
assert {1, 2, 3} in result
assert {4, 5} in result
assert {6} in result
graph = {
    1: [2],
    2: [1],
    3: [],
    4: [5, 6],
    5: [4, 6],
    6: [4, 5],
    7: []
}
result = find_connected_components(graph)
assert len(result) == 4
assert {1, 2} in result
assert {3} in result
assert {4, 5, 6} in result
assert {7} in result

graph = {
    -1: [0, 1],
    0: [-1, 1],
    1: [-1, 0],
    -2: [-3],
    -3: [-2]
}
result = find_connected_components(graph)
assert len(result) == 2
assert {-1, 0, 1} in result
assert {-2, -3} in result

graph = {}
for i in range(1, 4):
    graph[i] = [(i+1) % 4 or 4, (i+2) % 4 or 4] if i < 4 else [1, 2]

for i in range(5, 8):
    graph[i] = [(i+1) % 8 or 8, (i+2) % 8 or 8] if i < 8 else [5, 6]

for i in range(9, 12):
    graph[i] = [(i+1) % 12 or 12, (i+2) % 12 or 12] if i < 12 else [9, 10]

graph[13] = []
graph[14] = []
graph[15] = []

result = find_connected_components(graph)
assert len(result) == 6 
assert {1, 2, 3, 4} in result
assert {5, 6, 7, 8} in result
assert {9, 10, 11, 12} in result
assert {13} in result
assert {14} in result
assert {15} in result
