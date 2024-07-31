class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        x = list(jewels)
        y = Counter(stones)
        l = 0
        for i in x:
            if i in y:
                l += y.get(i)
        return l