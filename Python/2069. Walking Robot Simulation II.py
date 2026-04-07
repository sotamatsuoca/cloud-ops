class Robot:
    def __init__(self, width: int, height: int):
        self.w = width
        self.h = height
        self.total_steps = 0
        self.perimeter = 2 * (width + height - 2)
        self.directions = ["East", "North", "West", "South"]

    def step(self, num: int) -> None:
        self.total_steps += num

    def getPos(self) -> list[int]:
        curr = self.total_steps % self.perimeter
        if 0 <= curr < self.w:
            return [curr, 0]
        elif self.w <= curr < self.w + self.h - 1:
            return [self.w - 1, curr - (self.w - 1)]
        elif self.w + self.h - 1 <= curr < 2 * self.w + self.h - 2:
            return [self.w - 1 - (curr - (self.w + self.h - 2)), self.h - 1]
        else:
            return [0, self.h - 1 - (curr - (2 * self.w + self.h - 3))]

    def getDir(self) -> str:
        if self.total_steps == 0: return "East"
        curr = self.total_steps % self.perimeter
        if curr == 0: return "South"
        
        if 1 <= curr < self.w: return "East"
        if self.w <= curr < self.w + self.h - 1: return "North"
        if self.w + self.h - 1 <= curr < 2 * self.w + self.h - 2: return "West"
        return "South"