class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(re.findall('[A-Z]',word)) == len(word) or len(re.findall('[a-z]',word)) == len(word):
            return True
        elif len(re.findall('[A-Z]',word[0]) + re.findall('[a-z]',word[1::])) == len(word):
            return True
        else:
            return False

        