from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        
        nums = []
        count = Counter(s)
        t = ""
        
        for key,val in count.items():
            nums.append((val, key))
        
        nums.sort(key=lambda x:(-x[0],x))

        for val,key in nums:
            for i in range(val):
                t += "".join(key)
        
        return t