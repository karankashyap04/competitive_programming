"""
This is a solution to the problem 'Sums in a Triangle'
Problem code: SUMTRIAN
"""

def fill_triangle(n: int) -> "list[list[int]]":
    triangle = []
    for _ in range(n):
        this_row = [int(i) for i in input().split()]
        triangle.append(this_row)
    return triangle

def get_max(n: int, triangle: "list[list[int]]") -> "list[list[int]]":
    dp = []
    for i in range(n):
        dp.append([])
    for row in range(n - 1, -1, -1):
        if row == n - 1:
            dp[row] = triangle[row]
        else:
            for col in range(row + 1):
                dp[row].append(triangle[row][col] + max(dp[row+1][col], dp[row+1][col+1]))
    return dp

t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    triangle = fill_triangle(n)
    result = get_max(n, triangle)
    print(result[0][0])