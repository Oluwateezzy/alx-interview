def numSquares(n: int) -> int:
    perfect = []
    for i in range(1, n):
        sq_r = int(i**0.5)
        if sq_r ** 2 == i:
            perfect.append(i)
    return perfect

print(numSquares(12))