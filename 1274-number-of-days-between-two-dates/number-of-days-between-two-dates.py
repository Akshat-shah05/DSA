class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        year1, month1, day1 = map(int, date1.split("-"))
        year2, month2, day2 = map(int, date2.split("-"))
        return abs(self.from1900ToDate(year1, month1, day1) - self.from1900ToDate(year2, month2, day2))
    
    def from1900ToDate(self, year, month, day):
        # Days in months (non-leap)
        month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        # Count full years
        days = 0
        for y in range(1900, year):
            days += 366 if self.isLeap(y) else 365
        
        # Count full months in current year
        for m in range(1, month):
            if m == 2 and self.isLeap(year):
                days += 29
            else:
                days += month_days[m - 1]
        
        # Add days
        days += day
        return days

    def isLeap(self, year):
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
