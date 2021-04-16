def change(total : int, coins : list) -> int:
    # Init combinations list
    combinations = [0] * (total + 1)
    combinations[0] = 1
    # Dynamically fill combinations list
    for coin in coins:
        for amount in range(1, len(combinations)):
            if amount >= coin:
                combinations[amount] += combinations[amount-coin]
    # Return number of combinations for total
    return combinations[total]

# TEST 1: Should return 1
print(change(12, [1]))
# TEST 2: Should return 7
print(change(12, [1,2]))
# TEST 3: Should return 13
print(change(12, [1, 2, 5]))
