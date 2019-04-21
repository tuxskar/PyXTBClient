from client.constants import MarginMode, ProfitMode


class RateInfoRecord:
    def __init__(self, close, ctm, ctmString, high, low, open, vol, digits=0):
        """ Rate information record
        :param close {float} Value of close price (shift from open price)
        :param ctm	{timestamp}	Candle start time in CET / CEST time zone (see Daylight Saving Time, DST)
                - since epoch in milliseconds
        :param ctmString {string} String representation of the 'ctm' field
                - Ex: "Jan 10, 2014 3:04:00 PM"
        :param high	{float} Highest value in the given period (shift from open price)
        :param low	{float} Lowest value in the given period (shift from open price)
        :param open	{float} Open price (in base currency * 10 to the power of digits)
        :param vol	{float} Volume in lots
        :param digits {int}
        """
        self.close = close
        self.ctm = ctm
        self.ctm_string = ctmString
        self.high = high
        self.low = low
        self.open = open
        self.volume = vol
        self.digits = digits

    def __repr__(self):
        return '{}'.format(self.__dict__)


class Symbol(object):
    def __init__(self, symbol, currency, categoryName, currencyProfit, quoteId, quoteIdCross, marginMode, profitMode,
                 pipsPrecision, contractSize, exemode, time, expiration, stopsLevel, precision, swapType, stepRuleId,
                 type, instantMaxVolume, groupName, description, longOnly, trailingEnabled, marginHedgedStrong,
                 swapEnable, percentage, bid, ask, high, low, lotMin, lotMax, lotStep, tickSize, tickValue, swapLong,
                 swapShort, leverage, spreadRaw, spreadTable, starting, swap_rollover3days, marginMaintenance,
                 marginHedged, initialMargin, shortSelling, currencyPair, timeString):
        """
        Represents a symbol to trade with
        Ex: EURUSD, WHEAT or US500
        """
        self.symbol = symbol
        self.currency = currency
        self.category_name = categoryName
        self.currency_profit = currencyProfit
        self.quote_id = quoteId
        self.quote_id_cross = quoteIdCross
        self.margin_mode = marginMode
        self.profit_mode = profitMode
        self.pips_precision = pipsPrecision
        self.contract_size = contractSize
        self.exemode = exemode
        self.time = time
        self.expiration = expiration
        self.stops_level = stopsLevel
        self.precision = precision
        self.swap_type = swapType
        self.step_rule_id = stepRuleId
        self.type = type
        self.instant_max_volume = instantMaxVolume
        self.group_name = groupName
        self.description = description
        self.long_only = longOnly
        self.trailing_enabled = trailingEnabled
        self.margin_hedged_strong = marginHedgedStrong
        self.swap_enable = swapEnable
        self.percentage = percentage
        self.bid = bid
        self.ask = ask
        self.high = high
        self.low = low
        self.lot_min = lotMin
        self.lot_max = lotMax
        self.lot_step = lotStep
        self.tick_size = tickSize
        self.tick_value = tickValue
        self.swap_long = swapLong
        self.swap_short = swapShort
        self.leverage = leverage
        self.spread_raw = spreadRaw
        self.spread_table = spreadTable
        self.starting = starting
        self.swap_rollover3days = swap_rollover3days
        self.margin_maintenance = marginMaintenance
        self.margin_hedged = marginHedged
        self.initial_margin = initialMargin
        self.short_selling = shortSelling
        self.currency_pair = currencyPair
        self.time_string = timeString

        self.profit_mode_description = ProfitMode.descriptions.get(self.profit_mode, 'N/A')
        self.margin_mode_description = MarginMode.descriptions.get(self.margin_mode, 'N/A')

    def __repr__(self):
        return "{} - {} ({} {}) {}".format(self.symbol, self.category_name, self.margin_mode_description,
                                           self.currency, self.description)
