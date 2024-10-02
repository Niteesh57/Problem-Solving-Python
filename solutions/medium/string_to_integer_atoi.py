class Solution:
    def myAtoi(self, s: str) -> int:
        integer = ""
        operation = ""
        integer_bool = False
        h = 2**31 - 1
        for i in s:
            if i.isspace() and integer_bool == False:
                pass
            elif i in ['-','+'] and integer_bool == False and operation == "":
                operation = i
                integer_bool = True
            elif i.isalpha():
                break
            elif i.isnumeric():
                integer_bool = True
                integer += i
            else:
                break
        if len(integer) == 0: return 0
        if int(integer) > h:
            if int(integer) > h:
                return int(operation + str(h))-1 if operation == '-' else int(operation + str(h))
        return int(operation + integer)
