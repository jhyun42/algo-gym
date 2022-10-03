import sys

INPUT = sys.stdin.readline
N = int(INPUT())
A = list(map(int, INPUT().split()))
NUM_OPERATORS = list(map(int, INPUT().split()))


def solution():
    global N, A, NUM_OPERATORS

    ret_min, ret_max = float('inf'), -float('inf')

    def backtracking(result, num_idx):
        nonlocal ret_min, ret_max

        if num_idx == N - 1:
            ret_min = min(result, ret_min)
            ret_max = max(result, ret_max)

        for operator_idx in range(4):

            if NUM_OPERATORS[operator_idx]:

                NUM_OPERATORS[operator_idx] -= 1

                if operator_idx == 0:
                    backtracking(result + A[num_idx + 1], num_idx + 1)
                elif operator_idx == 1:
                    backtracking(result - A[num_idx + 1], num_idx + 1)
                elif operator_idx == 2:
                    backtracking(result * A[num_idx + 1], num_idx + 1)
                elif operator_idx == 3:
                    backtracking(int(result / A[num_idx + 1]), num_idx + 1)

                NUM_OPERATORS[operator_idx] += 1

    backtracking(A[0], 0)
    print(int(ret_max))
    print(int(ret_min))


solution()
