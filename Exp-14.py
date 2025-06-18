def climb_stairs(n):
    if n <= 2:
        return n
    ways = [0] * (n + 1)
    ways[1] = 1  # 1 way to climb 1 step
    ways[2] = 2  # 2 ways to climb 2 steps: (1+1), (2)
    
    for i in range(3, n + 1):
        ways[i] = ways[i-1] + ways[i-2]
        
    return ways[n]

# Example input
n = 4
print(climb_stairs(n))  # Output: 5
