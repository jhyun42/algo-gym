M, S = map(int, input().split())
FISHES = [list(map(int, input().split())) for _ in range(M)]
START_R, START_C = map(int, input().split())

FISH_DIRECTIONS = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
SHARK_DIRECTIONS = [(-1, 0), (0, -1), (1, 0), (0, 1)]

FISH_MAP = [[[] for _ in range(4)] for _ in range(4)]
for R, C, D in FISHES:
    FISH_MAP[R - 1][C - 1].append(D - 1)

SMELL_MAP = [[0 for _ in range(4)] for _ in range(4)]


# 1. 물고기 이동 -> move_fishes() 구현
# 2. 상어 이동 -> 3개 가지수, backtracking, dfs를 통해서 최대 이득 찾기. 이동방법 사전 수도 고려해야함
# 3. 2번 돌면 물고기 시체 제외
# 4. 복제 마법 -> 기존 물고기 + 복제된 물고기 추가

def move_fishes(fish_map, curr_shark_r, curr_shark_c):
    tmp_map = [[[] for _ in range(4)] for _ in range(4)]

    for r in range(4):
        for c in range(4):
            while fish_map[r][c]:

                # 하나의 cell의 모든 요소들을 다 꺼내서 본다
                fish_dir = fish_map[r][c].pop()

                # 물고기들이 현재 위치에서 반시계로 45도씩 돌면서 다음 방향으로 방향전환
                for new_dir in range(fish_dir, fish_dir - 8, -1):

                    # 한바퀴 돌아본다 while문 대신 for 문으로 한바퀴 돌면 그 자리 멈출 수 있게
                    new_dir %= 8

                    new_r = r + FISH_DIRECTIONS[new_dir][0]
                    new_c = c + FISH_DIRECTIONS[new_dir][1]

                    if new_r < 0 or new_r >= 4 or new_c < 0 or new_c >= 4:
                        continue

                    if (curr_shark_r, curr_shark_c) == (new_r, new_c) or SMELL_MAP[new_r][new_c]:
                        continue

                    tmp_map[new_r][new_c].append(new_dir)

                    # 방향 찾으면 break
                    break

                # break 안돌고 다 돌면 걍 제자리에 append
                else:
                    tmp_map[r][c].append(fish_dir)

    for r in range(4):
        for c in range(4):
            fish_map[r][c].extend(tmp_map[r][c])


def solution():
    global M, S, START_C, START_R

    shark_pos = (START_R - 1, START_C - 1)

    def backtracking(fish_map, shark_r, shark_c, curr_depth, num_fishes_ate, visit_pos_list):
        nonlocal max_ate_fish, shark_pos, best_travel_path

        if curr_depth == 3:
            if max_ate_fish < num_fishes_ate:
                max_ate_fish = num_fishes_ate
                shark_pos = (shark_r, shark_c)
                best_travel_path = visit_pos_list[:]
            return

        for shark_diff_r, shark_diff_c in SHARK_DIRECTIONS:

            new_r = shark_r + shark_diff_r
            new_c = shark_c + shark_diff_c

            if new_r < 0 or new_r >= 4 or new_c < 0 or new_c >= 4:
                continue

            # 이미 방문한 장소면 그냥 depth만 늘림
            if (new_r, new_c) in visit_pos_list:
                backtracking(fish_map, new_r, new_c, curr_depth + 1, num_fishes_ate, visit_pos_list)

            else:
                visit_pos_list.append((new_r, new_c))
                backtracking(
                    fish_map,
                    new_r,
                    new_c,
                    curr_depth + 1,
                    num_fishes_ate + len(fish_map[new_r][new_c]),
                    visit_pos_list
                )
                visit_pos_list.remove((new_r, new_c))

    for _ in range(S):

        best_travel_path = list()
        max_ate_fish = -1

        curr_shark_r, curr_shark_c = shark_pos

        tmp_map = [[[] for _ in range(4)] for _ in range(4)]
        for r in range(4):
            for c in range(4):
                tmp_map[r][c].extend(FISH_MAP[r][c])

        # 1. 물고기들 이동
        move_fishes(tmp_map, curr_shark_r, curr_shark_c)

        # 2. 상어이동 backtracking 사용
        backtracking(tmp_map, curr_shark_r, curr_shark_c, 0, 0, list())

        # 3. 물고기 시체 컨트롤
        for r in range(4):
            for c in range(4):
                # 시체가 있었으면 시체 카운트 -1
                if SMELL_MAP[r][c]:
                    SMELL_MAP[r][c] -= 1

        # 상어가 이동했던 경로의 물고기 시체를 표시
        for r, c in best_travel_path:
            if tmp_map[r][c]:
                tmp_map[r][c] = []

                # 2번 돌아야 냄새 없어짐
                SMELL_MAP[r][c] = 2

        # 4. 복제 마법 캐스팅 완료
        for r in range(4):
            for c in range(4):
                FISH_MAP[r][c].extend(tmp_map[r][c])

    ret = 0
    for row in range(4):
        for col in range(4):
            ret += len(FISH_MAP[row][col])

    return ret


print(solution())
