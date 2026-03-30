class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.arr = []

    def next(self, val: int) -> float:
        
        self.arr.append(val)
        print(self.arr)
        if len(self.arr) == 0:
            return 0
        if len(self.arr) < self.size:
            
            return sum(self.arr)/len(self.arr)
        new_arr = self.arr[len(self.arr) - self.size:]
        return sum(new_arr)/self.size


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
