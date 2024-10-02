class Solution:
    def reformatDate(self, date: str) -> str:
        x = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
        data = date.split(' ')
        x1 = data[0][:-2] if len(str(data[0][:-2])) > 1 else '0' + str(data[0][:-2])
        x2 = x.index(data[1])+1 if len(str(x.index(data[1])+1)) > 1 else '0' + str(x.index(data[1])+1)
        x3 = data[2]
        return "{year}-{month}-{day}".format(year=x3,month=x2,day=x1)     