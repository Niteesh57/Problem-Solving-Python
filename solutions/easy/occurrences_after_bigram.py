class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        x = text.split(' ')
        ans = []
        for i in range(len(x) - 1):
            if x[i] == first and x[i + 1] == second:
                if i + 2 <= len(x) - 1:
                    ans.append(x[i + 2])
        return ans