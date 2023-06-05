from collections import defaultdict
from collections import deque

n, m = map(int, input().split())
graph = defaultdict(list)
for _ in range(m):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)
    
def bfs(graph, user):
    num = [0] * (n+1)
    visited = set()
    visited.add(user)
    todo = deque()
    todo.append(user)

    while todo:
        target = todo.popleft()
        for g in graph[target]:
            if g not in visited:
                num[g] = num[target] + 1
                visited.add(g)
                todo.append(g)
    return sum(num)

result = []
for user in range(1, n+1):
    result.append(bfs(graph, user))

print(result.index(min(result))+1)