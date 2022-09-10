from DateAndTimeInterface import DateAndTimeInterface
from datetime import date, datetime


class ClientTwo(DateAndTimeInterface):
    def displayDate(self):
        today = date.today()
        time = datetime.now().time()
        print("client two date: " + str(today)+ ' ' + str(time))