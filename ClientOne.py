from DateAndTimeInterface import DateAndTimeInterface
from datetime import date, datetime


class ClientOne(DateAndTimeInterface):
    def displayDate(self):
        today = date.today()
        time = datetime.now().time()
        print("client one's date: " + str(today) + " " + str(time))
