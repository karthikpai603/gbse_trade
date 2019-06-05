from model.stock import StockType

STOCK_CONFIG = dict(TEA=dict(stock_type=StockType.COMMON, last_dividend=0.0, fixed_dividend=None, par_value=100.0),
                    POP=dict(stock_type=StockType.COMMON, last_dividend=8.0, fixed_dividend=None, par_value=100.0),
                    ALE=dict(stock_type=StockType.COMMON, last_dividend=23.0, fixed_dividend=None, par_value=60.0),
                    GIN=dict(stock_type=StockType.PREFERRED, last_dividend=8.0, fixed_dividend=2.0, par_value=100.0),
                    JOE=dict(stock_type=StockType.COMMON, last_dividend=13.0, fixed_dividend=None, par_value=250.0))