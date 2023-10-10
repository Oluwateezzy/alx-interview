#!/usr/bin/python3
"""Maria and Ben are playing a game.
   Given a set of consecutive integers
   starting from 1 up to and including n,
   they take turns choosing a prime number
   from the set and removing that number
   and its multiples from the set.
   The player that cannot make a move loses the game.
"""


def isWinner(x, nums):
    """ isWinner """
    player = {"Maria": 0, "Ben": 0}
    n = max(nums)
    primes = [0, 0, 2]
    add_prime(max(nums), primes)
    for round in range(x):
        _sum = sum((i != 0 and i <= nums[round])
                   for i in primes[:nums[round] + 1])
        if (_sum % 2):
            winner = "Maria"
        else:
            winner = "Ben"
        if winner:
            player[winner] += 1
    if player["Maria"] > player["Ben"]:
        return "Maria"
    elif player["Ben"] > player["Maria"]:
        return "Ben"

    return None


def add_prime(n, primes):
    """ Add prime to list """
    last_prime = primes[-1]
    if n > last_prime:
        for i in range(last_prime + 1, n + 1):
            if isPrime(i):
                primes.append(i)
            else:
                primes.append(0)


def isPrime(number):
    """ check prime number """
    for i in range(2, int(number ** 0.5) + 1):
        if not number % i:
            return False
    return True
