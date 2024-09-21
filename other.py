def helper(curr_num, n):
    if curr_num == n + 1:
        return 0
    return curr_num + helper(curr_num + 1, n)

def findSum(n):
    return helper(1, n)

print(findSum(5))