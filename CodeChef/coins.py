"""
This is a solution to the problem 'Bytelandian Gold Coins'
Problem code: COINS
"""

coin_values = dict()
coin_values[0] = 0

def get_value(n: int) -> int:
    if n not in coin_values:
        divide_value = get_value(n//2) + get_value(n//3) + get_value(n//4)
        coin_values[n] = max(divide_value, n)
    return coin_values[n]

while True:
    try:
        n = int(input())
    except:
        break
    print(get_value(n))