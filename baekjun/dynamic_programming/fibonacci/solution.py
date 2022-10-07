N = int(input())


def solution(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


ret = solution(N)
print(ret)
