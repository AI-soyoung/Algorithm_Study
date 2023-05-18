from collections import defaultdict
n, m, v = map(int, input().split())

graph = defaultdict(list)
for _ in range(m):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

# DFS
for n, e in graph.items():
    e = e.sort(reverse=True)

todo = [v]
visited = []

while todo:
    n = todo.pop()
    if n not in visited:
        todo.extend(graph[n])
        visited.append(n)
print(' '.join(map(str, visited)))

# BFS
for n, e in graph.items():
    e = e.sort()
todo = [v]
visited = [v]

while todo:
    n = todo.pop(0)
    for x in graph[n]:
        if x not in visited:
            visited.append(x)
            todo.append(x)
print(' '.join(map(str, visited)))  