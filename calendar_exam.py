class Calendar:

    def __init__(self):
        self._year = 0
        self._month = 0
        self._day = 0

    def set_date(self, year, month, day):
        self._year = year
        self._month = month
        self._day = day

    def get_year(self):
        return self._year

    def get_month(self):
        return self._month

    def get_day(self):
        return self._day

    def get_day_of_week(self):
        total_days = 0
        days_of_month = [0,31,28,31,30,31,30,31,31,30,31,30,31]
        day_of_week = ["일요일","월요일","화요일","수요일","목요일","금요일","토요일"]

        for year in range(1, self._year):
            if year % 4 == 0:
                if year % 100 == 0:
                    if year % 400 == 0:
                        total_days = total_days + 366

                    else:
                        total_days = total_days + 365
                else:
                    total_days = total_days + 366
            else:
                total_days = total_days +365

        for month in range(1, self._month):
            total_days = total_days + days_of_month[month]

        if self._month >= 3:
            if self._year % 4 == 0:
                if self._year % 100 == 0:
                    if self._year % 400 ==0:
                        total_days = total_days +1
                    else:
                        pass
                else:
                    total_days = total_days +1
            else:
                pass


        total_days = total_days + self._day

        return day_of_week[total_days % 7]


if __name__ == "__main__":
    calendar = Calendar()
    calendar.set_date(2021,5,8)
    print("년도:", calendar.get_year())
    print("월:", calendar.get_month())
    print("일:", calendar.get_day())
    print(calendar.get_day_of_week())
