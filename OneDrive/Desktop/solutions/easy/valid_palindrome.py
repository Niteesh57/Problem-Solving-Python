import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        string = ""
        for i in s:
            if re.match("[a-zA-Z]+", i) or re.search(r'\d', i):
                string += i
        length = len(string) - 1
        len_str = 0
        for i in range(len(string)):
            if string[len_str] == string[length]:
                length -= 1
                len_str += 1
                pass
            else:
                return False
        return True
