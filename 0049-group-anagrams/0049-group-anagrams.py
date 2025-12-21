class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        graph = defaultdict(list)
        result = []

        for s in strs:
            key = "".join(sorted(s))
            graph[key].append(s)
        
        for key, value in graph.items():
            result.append(value)
        
        return result
