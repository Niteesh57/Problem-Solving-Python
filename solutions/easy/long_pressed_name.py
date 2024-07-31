class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        x = 0
        y = 0
        while y < len(typed) and x < len(name):
                if name[x] == typed[y]:
                    x += 1
                    y += 1
                elif y > 0 and typed[y] == typed[y-1]:
                    y += 1
                else:
                    return False
        while y != len(typed):
            if typed[y] == typed[y-1]:
                y += 1
            else:
                return False
        return x == len(name) and y == len(typed)