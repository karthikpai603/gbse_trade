from config.stock_config import STOCK_CONFIG
from model.stock import Stock
from constants.stock_constants import *
stock_list = []


def get_all_stocks_from_config():
    """

    :return:
    """
    for key, value in STOCK_CONFIG.items():
        new_stock = Stock()
        new_stock.stock_symbol = key
        new_stock.last_dividend = value.get(LAST_DIVIDEND)
        new_stock.fixed_dividend = value.get(FIXED_DIVIDEND)
        new_stock.par_value = value.get(PAR_VALUE)
        new_stock.stock_type = value.get(STOCK_TYPE)
        stock_list.append(new_stock)
    return stock_list


def get_stock_by_symbol(stock_symbol):
    """

    :param stock_symbol:
    :return:
    """
    new_stock = None
    for key, value in STOCK_CONFIG.items():
        if stock_symbol == key:
            new_stock = Stock()
            new_stock.stock_symbol = key
            new_stock.last_dividend = value.get(LAST_DIVIDEND)
            new_stock.fixed_dividend = value.get(FIXED_DIVIDEND)
            new_stock.par_value = value.get(PAR_VALUE)
            new_stock.stock_type = value.get(STOCK_TYPE)
            break
    return new_stock
