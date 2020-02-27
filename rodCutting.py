# https://app.codesignal.com/challenge/AHL2v6hReiaHhZCJR


def rodCutting(n, v):

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
