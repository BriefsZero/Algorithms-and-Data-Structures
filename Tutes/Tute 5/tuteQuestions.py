def coinChangeBottomUp(coins, value):
    min_coins = [0] * value
    min_coins[0] = 0
    for x in range(1, value):
        for y in range(1, len(coins)):
            if coins[y] < x:
                min_coins[x] = min(min_coins[x], 1+min_coins[x - coins[y]])
    return min_coins[value]



def coinChange(coins, value):
    memo = [None] * value
    coinChangeTopDown(coins, value, memo)

def coinChangeTopDown(coins, value, memo):
    if value == 0:
        return 0

    if memo[value] == None:
       min_coins = None
       for i in range(1, len(coins)):
           if coins[i] <= value:
               min_coins = min(min_coins, 1 + coinChangeTopDown(value - coins[i]))

       memo[value] = min_coins

    return memo[value]


def findMaxSub(arr):
    t = [1] * len(arr)
    for i in range(1, len(arr)):
        for j in range(i):
            if arr[j] < arr[i]:
                t[i] = max(t[i], t[j] + 1)
    return max(t)

print(findMaxSub([0, 8, 4, 12,2, 10,6, 14, 1,9, 5, 13, 3,11, 7,15]))