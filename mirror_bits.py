def mirrorBits(a):
    return int(f'{a:b}'[::-1], 2)


assert mirrorBits(97) == 55, "Failed"


# This was the top voted
def mirrorBits(a):
    return int(bin(a)[2:][::-1], 2)
