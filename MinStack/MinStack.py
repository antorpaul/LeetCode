import math

class MinStack:
    def __init__(self):
        self.stack: list = []
        self.minTrack: list = []
        self.min: int

    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            self.min = val
            self.stack.append(val)
            self.minTrack.append(self.min)
            return
        
        if val >= self.min:
            self.stack.append(val)
            self.minTrack.append(self.min)
        else:
            self.min = val
            self.stack.append(val)
            self.minTrack.append(val)
            return

    def pop(self) -> None:
        self.stack.pop()
        self.minTrack.pop()

        # update the min value after pop
        if len(self.stack) > 0:
            self.min = self.minTrack[-1]
        else:
            self.min = None


    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minTrack[-1]

    def getStack(self) -> list[int]:
        return self.stack