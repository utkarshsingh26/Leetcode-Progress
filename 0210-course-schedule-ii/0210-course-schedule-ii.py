class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        graph = defaultdict(list)
        result = []

        for u,v in prerequisites:
            graph[v].append(u)
        
        UNVISITED = 0
        VISITING = 1
        VISITED = 2

        status = [UNVISITED] * numCourses

        def cycle(node):
            if status[node] == VISITED:
                return False
            elif status[node] == VISITING:
                return True
            else:
                status[node] = VISITING
                for neighbor in graph[node]:
                    if cycle(neighbor):
                        return True
                status[node] = VISITED
                result.append(node)
                return False

        for i in range(numCourses):
            if cycle(i):
                return []

        return result[::-1] 