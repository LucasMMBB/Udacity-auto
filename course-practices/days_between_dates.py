# helper funtions
def isLeapYearMaoxu(year):
    return (year%4==0 and year%100!=0) or (year%400==0)

def daysInMonth(year, month):
    if month == 1 or month ==3 or month == 5 \
        or month == 7 or month == 8 or month == 10 \
            or month == 12:
                return 31
    if month != 2:
        return 30
    if isLeapYearMaoxu(year):
        return 29
    else:
        return 28

def isDayBefore(date1, date2):
    year1, month1, day1 = date1
    year2, month2, day2 = date2
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            if day1 < day2:
                return True
    return False




def nextDate(date):
    year, month, day = date
    if day < daysInMonth(year, month):
        return (year, month, day+1)
    else:
        if month < 12:
            return (year, month+1, 1)
        else:
            return (year+1, 1, 1)        

def days_between_dates(y1, m1, d1, y2, m2, d2):
    """
    Calculates the number of days between two dates.
    """
    
    # TODO - by the end of this lesson you will have
    #  completed this function. You do not need to complete
    #  it yet though! 
    count = 0
    date1 = (y1, m1, d1)
    date2 = (y2, m2, d2)
    assert not isDayBefore(date2, date1)
    while isDayBefore(date1, date2):
        date1 = nextDate(date1)
        count += 1
    return count

def test_days_between_dates():
    
    # test same day
    assert(days_between_dates(2017, 12, 30,
                              2017, 12, 30) == 0)
    # test adjacent days
    assert(days_between_dates(2017, 12, 30, 
                              2017, 12, 31) == 1)
    # test new year
    assert(days_between_dates(2017, 12, 30, 
                              2018, 1,  1)  == 2)
    # test full year difference
    assert(days_between_dates(2012, 6, 29,
                              2013, 6, 29)  == 365)
    
    print("Congratulations! Your days_between_dates")
    print("function is working correctly!")
    
test_days_between_dates()