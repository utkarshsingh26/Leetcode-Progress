class RandomizedSet:

    def __init__(self):
        self.sett = set()
        self.nums = []

    def insert(self, val: int) -> bool:
        if val in self.sett:
            return False
        else:
            self.sett.add(val)
            self.nums.append(val)
            return True

    def remove(self, val: int) -> bool:
        if val not in self.sett:
            return False
        else:
            self.sett.remove(val)
            self.nums.remove(val)
            return True

    def getRandom(self) -> int:
        length = len(self.nums)
        index = random.randint(0,length-1)
        return self.nums[index]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()