def bfs(graph, node, queue, visited, level):
    visited.append(node)
    queue.append(node)
    
    level[node] = 0

    while queue:
        parent = queue.pop(0)
        print(parent, end=" ")

        for child in graph[parent]:
            if child not in visited:
                visited.append(child)
                queue.append(child)
                level[child] = level[parent] + 1
        

if __name__ == '__main__':
    queue = []
    visited = []
    level = {}
    graph = {
        'A' : ['B', 'C'],
        'B' : ['D', 'E'],
        'C' : ['F'],
        'D' : [],
        'E' : ['F'],
        'F' : []
    }

bfs(graph, 'A', queue, visited, level)
print()
print(level)