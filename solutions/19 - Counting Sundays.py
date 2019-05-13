from commons import runtime

def resolve():
    year = 1900
    sundays = 0
    counted_months = 0
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days_passed = 0
    while year < 2001:
        #print(year, sundays, counted_months, days_passed)
        days_passed += months[counted_months]
        if counted_months == 1 and ((not str(year).endswith('00') and year % 4 == 0) or (str(year).endswith('00') and year % 400 == 0)):
            days_passed += 1
        if days_passed % 7 == 6:
            days_passed = 6
            if year >= 1901:
                sundays += 1
        counted_months = counted_months + 1 if counted_months < 11 else 0
        if counted_months == 0:
            year += 1
    print(sundays)

runtime(resolve)
