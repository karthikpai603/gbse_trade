import enum
import datetime


class Trade(object):
    def __init__(self):
        """

        """
        self._price = 0
        self._indicator = 1
        self._quantity = 1
        self._timestamp = None

    @property
    def price(self):
        """

        :return:
        """
        return self._price

    @price.setter
    def price(self, price):
        """

        :param price:
        """
        if price < 0:
            raise ValueError('Price of trade cannot be negative')
        else:
            self._price = price

    @property
    def timestamp(self):
        """

        :return:
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """

        :param timestamp:
        """
        if timestamp > datetime.datetime.now():
            raise ValueError('Timestamp cannot be a future time')
        self._timestamp = timestamp

    @property
    def quantity(self):
        """

        :return:
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """

        :param quantity:
        """
        if quantity <= 0:
            raise ValueError('Quantity of trade cannot be zero or negative')
        else:
            self._quantity = quantity

    @property
    def indicator(self):
        """

        :return:
        """
        return BuySellIndicator(self._indicator).name

    @indicator.setter
    def indicator(self, indicator):
        """

        :param indicator:
        """
        self._indicator = indicator


class BuySellIndicator(enum.Enum):
    BUY = 1
    SELL = 2
