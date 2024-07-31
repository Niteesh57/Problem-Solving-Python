class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        l = set()
        for i in emails:
            x = i.split('@')
            localhost = x[0]
            x1 = localhost.split('+')
            localhost = x1[0].replace('.', '')
            data = localhost + '@' + x[1]
            l.add(data)
        return len(l)