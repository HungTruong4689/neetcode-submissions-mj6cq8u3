class MinStack:

    def __init__(self):
        self.data = []
        self.mV = []

    def push(self, val: int) -> None:
        self.data.append(val)
        if not self.mV or self.mV[-1]>=val:
            self.mV.append(val)

    def pop(self) -> None:
        val = self.data.pop()
        if self.data and val == self.mV[-1]:
            self.mV.pop()

    def top(self) -> int:
        return self.data[-1]

    def getMin(self) -> int:
        return self.mV[-1]
