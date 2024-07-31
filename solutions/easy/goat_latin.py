class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        sen = ""
        n = sentence.split(" ")
        val = 'a'
        vowel = ['a','e','i','o','u']
        for i in range(len(n)):
            if n[i][0] in "".join(vowel) or n[i][0] in "".join(vowel).upper():
                n[i] = n[i] + "ma" + (val * (i + 1))
            else:
                n[i] = n[i][1::] + n[i][0] + "ma" + (val * (i + 1))
        return " ".join(n)
        