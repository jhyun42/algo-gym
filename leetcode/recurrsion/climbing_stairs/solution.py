from collections import defaultdict


def climb_stairs(n):
    def helper(n, memo):
        if n not in memo.keys():
            memo[n] = helper(n - 1, memo) + helper(n - 2, memo)

        return memo[n]

    memo = defaultdict(int)
    memo[0] = memo[1] = 1

    return helper(n, memo)
