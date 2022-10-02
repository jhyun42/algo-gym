import collections
import sys

inputs = sys.stdin.readline
N = int(inputs())
counseling_info = [list(map(int, inputs().split())) for _ in range(N)]


def solution(n, info):
    adj_list = collections.defaultdict(tuple)
    for d, (t, p) in enumerate(info):
        adj_list[d + 1] = (t, p)

    ret = 0

    def dfs(curr_day, curr_sum):
        nonlocal adj_list, n, ret

        if curr_day == n:
            ret = max(curr_sum, ret)
            return

        dfs(curr_day + 1, curr_sum)

        if curr_day + adj_list[curr_day + 1][0] <= n:
            dfs(curr_day + adj_list[curr_day + 1][0], curr_sum + adj_list[curr_day + 1][1])

    dfs(curr_day=0, curr_sum=0)

    return ret


ret = solution(N, counseling_info)
print(ret)
