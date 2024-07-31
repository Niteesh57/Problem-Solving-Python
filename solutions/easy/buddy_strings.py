class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        elif s == goal and len(set(s)) < len(goal):
            return True
        else:
            val = []
            for i in range(len(goal)):
                if s[i] != goal[i]:
                    val.append(i)
            if len(val) > 2 or val == [] or len(val) == 1:
                return False
            else:
                x = list(s)
                temp = x[val[0]]
                temp2 = x[val[1]]
                x[val[1]] = temp
                x[val[0]] = temp2
                if "".join(x) == goal:
                    return True
        return False