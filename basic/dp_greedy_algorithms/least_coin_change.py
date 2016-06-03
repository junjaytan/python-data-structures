"""
Some examples of how to solve the least number of coins to make change problem
using Dynamic Programming and Memoization
see: http://interactivepython.org/runestone/static/pythonds/Recursion/DynamicProgramming.html
"""


def recDC(coinValueList,change,knownResults):
    """ Modified memoized recursion schema to find least number of coins to make change
    :param coinValueList: list of possible coins
    :param change: amount you need change for
    :param knownResults: a list holding the min coins to make change for an amount from 0 to the desired amount
    :return:
    """
    minCoins = change
    if change in coinValueList:
        knownResults[change] = 1
        return 1
    elif knownResults[change] > 0:
        return knownResults[change]
    else:
       for i in [c for c in coinValueList if c <= change]:
         numCoins = 1 + recDC(coinValueList, change-i,
                              knownResults)
         if numCoins < minCoins:
            minCoins = numCoins
            knownResults[change] = minCoins
    return minCoins

"""
DP solution
"""
def dpMakeChange(coinValueList,change,minCoins,coinsUsed):
   for cents in range(change+1):
      coinCount = cents
      newCoin = 1
      for j in [c for c in coinValueList if c <= cents]:    # use list comprehension to generate a list containing only entries that meet condition
            if minCoins[cents-j] + 1 < coinCount:
               coinCount = minCoins[cents-j]+1
               newCoin = j
      minCoins[cents] = coinCount
      coinsUsed[cents] = newCoin
   return minCoins[change]

def printCoins(coinsUsed,change):
   coin = change
   while coin > 0:
      thisCoin = coinsUsed[coin]
      print(thisCoin)
      coin = coin - thisCoin


if __name__=="__main__":
    #print(recDC([1,5,10,25],63,[0]*64))
    coinValueList = [1, 5, 6, 7, 4]
    j = [c for c in coinValueList if c < 6]
    print j

    amnt = 63
    clist = [1,5,10,21,25]
    coinsUsed = [0]*(amnt+1)
    coinCount = [0]*(amnt+1)
    print dpMakeChange(clist, amnt, coinCount, coinsUsed)