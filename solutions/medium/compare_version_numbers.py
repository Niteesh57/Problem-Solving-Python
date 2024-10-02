class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        x1: List[str] = version1.split('.')
        x2: List[str] = version2.split('.')
        m = max(len(x1),len(x2))
        for i in range(m):
            x = x1[i] if i < len(x1) else '0'
            y = x2[i] if i < len(x2) else '0'
            if int(x) > int(y):
                return 1
            elif int(x) < int(y):
                return -1
        return 0