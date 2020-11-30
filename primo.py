def ehPrimo(n):
    count = 2
    if n == 2:
        return True
    while n % count != 0 and count <= n/2:
        count += 1
    if n % count == 0:
        return False
    else:
        return True