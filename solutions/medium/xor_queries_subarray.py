class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        l = []
        x = [0]
        for i in range(0,len(arr)):
            x.append(x[-1]^arr[i])
        for i,j in queries:
            l.append(x[j+1]^x[i])
        return l
            

                

        