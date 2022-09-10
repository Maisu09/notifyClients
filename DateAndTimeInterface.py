from abc import ABCMeta, abstractstaticmethod
from datetime import date


class DateAndTimeInterface(metaclass=ABCMeta):

    @abstractstaticmethod
    def displayDate():
        pass
