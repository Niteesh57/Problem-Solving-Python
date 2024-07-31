class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        x = list(s)
        for i in range(len(x)):
            if "".join(x) == goal:
                return True
            val = x[0]
            x = x[1:] + [val]
        return False