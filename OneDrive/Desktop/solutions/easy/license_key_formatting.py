class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        data = ""
        value = k
        pre = 0
        x = s.replace("-","").upper()[::-1]
        for i in range(value,len(x)+value,value):
            data += x[pre:i]
            data += '-'
            pre = i
        return data[:len(data)-1][::-1]