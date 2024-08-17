class Solution:
    def dayOfYear(self, date: str) -> int:
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        year, month, day = map(int, date.split('-'))
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            days_in_month[1] = 29
        x = sum(days_in_month[:month - 1]) + day
        return x
        