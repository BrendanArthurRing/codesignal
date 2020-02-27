def secondRightmostZeroBit(n):
    return = 2 ** bin(n)[::-1].index('0', bin(n)[::-1].index('0') + 1)


assert secondRightmostZeroBit(37) == 8, "Failed"
