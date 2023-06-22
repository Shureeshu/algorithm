def solution(tickets):
    answer = []

    graph = dict()
    for a, b in tickets:
        graph[a] = graph.get(a, [])
        graph[a].append(b)
    
    for airport_list in graph.values():
        airport_list.sort(reverse=True)

    
    visited = []
    def dfs(a):
        stack = []
        for i, b in enumerate(graph.get(a, [])):
            if [a, b, i] not in visited:
                stack.append([a, b, i])
        while stack:
            a, b, i = stack.pop()
            visited.append([a, b, i])
            dfs(b)
            if len(visited) == len(tickets):
                return
            else:
                visited.pop()

    dfs("ICN")
                
    answer = [v[0] for v in visited] + [visited[-1][1]]
    return answer
