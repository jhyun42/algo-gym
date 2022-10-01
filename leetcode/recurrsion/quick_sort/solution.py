test_01 = [1, 5, 3, 2, 8, 7, 6, 4]


def quick_sort(lst):
    n = len(lst)

    def q_sort(lst, lo, hi):
        if lo < hi:
            p = partition(lst, lo, hi)
            q_sort(lst, lo, p - 1)
            q_sort(lst, p + 1, hi)

    def partition(lst, lo, hi):
        pivot = lst[hi]
        i = lo
        for j in range(lo, hi):
            if lst[j] < pivot:
                lst[i], lst[j] = lst[j], lst[i]
                i += 1
        lst[i], lst[hi] = lst[hi], lst[i]

        return i

    q_sort(lst, 0, n - 1)

    return lst


ans = quick_sort(test_01)
print(ans)
