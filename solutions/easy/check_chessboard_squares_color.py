class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        even = ["b","d","f","h"]
        odd = ["a","c","e","g"]
        if int(list(coordinate1)[1]) % 2 and int(list(coordinate2)[1]) % 2:
            if list(coordinate1)[0] in even and list(coordinate2)[0] in even:
                return True
            elif list(coordinate1)[0] in odd and list(coordinate2)[0] in odd:
                return True
            else:
                return False
        elif int(list(coordinate1)[1]) % 2 == 0 and int(list(coordinate2)[1]) % 2 == 0:
            if list(coordinate1)[0] in even and list(coordinate2)[0] in even:
                return True
            elif list(coordinate1)[0] in odd and list(coordinate2)[0] in odd:
                return True
            else:
                return False
        elif int(list(coordinate1)[1]) % 2 != 0 and int(list(coordinate2)[1]) % 2 == 0 or int(list(coordinate1)[1]) % 2 == 0 and int(list(coordinate2)[1]) % 2 != 0:
            if list(coordinate1)[0] in even and list(coordinate2)[0] in odd or list(coordinate1)[0] in odd and list(coordinate2)[0] in even:
                return True
            else:
                return False