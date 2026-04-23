class MinStack:

    def __init__(self):
        self.stack = []
        self.curr_min = float("infinity")
        self.mins = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.curr_min = min(self.curr_min, val)
        self.mins.append(self.curr_min)

    def pop(self) -> None:
        self.stack.pop()
        self.mins.pop()
        self.curr_min = self.mins[-1] if self.mins else float("infinity")

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.curr_min
