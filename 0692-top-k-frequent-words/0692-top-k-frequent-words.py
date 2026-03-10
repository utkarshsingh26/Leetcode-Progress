from collections import Counter
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        count = Counter(words)
        nums = []

        for key,val in count.items():
           nums.append((val, key))
        
        nums.sort(key=lambda x: (-x[0], x))
        answer = nums[:k]

        return [val for _,val in answer]