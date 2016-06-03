"""
coin change-- how do you make change with the least number of coins
Note: greedy solution does not work. E.g., if you have a quarter, dimes, and pennies,
the least number of coins is 3 dimes, not 1 quarter and 5 pennies

assume: we always have pennies so there is a guaranteed solution

related resource, see: https://jeremykun.com/2012/01/12/a-spoonful-of-python/
"""

"""
Dynamic programming solution is bottom up, i.e., we solve subproblems before making the first choice
"""

def coin_change(amount, coin_values):
    min_coins