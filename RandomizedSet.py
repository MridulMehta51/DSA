class RandomizedSet:

    def __init__(self):
        self.list=[]
    def insert(self, val: int) -> bool:
        if val in self.list:
            return False
        self.list.append(val)
        return True
    def remove(self, val: int) -> bool:
        if val not in self.list:
            return False 
        self.list.remove(val)
        return True
    def getRandom(self) -> int:
        return random.choice(self.list)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
