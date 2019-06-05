import logging
import datetime
import math

logger = logging.getLogger('stock_service_helper')
logger.setLevel(logging.INFO)


class StockServiceHelper(object):

    @staticmethod
    def calculate_dividend_yield_for_common_stock(last_dividend, price):
        """

        :param last_dividend:
        :param price:
        :return:
        """
        if price == 0.0:
            raise ValueError("calculate_dividend_yield_for_common_stock : Dividend Yield can not be "
                             "calculated when price is 0")
        dividend_yield = float(last_dividend / price)
        logger.info("Dividend yield-" + str(dividend_yield) + " calculated for Common Stock with "
                    "Last Dividend-" + str(last_dividend) +
                    "  and price-" + str(price))
        return round(dividend_yield, 2)

    @staticmethod
    def calculate_dividend_yield_for_pref_stock(fixed_dividend, par_value, price):
        """

        :param fixed_dividend:
        :param par_value:
        :param price:
        :return:
        """
        if price == 0.0:
            raise ValueError("calculate_dividend_yield_for_pref_stock : Dividend Yield can not be "
                             "calculated when price is 0")
        dividend_yield = float((fixed_dividend * par_value) / price)
        logger.info("Dividend yield-" + str(dividend_yield) + " calculated for Preferred Stock with "
                    "Fixed Dividend-" + str(fixed_dividend)
                    + "  and par value-" + str(par_value)
                    + "  and price-" + str(price))
        return round(dividend_yield, 2)

    @staticmethod
    def calculate_p_e_ratio(last_dividend, price):
        """

        :param last_dividend:
        :param price:
        :return:
        """
        if last_dividend == 0:
            raise ValueError("calculate_p_e_ratio: P/E Ratio cannot be calculated when last dividend is 0")
        p_e_ratio = float(price / last_dividend)
        logger.info("P/E Ratio " + str(p_e_ratio) + " calculated for last dividend " + str(last_dividend)
                    + " and price " + str(price))
        return round(p_e_ratio, 2)

    @staticmethod
    def calculate_vol_weight_price(stock):
        """

        :param stock:
        :return:
        """
        volume_weighted_price = 0.0
        trades = stock.trade_list
        quantity_total = 0
        quantity_price_total = 0.0
        current_time = datetime.datetime.now()
        for trade in trades:
            time_difference = int((current_time - trade.timestamp).total_seconds())
            if time_difference < 300:
                quantity_total += trade.quantity
                quantity_price_total += trade.quantity * trade.price
        if quantity_total != 0:
            volume_weighted_price = float(quantity_price_total / quantity_total)
        logger.info("Volume Weighted Price-" + str(volume_weighted_price) + "calculated for trades of "
                    "last 5 minutes for Stock -"
                    + stock.stock_symbol)
        return round(volume_weighted_price, 2)

    def calculate_gbce_all_share_index(self, stock_list):
        """

        :param stock_list:
        :return:
        """
        vol_weight_price_total = 0
        for stock in stock_list:
            vol_weight_price_total += self.calculate_vol_weight_price(stock)
        gbce_all_share_index = float(math.pow(vol_weight_price_total, 1.0 / len(stock_list)))
        logger.info(
            "GBCE All Shared Index -" + str(gbce_all_share_index) + " calculated for total "
            + str(len(stock_list)) + " stocks")
        return round(gbce_all_share_index, 4)
