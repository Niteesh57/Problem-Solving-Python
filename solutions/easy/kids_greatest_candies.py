class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        x = sorted(candies)[-1]
        for i in candies:
            yield (i+extraCandies) >= x