import sys

inputs = sys.stdin.readline

N = int(inputs())
A = list(map(int, inputs().split()))
B, C = list(map(int, inputs().split()))


def solution(n, a: list, b, c):
    num_supervisors = 0
    for num_students_to_supervise in a:

        # Main supervisor
        num_students_to_supervise = num_students_to_supervise - b
        num_supervisors += 1

        # Sub-supervisor
        if num_students_to_supervise > 0:
            num_sub_super = int(num_students_to_supervise / c)
            if (num_students_to_supervise % c) != 0:
                num_sub_super += 1

            num_supervisors += num_sub_super

    return num_supervisors


ret = solution(N, A, B, C)
print(ret)
