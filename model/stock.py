import enum
from model.trade import Trade


class Stock(object):
    def __init__(self):
        """

        """
        self._stock_symbol = None
        self._stock_type = 1
        self._par_value = 0.0
        self._last_dividend = 0.0
        self._fixed_dividend = 0.0
        self._trade_list = []

    @property
    def stock_symbol(self):
        """

        :return:
        """
        return self._stock_symbol

    @stock_symbol.setter
    def stock_symbol(self, stock_symbol):
        """

        :param stock_symbol:
        """
        self._stock_symbol = stock_symbol

    @property
    def par_value(self):
        """

        :return:
        """
        return self._par_value

    @par_value.setter
    def par_value(self, par_value):
        """

        :param par_value:
        """
        if par_value < 0:
            raise ValueError('par_value of stock cannot be negative')
        else:
            self._par_value = par_value

    @property
    def fixed_dividend(self):
        """

        :return:
        """
        return self._fixed_dividend

    @fixed_dividend.setter
    def fixed_dividend(self, fixed_dividend):
        """

        :param fixed_dividend:
        """
        if fixed_dividend and fixed_dividend <= 0:
            raise ValueError('fixed_dividend of stock cannot be zero or negative')
        else:
            self._fixed_dividend = fixed_dividend

    @property
    def last_dividend(self):
        """

        :return:
        """
        return self._last_dividend

    @last_dividend.setter
    def last_dividend(self, last_dividend):
        """

        :param last_dividend:
        """
        self._last_dividend = last_dividend

    @property
    def stock_type(self):
        """

        :return:
        """
        return StockType(self._stock_type).name

    @stock_type.setter
    def stock_type(self, stock_type):
        """

        :param stock_type:
        """
        self._stock_type = stock_type

    @property
    def trade_list(self):
        return self._trade_list

    @trade_list.setter
    def trade_list(self, trade):
        """

        :param trade:
        """
        if isinstance(trade, Trade):
            self._trade_list.append(trade)
        else:
            raise TypeError('trade of stock should be of type Trade')


class StockType(enum.Enum):
    COMMON = 1
    PREFERRED = 2
