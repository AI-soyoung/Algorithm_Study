from collections import deque, defaultdict

def dfs(graph):
    answer = []
    q = ["ICN"]
    
    while q:
        now = q[-1]
        if now not in graph or len(graph[now])==0:
            answer.append(q.pop())
        else:
            q.append(graph[now].pop())
    return answer[::-1]
    

def solution(tickets):
    graph = defaultdict(list)
    for start, end in tickets:
        graph[start].append(end)
    
    for k in graph.keys():
        graph[k].sort(reverse=True)
    
    return dfs(graph)