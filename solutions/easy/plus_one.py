class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        L = []
        y = ""
        for i in digits:
            y += str(i)
        y = str(int(y)+1)
        if len(y) == 1:
            L.append(int(y))
            return L 
        for i in y:
            L.append(int(i))
        return L
        