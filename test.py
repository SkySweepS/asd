import timeit


def special_coins(coins: str, catalogue: str) -> int:
    count = 0
    for coin in coins:
        if coin in catalogue:
            count += 1
    return count


def special_coins2(coins: str, catalogue: str) -> int:
    count = 0
    catalogue = set(catalogue)
    for coin in coins:
        if coin in catalogue:
            count += 1
    return count


# Timing each approach using code strings
time_one = timeit.timeit("special_coins(coins='a'*4000, catalogue='cb'*100+'a')", globals=globals(), number=100000)
time_two = timeit.timeit("special_coins2(coins='a'*4000, catalogue='cb'*100+'a')", globals=globals(), number=100000)

print(f"Approach One took {time_one} seconds")
print(f"Approach Two took {time_two} seconds")

if time_one < time_two:
    print("Approach One is faster")
else:
    print("Approach Two is faster")
