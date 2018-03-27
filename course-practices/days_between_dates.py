# helper funtions
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


def isLeapYear(year):
    return (year%4==0 and year%100!=0) or (year%400==0)

def nextDate(date):
    year, month, day = date
    longMonth = {1,3,5,7,8,10,12}
    if day < 28:
        day += 1
    else:
        if month == 2:
            if isLeapYear(year):
                if day < 28:
                    day += 1
                else:
                    day = 1
            else:
                if day < 29:
                    day += 1
                else:
                    day = 1
        else:
            if day < 30:
                day +=1
            elif day == 30:
                if month in longMonth:
                    day += 1
                else:
                    day = 1
            elif day == 31:
                day = 1

    if day == 1:
        if month < 12:
            month += 1
        else:
            month = 1
            year += 1
    return (year, month, day)
        

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
    print count
    assert not isDayBefore(date2, date1)
    while isDayBefore(date1, date2):
        print date1
        print date2
        print "-------------------"
        date1 = nextDate(date1)
        count += 1
    print count
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