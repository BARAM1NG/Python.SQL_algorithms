def solution(n):
    num = 0
    for i in range(1, n + 1):
        if n % i == 0:
            num += i
        else:
            pass
    return num