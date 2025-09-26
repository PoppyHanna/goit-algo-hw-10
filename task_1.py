from typing import Dict

COINS = [50, 25, 10, 5, 2, 1]

# Жадібний алгоритм
def find_coins_greedy(amount: int) -> Dict[int, int]:
    result = {}
    for coin in COINS:
        if amount >= coin:
            count = amount // coin
            result[coin] = count
            amount -= coin * count
    return result

# Динамічне програмування
def find_min_coins(amount: int) -> Dict[int, int]:
    min_coins = [0] + [float("inf")] * amount

    last_coin = [0] * (amount + 1)

    for i in range(1, amount + 1):
        for coin in COINS:
            if coin <= i and min_coins[i - coin] + 1 < min_coins[i]:
                min_coins[i] = min_coins[i - coin] + 1
                last_coin[i] = coin

    result = {}
    current = amount
    while current > 0:
        coin = last_coin[current]
        result[coin] = result.get(coin, 0) + 1
        current -= coin

    return result

def print_desc(result: dict) -> dict:
    return {coin: result[coin] for coin in sorted(result.keys(), reverse=True)}

def print_asc(result: dict) -> dict:
    return {coin: result[coin] for coin in sorted(result.keys())}

if __name__ == "__main__":
    amount = 114

    greedy_res = find_coins_greedy(amount)
    dp_res = find_min_coins(amount)

    print(f"Greedy result for {amount}: {print_desc(greedy_res)}")
    print(f"DP result for {amount}: {print_asc(dp_res)}")    