def max_gold_coins(N):
    coins = [0] * (N + 1)
    coins[1] = 1
    for i in range(2, N + 1):
        if i % 2 == 0:
            coins[i] = coins[i // 2]
        else:
            coins[i] = coins[i // 2] + coins[(i // 2) + 1]
    return max(coins) , coins
N = int(input())
a , b = max_gold_coins(N)

