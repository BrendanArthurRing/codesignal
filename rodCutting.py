# https://app.codesignal.com/challenge/AHL2v6hReiaHhZCJR


def accel_asc(n):
    # http://jeromekelleher.net/generating-integer-partitions.html
    # Function by By Jerome Kelleher, license unknown
    a = [0 for i in range(n + 1)]
    k = 1
    y = n - 1
    while k != 0:
        x = a[k - 1] + 1
        k -= 1
        while 2 * x <= y:
            a[k] = x
            y -= x
            k += 1
        l = k + 1
        while x <= y:
            a[k] = x
            a[l] = y
            yield a[:k + 2]
            x += 1
            y -= 1
        a[k] = x + y
        y = x + y - 1
        yield a[:k + 1]


def rodCutting(n, v):
    price = 0
    for i in accel_asc(n):
        total = 0
        for j in i:
            total += v[j]
        if total > price:
            price = total
    return price


n = 4
v = [0, 2, 4, 7, 7]
rodCutting(n, v)

# Start Testing

n = 4
v = [0, 2, 4, 7, 7]
assert rodCutting(n, v) == 9

n = 1
v = [0, 10]
assert rodCutting(n, v) == 10

n = 4
v = [0, 0, 4, 7, 1]
assert rodCutting(n, v) == 8

n = 10
v = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
assert rodCutting(n, v) == 10

n = 20
v = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 25]
assert rodCutting(n, v) == 25

n = 25
v = [0, 4, 10, 19, 19, 28, 32, 39, 41, 51, 57, 61, 61, 71,
     76, 77, 83, 85, 88, 95, 98, 103, 108, 113, 118, 121]
assert rodCutting(n, v) == 156


"""
Serling Enterprises buys long steel rods and cuts them into shorter rods, which it then sells. Each cut is free. Given a rod of length n and an array of prices v, where v[i] stands for the price of a piece with a length of i, determine the maximum revenue that you can obtain by cutting up the rod and selling the pieces.

Example

For n = 4 and v = [0, 2, 4, 7, 7], the output should be
rodCutting(n, v) = 9.

A rod with a length of 4 costs 7. You can cut it into 4 pieces of length 1 - this variant will have a revenue of 8. You can cut it into 2 pieces of length 2 - this variant will also have a revenue of 8. You can also cut it into pieces of lengths 1 and 3 - this variant will have a revenue of 2 + 7 = 9, which is the maximum possible.
"""

'''

In the example they give the following
1+1+1+1 = 4
and so since the index of 1 in the array v = 2 that would be 2+2+2+2 = 8

This problem might come down to finding all numbers that add up to the number n and then finding the greatest sum if you plug those numbers as indexes back into the array v.

I figured out that the numbers that add up to a sum are called addends
https://math.stackexchange.com/questions/1909222/how-to-find-all-possible-addends-for-a-large-number
And there is a mathmatica module called partitions that does this

So the terms addends and partitions are a good place to look.

https://stackoverflow.com/questions/10035752/elegant-python-code-for-integer-partitioning

This is called integer partitions
https://code.activestate.com/recipes/218332-generator-for-integer-partitions/

Generating integar partitions
http://jeromekelleher.net/generating-integer-partitions.html




def partitions(n):
    # https://code.activestate.com/recipes/218332-generator-for-integer-partitions/
    # This function is by David Eppstein under PSF License
    # But it does not pass the execution limit.
    if n == 0:
        yield []
        return
    for p in partitions(n - 1):
        yield [1] + p
        if p and (len(p) < 2 or p[1] > p[0]):
            yield [p[0] + 1] + p[1:]

'''
