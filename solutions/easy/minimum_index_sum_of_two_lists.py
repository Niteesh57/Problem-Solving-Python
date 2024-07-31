class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        x = []
        data = []
        val = None
        for i in range(0,len(list1)):
            for j in range(0,len(list2)):
                if list1[i] == list2[j]:
                    if val == None:
                        x.append([i,j])
                        val = i + j
                        break
                    else:
                        if val != i + j and val > i + j:
                            x = []
                        if val >= (i+j):
                            x.append([i,j])
                            val = i + j
                            break
        for i in x[::-1]:
            data.append(list1[i[0]])
        return data