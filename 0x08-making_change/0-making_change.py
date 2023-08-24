#!/usr/bin/python3
'''
A modul which solves coin problem
'''


def makeChange(coins, total):
    '''
    A function which returns fewest number of coins needed to
    meet a given total coin number if total is not less than 0
    '''
    if total < 0:
        return -1  
    if total == 0:
        return 0  
    
    min_coins = -1
    
    for coin in coins:
        count = makeChange(coins, total - coin)
        if count != -1:
            if min_coins == -1 or count + 1 < min_coins:
                min_coins = count + 1
    
    return min_coins
