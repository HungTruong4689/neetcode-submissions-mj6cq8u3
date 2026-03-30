class StockSpanner:

    def __init__(self):
        #self.stack = []
        self.values = []
        #self.count = 0

    def next(self, price: int) -> int:
        count = 1
        stack = []
        
        while self.values and price >= self.values[-1]:
            count+=1
            last = self.values.pop()
            stack.append(last)
        while stack:
            val = stack.pop()
            self.values.append(val)
        self.values.append(price)
        return count



# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)