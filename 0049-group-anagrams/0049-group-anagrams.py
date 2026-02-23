class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        graph = defaultdict(list)
        result = []

        for s in strs:
            sorted_s = "".join(sorted(s))
            graph[sorted_s].append(s)
        
        for key,value in graph.items():
            result.append(value)
        
        return result
        
        