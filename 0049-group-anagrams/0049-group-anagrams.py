class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        result = []
        graph = defaultdict(list)

        for s in strs:
            graph["".join(sorted(s))].append(s)
        
        for key,val in graph.items():
            result.append(val)
        
        return result