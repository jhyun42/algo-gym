import sys

INPUT = sys.stdin.readline
N = int(INPUT())
TEAM_STAT_MAT = [list(map(int, INPUT().split())) for _ in range(N)]


def solution():
    global TEAM_STAT_MAT, N

    ret = float('inf')
    pick_set = set()

    def update_min():
        nonlocal pick_set, ret

        team_1 = list(pick_set)
        team_2 = set([i for i in range(N)])
        team_2 = list(team_2.difference(team_1))

        team_1_stats = 0
        team_2_stats = 0
        for i in range(N // 2):
            for j in range(i, N // 2):
                team_1_stats += TEAM_STAT_MAT[team_1[i]][team_1[j]] + TEAM_STAT_MAT[team_1[j]][team_1[i]]
                team_2_stats += TEAM_STAT_MAT[team_2[i]][team_2[j]] + TEAM_STAT_MAT[team_2[j]][team_2[i]]

        ret = min(ret, abs(team_1_stats - team_2_stats))

    def backtracking(curr_player_idx, pick_count):
        nonlocal pick_set

        if pick_count == N // 2:
            update_min()
            return

        for player_idx in range(curr_player_idx, N):
            pick_set.add(player_idx)
            backtracking(player_idx + 1, pick_count + 1)
            pick_set.remove(player_idx)

    backtracking(0, 0)
    return ret


ret = solution()
print(ret)
