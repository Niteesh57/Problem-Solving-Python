class Solution:
    def calPoints(self, operations: List[str]) -> int:
        x = []
        for i in operations:
            try:
                if int(i)/2:
                    x.append(int(i))
            except:
                if i == 'C':
                    if x != []:
                        x.pop()
                elif i == 'D':
                    if x != []:
                        data = 2 * (int(x[len(x) -1]))
                        x.append(data)
                else:
                    if len(x) >= 2:
                        data = int(x[len(x) -1]) + int(x[len(x) -2])
                        x.append(data)
        return sum(x)