def invalid():
    print("Invalid date")

def check_validity(year,month,day):
    if (month >= 1) and (month <= 12):
        if year % 4 != 0:
            if (day >= 1) and (day <= 28):
                return 1
        if year % 4 == 0:
            if (day >= 1) and (day <= 29):
                return 1

        if (day >= 1) and (day <= 30):
            if month != 2:
                return 1
            else:
                invalid()
                return 0

        elif (day >= 1) and (day <= 31):
            if (month == 1) or (month == 3) or (month == 5) or (month == 7) or (
                    month == 8) or (month == 10) or (month == 12):
                return 1
            else:
                invalid()
                return 0

        else:
            invalid()
            return 0

    else:
        invalid()
        return 0


def calc_no_days(year,month,day):
    n=day
    if month == 1:
        return n

    elif month == 2:
        return n+31

    else:
        if month == 3:
            n = n + 31 + 28

        elif month == 4:
            n = n + 31 + 28 + 31

        elif month == 5:
            n = n + 31 + 28 + 31 + 30

        elif month == 6:
            n = n + 31 + 28 + 31 + 30 + 31

        elif month == 7:
            n = n + 31 + 28 + 31 + 30 + 31 + 30

        elif month == 8:
            n = n + 31 + 28 + 31 + 30 + 31 + 30 + 31

        elif month == 9:
            n = n + 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31

        elif month == 10:
            n = n + 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30

        elif month == 11:
            n = n + 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31

        elif month == 12:
            n = n + 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30

    if year % 4 == 0:
        return n+1
    else:
        return n

class DaysCalc ():
    def __init__(self, init_date, final_date):
        self.init_date={}
        self.final_date={}
        self.init_date = init_date
        self.final_date = final_date
        #print(self.init_date)
        #print(self.final_date)
        #print("Test 1 complete")

        #my input would be like 0324,0606

    def swap_date(self):
        temp = {}
        temp = self.init_date
        self.init_date = self.final_date
        self.final_date = temp

        #print(self.init_date, self.final_date)
        #print("Test 2 completed")

    def calc_days(self):
        iyear = int(self.init_date['year'])
        imonth=int(self.init_date['month'])
        iday=int(self.init_date['day'])
        fyear = int(self.final_date['year'])
        fmonth=int(self.final_date['month'])
        fday=int(self.final_date['day'])

        if iyear != fyear:
            if iyear > fyear:
                self.swap_date()

        else:
            if imonth > fmonth:
                self.swap_date()

            if iday > fday:
                self.swap_date()

        iyear = int(self.init_date['year'])
        imonth = int(self.init_date['month'])
        iday = int(self.init_date['day'])
        fyear = int(self.final_date['year'])
        fmonth = int(self.final_date['month'])
        fday = int(self.final_date['day'])

        #print(iday,imonth,iyear)
        #print(fday,fmonth,fyear)
        #print('Test 3 completed')

        check1=check_validity(iyear,imonth,iday)
        check2=check_validity(fyear,fmonth,fday)

        #print(check1,check2)
        #print('Test 4 completed')
        if (check1 == 1) and (check2 == 1):
           # print('Test *')
            d1 = calc_no_days(iyear, imonth, iday)
            if iyear == fyear:
                d2 = calc_no_days(fyear,fmonth,fday)
                #print(d1,d2)
                #print('Test 5a completed')

            else:
                #print('Test **')
                year_diff = fyear - iyear
                y1=calc_no_days(iyear,12,31)
                n1=y1-d1
                n = (year_diff-1)*365+n1
                while (iyear<fyear):
                    #print('Test ***')
                    if iyear % 4 == 0:
                        n=n
                    iyear += 1
                y2=calc_no_days(fyear,fmonth,fday)
                d2=n+y2
                #print(d1,d2)
                #print('Test 5b completed')
            return str(d2-d1)

