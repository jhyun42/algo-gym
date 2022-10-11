N = int(input())

for test_case in range(1, N + 1):
    input_list = list(map(int, input().split()))
    ret = round(sum(input_list) / len(input_list))
    print('#{} {}'.format(test_case, ret))
