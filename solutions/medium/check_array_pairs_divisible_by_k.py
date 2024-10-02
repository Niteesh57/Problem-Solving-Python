class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        remainder_counts = Counter([x % k for x in arr])
        for remainder in remainder_counts:
            if remainder == 0:
                if remainder_counts[remainder] % 2 != 0:
                    return False
            elif remainder == k // 2 and k % 2 == 0:
                if remainder_counts[remainder] % 2 != 0:
                    return False
            else:
                if remainder_counts[remainder] != remainder_counts[k - remainder]:
                    return False
        return True