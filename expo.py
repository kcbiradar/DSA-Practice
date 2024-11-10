def expo(base : int, expo : int) -> int:
    result = 1
    while expo > 0:
        if expo % 2:
            result = result * base
        base = base * base
        expo //= 2

    return result

print(expo(2 , 5))
