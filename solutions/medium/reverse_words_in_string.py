class Solution:
    def reverseWords(self, s: str) -> str:
        x = ''
        l = [i for i in s.split(' ') if i != '']
        for i in range(len(l)-1,-1,-1):
            if i == 0:
                x += l[i]
            else:
                x += l[i] + ' '
        return x      