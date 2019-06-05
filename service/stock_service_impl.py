from service.stock_service import StockService
from util.stock_util import *
from helper.stock_service_helper import StockServiceHelper
from model.trade import Trade
import logging

logger = logging.getLogger('stock_service_impl')
logger.setLevel(logging.INFO)


class StockServiceImpl(StockService):

    def calculate_dividend_yield(self, stock_symbol, price):
        """

        :type stock_symbol: string
        :type price: float
        """
        dividend_yield = 0.0
        if price < 0:
            logger.error("calculate_dividend_yield :: Price can not be negative")
            raise ValueError("Price cannot be negative")

        if not stock_symbol:
            logger.error("calculate_dividend_yield :: Stock Symbol can not be empty")
            raise ValueError("Stock Symbol cannot be None")

        stock = get_stock_by_symbol(stock_symbol)
        if stock.stock_type == StockType.COMMON.name:
            dividend_yield = StockServiceHelper.calculate_dividend_yield_for_common_stock(stock.last_dividend, price)
        elif stock.stock_type == StockType.PREFERRED.name:
            dividend_yield = StockServiceHelper.calculate_dividend_yield_for_pref_stock(
                        stock.fixed_dividend, stock.par_value, price)
        return dividend_yield

    def calculate_p_e_ratio(self, stock_symbol, price):
        """

                :type stock_symbol: string
                :type price: float
                """
        if price < 0:
            logger.error("calculate_p_e_ratio :: Price can not be negative")
            raise ValueError("Price cannot be negative")

        if not stock_symbol:
            logger.error("calculate_p_e_ratio :: Stock Symbol can not be empty")
            raise ValueError("Stock Symbol cannot be None")
        stock = get_stock_by_symbol(stock_symbol)
        p_e_ratio = StockServiceHelper.calculate_p_e_ratio(stock.last_dividend, price)
        return p_e_ratio

    def record_trade(self, stock_symbol, trade_data, stock=None):
        """
        :param stock:
        :return:
        :type stock_symbol: string
        :type trade_data: Trade object
        """
        if not stock_symbol:
            logger.error("record_trade :: Stock Symbol can not be empty")
            raise ValueError("Stock Symbol cannot be None")
        if not trade_data:
            logger.error("record_trade :: Trade data can not be empty")
            raise ValueError("Trade data cannot be None")
        if not stock:
            stock = get_stock_by_symbol(stock_symbol)
        trade = Trade()
        trade.indicator = trade_data.indicator
        trade.price = trade_data.price
        trade.quantity = trade_data.quantity
        trade.timestamp = trade_data.timestamp
        stock.trade_list = trade
        print(stock.trade_list)
        return stock

    def calculate_volume_weighted_price(self, stock_symbol, stock=None):
        """
        :param stock:
        :type stock_symbol: string
        """
        if not stock_symbol:
            logger.error("record_trade :: Stock Symbol can not be empty")
            raise ValueError("Stock Symbol cannot be None")
        if not stock:
            stock = get_stock_by_symbol(stock_symbol)
        vol_weighted_price = StockServiceHelper.calculate_vol_weight_price(stock)
        return vol_weighted_price

    def calculate_gbce_all_share_index(self):
        """

        """
        stock_list = get_all_stocks_from_config()
        gbce_all_share_index = StockServiceHelper().calculate_gbce_all_share_index(stock_list)
        return gbce_all_share_index
