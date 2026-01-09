class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        graph = defaultdict(list)
        visited = set()

        def cycle(node1, node2):
            if node1 == node2:
                return True
            
            visited.add(node2)

            for neighbor in graph[node2]:
                if neighbor not in visited:
                    if cycle(node1, neighbor):
                        return True
            
            return False

        for u,v in edges:
            if u in graph or v in graph:
                visited.clear()
                if cycle(u,v):
                    return [u,v]
            graph[u].append(v)
            graph[v].append(u)