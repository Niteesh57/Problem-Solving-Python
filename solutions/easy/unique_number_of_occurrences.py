class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        x = dict(Counter(arr))
        arr_x = []
        for i in x.values():
            arr_x.append(i)
        for i in range(len(arr_x)):
            if arr_x[i] in arr_x[i+1:]:
                return False
        return True