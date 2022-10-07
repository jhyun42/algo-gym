N = int(input())


def solution(n):
    dp_table = [0] * (n + 1)

    for i in range(2, n + 1):
        dp_table[i] = dp_table[i - 1] + 1
        print(dp_table)
        if i % 3 == 0:
            dp_table[i] = min(dp_table[i], dp_table[i // 3] + 1)
        if i % 2 == 0:
            dp_table[i] = min(dp_table[i], dp_table[i // 2] + 1)
    ret = dp_table[n]
    return ret


ret = solution(N)
print(ret)
