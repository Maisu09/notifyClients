from DateAndTimeInterface import DateAndTimeInterface

class TimeServer():

    def __init__(self, subscriber:list):
        self.__subscribers = subscriber

    def notifySubscribers(self):
        subscriber : DateAndTimeInterface
        for subscriber in self.__subscribers:
            subscriber.displayDate()

    


        