class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        x = score.copy()
        score.sort(reverse=True)
        n = ["Gold Medal","Silver Medal","Bronze Medal"]
        val = 0
        for i in range(len(score)):
            ind = x.index(score[i])
            try:
                x[ind] = n[val]
            except:
                dep = val + 1
                x[ind] = str(dep)
            val += 1
        return x
        