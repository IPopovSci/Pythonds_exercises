#Very inefficient

def recMC(coinValueList,change):
   minCoins = change
   print('minCoins','*'*10,minCoins)
   if change in coinValueList:
     return 1
   else:
      for i in [c for c in coinValueList if c <= change]:
         numCoins = 1 + recMC(coinValueList,change-i)
         print('numCoins','*'*10,numCoins)
         if numCoins < minCoins:
            minCoins = numCoins
   return minCoins

#W/ added caching
def recDC(coinValueList,change,knownResults):
    minCoins = change
    print('minCoins','*'*10,minCoins)
    if change in coinValueList:
       knownResults[change] = 1
       return 1
    elif knownResults[change] > 0:
       return knownResults[change]
    else:
        for i in [c for c in coinValueList if c <= change]:
          numCoins = 1 + recDC(coinValueList, change-i,
                               knownResults)
          print('numCoins', '*' * 10, numCoins)
          if numCoins < minCoins:
             minCoins = numCoins

             knownResults[change] = minCoins
             print('knownResults', '*' * 10, knownResults)

    return minCoins

#Dynamic programming

def dpMakeChange(coinValueList,change,minCoins,coinsUsed):
   for cents in range(change+1):
      coinCount = cents
      newCoin = 1
      for j in [c for c in coinValueList if c <= cents]:
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

def main():
    amnt = 33
    clist = [1,5,8,10,21,25]
    coinsUsed = [0]*(amnt+1)
    coinCount = [0]*(amnt+1)

    print("Making change for",amnt,"requires")
    print(dpMakeChange(clist,amnt,coinCount,coinsUsed),"coins")
    print("They are:")
    printCoins(coinsUsed,amnt)
    print("The used list is as follows:")
    print(coinsUsed)

main()