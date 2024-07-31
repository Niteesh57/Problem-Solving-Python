class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        val = []
        for i in range(left,right+1):
            print(i)
            v = list(str(i))
            if len(v) > 1:
                x = len(v)
                for j in v:
                    if j != '0' and i % int(j) == 0:
                        x -= 1
                if x == 0:
                    val.append(i)
            else:
                val.append(i)
        return val
        