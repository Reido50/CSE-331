# Reid Harry
# 2/9/2021

import datetime
from typing import Tuple, List

class Stock:
    """
    Implementation of a stock price on a given day.
    Do not modify.
    """

    __slots__ = ["date", "price"]

    def __init__(self, date: datetime.date, price: float) -> None:
        """
        Construct a stock.
        :param date: date of stock.
        :param price: the price of the stock at the given date.
        """
        self.date = date
        self.price = price

    def __repr__(self) -> str:
        """
        Represents the Stock as a string.
        :return: string representation of the Stock.
        """
        return f"<{str(self.date)}, ${self.price}>"

    def __str__(self) -> str:
        """
        Represents the Stock as a string.
        :return: string representation of the Stock.
        """
        return repr(self)
        
def intellishort(stocks: List[Stock]) -> Tuple[datetime.date, datetime.date, float]:
    """
    :param stocks: a list of `Stock` objects
    :return: Tuple of the form described
    """

    if len(stocks) != 0:
        # Init streakBegin, streakEnd
        streakBegin = None
        streakEnd = None

        # Init initPrice and curPrice
        initPrice = stocks[0].price
        curPrice = stocks[0].price

        # Init maxStreakBegin maxStreakEnd
        maxStreakBegin = stocks[0].date
        maxStreakEnd = stocks[0].date

        # Init maxInitPrice and maxCurPrice
        maxInitPrice = -1
        maxCurPrice = -1
    else:
        return (None, None, 0)

    # Traverse stocks list (except final element)
    for i in range(len(stocks)-1):
        if stocks[i+1].price <= curPrice:
            # Decreased or stayed same from previous
            # Set up or conitnue a streak
            curPrice = stocks[i+1].price
            streakEnd = stocks[i+1].date
            if streakBegin is None:
                streakBegin = stocks[i].date
        else:
            # Strictly increased from previous
            # Break the streak
            streakBegin = None
            streakEnd = None
            curPrice = stocks[i+1].price
            initPrice = stocks[i+1].price
        if streakBegin is not None:
            # Update max streak if needed
            priceDiff = (initPrice - curPrice) - (maxInitPrice - maxCurPrice)
            dateDiff = (streakEnd - streakBegin) - (maxStreakEnd - maxStreakBegin)
            if (priceDiff > 0) or (priceDiff == 0 and dateDiff.days > 0):
                # Current streak is stronger than max streak
                maxCurPrice = curPrice
                maxInitPrice = initPrice
                maxStreakBegin = streakBegin
                maxStreakEnd = streakEnd

    return (maxStreakBegin, maxStreakEnd, maxInitPrice - maxCurPrice)