class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = defaultdict(list)

        for u,v in prerequisites:
            graph[v].append(u)
        
        UNVISITED = 0
        VISITNG = 1
        VISITED = 2

        status = [UNVISITED] * numCourses
        print(status)

        def cycle(node):
            if status[node] == VISITNG:
                return True
            elif status[node] == VISITED:
                return False
            else:
                status[node] = VISITNG

                for neighbor in graph[node]:
                    if cycle(neighbor):
                        return True
                status[node] = VISITED
                return False
        
        for i in range(numCourses):
            if cycle(i):
                return False
        
        return True