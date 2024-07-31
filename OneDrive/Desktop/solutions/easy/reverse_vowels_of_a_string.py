class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        l = 0
        r = len(s)-1
        x1 = ['a','e','i','o','u']
        x,y = False,False
        while l < r:
            if s[l].lower() in x1:
                x = True
            if s[r].lower() in x1:
                y = True
            print(l,r)
            if x == True and y == True:
                temp = s[l]
                s[l] = s[r]
                s[r] = temp
                l += 1
                r -= 1
                x,y = False,False
            elif x == False and y == True:
                l += 1
            elif x == True and y == False:
                r -= 1
            else:
                l += 1
                r -= 1
        return ''.join(s)