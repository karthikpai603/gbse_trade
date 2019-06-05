import abc


class StockService(abc.ABC):

    @abc.abstractmethod
    def calculate_dividend_yield(self, stock_symbol, price):
        """

        :type stock_symbol: string
        :type price: float
        """
        pass

    @abc.abstractmethod
    def calculate_p_e_ratio(self, stock_symbol, price):
        """

        :type stock_symbol: string
        :type price: float
        """
        pass

    @abc.abstractmethod
    def record_trade(self, stock_symbol, trade_data, stock=None):
        """
        :param stock:
        :type stock_symbol: string
        :type trade_data: Trade object
        """
        pass

    @abc.abstractmethod
    def calculate_volume_weighted_price(self, stock_symbol, stock=None):
        """
        :param stock:
        :type stock_symbol: string
        """
        pass

    @abc.abstractmethod
    def calculate_gbce_all_share_index(self):
        """

        """
        pass
