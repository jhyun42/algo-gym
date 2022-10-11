N = int(input())

for test_case in range(N):
    input_list = list(map(int, input().split()))
    ret = 0
    for num in input_list:
        if num % 2 == 1:
            ret += num
    print('#{} {}'.format(test_case + 1, ret))
