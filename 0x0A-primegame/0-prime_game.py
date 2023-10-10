#!/usr/bin/python3
"""Maria and Ben are playing a game.
   Given a set of consecutive integers starting from 1 up to and including n,
   they take turns choosing a prime number from the set and removing that number 
   and its multiples from the set. The player that cannot make a move loses the game.
"""

def isWinner(x, nums):
    """ isWinner """
    player = {'Ben': 0, 'Maria': 0}
    n = max(nums)
    primes = []
    
    if n > 2:
        for i in range(3, n+1):
            if isPrime(i):
                primes.append(i)
            else:
                primes.append(0)
    for round in range(x):
        total = sum((i != 0 and i <= nums[round]) for i in primes[:nums[round] + 1])
        if (total % 2):
            winner = "Maria"
        else:
            winner = "Ben"
        if winner:
            player[winner] += 1
    if player['Maria'] > player['Ben']:
        return 'Maria'
    elif player['Ben'] > player['Maria']:
        return 'Ben'
    return None

def isPrime(number):
    """ check prime number """
    for i in range(2, number + 1):
        if number % i == 0:
            return False
        else:
            return True
