class MyCalendar:

    def __init__(self):
        self.arr = []

    def book(self, start: int, end: int) -> bool:
        if self.arr == []:
            self.arr.append([start,end])
            return True
        else:
            for i,j in self.arr:
                if not (end <= i or start >= j):
                    return False
            self.arr.append([start,end])
        return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)