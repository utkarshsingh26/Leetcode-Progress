class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        graph = defaultdict(list)
        result = []

        for s in strs:
            graph["".join(sorted(s))].append(s)
        
        for key,arr in graph.items():
            result.append(arr)
        
        return result