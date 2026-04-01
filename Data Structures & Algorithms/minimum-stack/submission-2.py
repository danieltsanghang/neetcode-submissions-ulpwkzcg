class MinStack:

    def __init__(self):

        self.arr = []
        self.m = []

    def push(self, val: int) -> None:
        if not self.m:
            self.m.append(val)
        else:
            self.m.append(min(self.m[-1], val))
        self.arr.append(val)

    def pop(self) -> None:
        self.arr.pop()
        self.m.pop()
        # maintain 2 stacks, at any index i, m[i] is the min 
        # of arr[i] so we can pop them together

    def top(self) -> int:
        return self.arr[-1]

    def getMin(self) -> int:
        print(self.m)
        return self.m[-1]
        