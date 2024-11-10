
def check(mid : int, n : int , m : int) -> int:
    result = 1
    for i in range(1 , n  + 1):
        result = result * mid
        if result > m:
            return 2
    if result == m:
        return 1
    return 0


def NthRoot(n : int , m : int) -> int:
    low = 1
    high = m
    while(low <= high):
        mid = (low + high) // 2
        currentAns = check(mid , n , m)
        if currentAns == 1:
            return mid
        elif currentAns == 0:
            low = mid + 1
        else:
            high = mid - 1
    return -1

n = 3
m = 27
ans = NthRoot(n, m)

print(ans)