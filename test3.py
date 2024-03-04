from datetime import date

def date_differnce(date1, date2):
    return abs((date2 - date1).days)

date1 = date(2024, 3, 1)
date2 = date(2024, 1, 1)
print(date_differnce(date1, date2))