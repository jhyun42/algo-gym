"""
보드 판에는 물고기의 번호와 이동방향이 입력됨

상어는 0,0 에서 시작하고 현재 위치의 물고기를 먹고

물고기 턴
1. 물고기가 작은 번호부터 움직인다

2. 물고기가 움지이려는 칸이 벽이거나 상어가 있는 칸이면 반시계방향으로 방향을 전환
- 계속 45도씩 턴하면서 갈 수 있는 방향을 찾음

3. 움직이려는 칸에 다른 물고기가 있다면 두 물고기가 자리를 교체수

4. 움직이려는 칸에 물고기가 없다면 그냥 이동

상어 턴
물고기의 이동이 완료되면 상어는 "잡머먹은 물고기"의 이동방향으로 1칸 또는 2칸 또는 3칸까지 이동한다
- 잡아먹은 물고기 방향 정보를 상어가 흡

종료조건:
상어가 보드 밖으로 나가면 처리는 종료
먹은 물고기의 최대의 길이의 합 --> 경우의 수를 요구하기 떄문에 backtracking?

물고기가 움직이는 지도와 물고기의 정보를 따로 저장하고
정보가 변할때 sync를 맞춰서 업데이트 해줌
"""

# 순서 중요
import copy

DIRECTIONS = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]
MAP = [list(map(int, input().split())) for _ in range(4)]
BOARD = [[0 for _ in range(4)] for _ in range(4)]
FISH_LIST = [[0, 0, 0] for _ in range(16)]

for r_idx, shark_line in enumerate(MAP):
    BOARD[r_idx][0], BOARD[r_idx][1], BOARD[r_idx][2], BOARD[r_idx][3] = \
        shark_line[0] - 1, shark_line[2] - 1, shark_line[4] - 1, shark_line[6] - 1
    FISH_LIST[shark_line[0] - 1][0] = r_idx
    FISH_LIST[shark_line[0] - 1][1] = 0
    FISH_LIST[shark_line[0] - 1][2] = shark_line[1] - 1

    FISH_LIST[shark_line[2] - 1][0] = r_idx
    FISH_LIST[shark_line[2] - 1][1] = 1
    FISH_LIST[shark_line[2] - 1][2] = shark_line[3] - 1

    FISH_LIST[shark_line[4] - 1][0] = r_idx
    FISH_LIST[shark_line[4] - 1][1] = 2
    FISH_LIST[shark_line[4] - 1][2] = shark_line[5] - 1

    FISH_LIST[shark_line[6] - 1][0] = r_idx
    FISH_LIST[shark_line[6] - 1][1] = 3
    FISH_LIST[shark_line[6] - 1][2] = shark_line[7] - 1


def solution():
    global FISH_LIST

    ret = 0

    def solve(board, fish_list, shark_y, shark_x, ate_sum):

        nonlocal ret

        candidate_board = [[0 for _ in range(4)] for _ in range(4)]
        candidate_fish = [[0, 0, 0] for _ in range(16)]

        for r in range(4):
            for c in range(4):
                candidate_board[r][c] = board[r][c]

        for x in range(16):
            candidate_fish[x][0] = fish_list[x][0]
            candidate_fish[x][1] = fish_list[x][1]
            candidate_fish[x][2] = fish_list[x][2]

        fish_number = candidate_board[shark_y][shark_x]
        shark_dir = candidate_fish[fish_number][2]
        candidate_fish[fish_number][0] = -1
        candidate_fish[fish_number][1] = -1
        candidate_fish[fish_number][2] = -1
        candidate_board[shark_y][shark_x] = -1

        ate_sum += (fish_number + 1)
        ret = max(ate_sum, ret)

        # Fish move
        for fish_idx in range(16):

            if candidate_fish[fish_idx][0] == -1:
                continue

            curr_y = candidate_fish[fish_idx][0]
            curr_x = candidate_fish[fish_idx][1]
            curr_dir = candidate_fish[fish_idx][2]

            new_y = curr_y + DIRECTIONS[curr_dir][0]
            new_x = curr_x + DIRECTIONS[curr_dir][1]
            new_dir = curr_dir

            # 상어를 만나거나 벽을 만날때 45도씩 회전하면서 자리 찾기
            while new_y < 0 or new_y >= 4 or new_x < 0 or new_x >= 4 or (new_y == shark_y and new_x == shark_x):
                new_dir = (new_dir + 1) % 8
                new_y = curr_y + DIRECTIONS[new_dir][0]
                new_x = curr_x + DIRECTIONS[new_dir][1]

            # 물고기 이동을 위해 자리 바꾸기
            if candidate_board[new_y][new_x] != -1:

                target = candidate_board[new_y][new_x]

                candidate_fish[target][0] = curr_y
                candidate_fish[target][1] = curr_x

                candidate_fish[fish_idx][0] = new_y
                candidate_fish[fish_idx][1] = new_x
                candidate_fish[fish_idx][2] = new_dir

                candidate_board[new_y][new_x] = fish_idx
                candidate_board[curr_y][curr_x] = target

            else:
                candidate_fish[fish_idx][0] = new_y
                candidate_fish[fish_idx][1] = new_x
                candidate_fish[fish_idx][2] = new_dir

                candidate_board[new_y][new_x] = fish_idx
                candidate_board[curr_y][curr_x] = -1

        # Shark move
        for step in range(1, 4):

            new_y = shark_y + DIRECTIONS[shark_dir][0] * step
            new_x = shark_x + DIRECTIONS[shark_dir][1] * step

            if new_y < 0 or new_y >= 4 or new_x < 0 or new_x >= 4:
                break

            if candidate_board[new_y][new_x] != -1:
                solve(candidate_board, candidate_fish, new_y, new_x, ate_sum)

    solve(BOARD, FISH_LIST, 0, 0, 0)
    return ret


print(solution())
