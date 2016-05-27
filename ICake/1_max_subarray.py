import random

def get_max_profit(stock_prices):

    # ensure we have at least 2 prices
    if len(stock_prices) < 2:
        raise IndexError('Getting a profit requires at least 2 prices')

    # use greedy algorithm to store min_price and max_profit as you iterate through prices
    # begin by initializing them to the first price/first profit
    min_price = stock_prices[0]
    max_profit = stock_prices[1] - stock_prices[0]

    for index, current_price in enumerate(stock_prices):

        # skip first element since you can't both buy/sell at time 0
        if index == 0:
            continue

        # see what profit would be if we sold at current price
        potential_profit = current_price - min_price

        # update max profit if it's better
        max_profit = max(max_profit, potential_profit)

        # update min_price, so it's always the lowest price seen so far
        min_price = min(min_price, current_price)

    return max_profit

if __name__ == "__main__":

    random_prices = []
    for i in range(100):
        random_prices.append(random.randrange(-50, 50))

    print get_max_profit(random_prices)