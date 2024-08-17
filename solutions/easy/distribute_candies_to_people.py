class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        n = [0]*num_people
        count = 1
        while candies > 0:
            for i in range(num_people):
                if count > candies:
                    n[i] += candies
                    candies = 0
                    break
                n[i] += count
                candies -= count
                count += 1
        return n