class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        val = []
        lowercase_letters = string.ascii_lowercase
        enc = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        x = dict(zip(lowercase_letters,enc))
        for i in words:
            temp = list(i)
            encode = ""
            for j in temp:
                encode += x[j]
            if encode not in val:
                val.append(encode)
            encode = ""
        return len(val)