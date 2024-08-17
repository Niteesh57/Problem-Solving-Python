class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        x1 = Counter(arr1)
        ans = []
        t1 = set(arr1)
        t2 = set(arr2)
        t3 = sorted(list(t1 ^ t2))
        for i in arr2:
            x = x1.get(i)
            ans = ans + [i]*x
        for i in t3:
            x = x1.get(i)
            ans = ans + [i]*x
        return ans