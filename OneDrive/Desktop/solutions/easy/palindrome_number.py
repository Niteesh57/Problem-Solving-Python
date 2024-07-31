class Solution:
    def isPalindrome(self, x: int) -> bool:
        a = str(x)
        data = a[::-1]
        if str(x) == data:
            return True
        else:
            return False
