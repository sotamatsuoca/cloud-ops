class Fancy:

    def __init__(self):
        self.data = [] 
        self.add = 0
        self.mult = 1
        self.MOD = 10**9 + 7

    def append(self, val: int) -> None:
        inv_mult = pow(self.mult, -1, self.MOD)
        normalized_val = (val - self.add) * inv_mult % self.MOD
        self.data.append(normalized_val)

    def addAll(self, inc: int) -> None:
        self.add = (self.add + inc) % self.MOD

    def multAll(self, m: int) -> None:
        self.mult = (self.mult * m) % self.MOD
        self.add = (self.add * m) % self.MOD

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.data):
            return -1
        normalized_val = self.data[idx]
        actual_val = (normalized_val * self.mult + self.add) % self.MOD
        return actual_val
