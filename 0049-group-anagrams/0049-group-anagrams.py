class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        graph = defaultdict(list)

        for s in strs:
            graph["".join(sorted(s))].append(s)
        
        result = []

        for key,val in graph.items():
            result.append(val)
        
        return result