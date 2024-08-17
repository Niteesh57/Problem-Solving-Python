class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        p = 0
        if sum(arr) % 3 == 0:
            sums = 0
            x = sum(arr) // 3
            for i in arr:
                sums += i
                if sums == x:
                    p += 1
                    sums = 0
        else:
            return False
        return p >= 3