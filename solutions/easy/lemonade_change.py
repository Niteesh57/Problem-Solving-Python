class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        x = []
        for i in bills:
            if i == 5:
                x.append(5)
            elif i == 10:
                if 5 in x:
                    x.remove(5)
                    x.append(10)
                else:
                    return False
            elif i == 20:
                val = Counter(x)
                t = val.get(5)
                t1 = val.get(10)
                if t == None:
                    return False
                if t1 == None:
                    if t >= 3:
                        for i in range(3):
                            x.remove(5)
                        x.append(20)
                    else:
                        return False
                else:
                    x.remove(5)
                    x.remove(10)
                    x.append(20)
        return True