import sys


def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            while mid > 0:
                if array[mid - 1] == target:
                    mid -= 1
                else:
                    break
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None


n = int(sys.stdin.readline())
n_list = list(map(int, sys.stdin.readline().split()))
n_list.sort()

m = int(sys.stdin.readline())
m_list = list(map(int, sys.stdin.readline().split()))

n_dict = {}

for i in range(m):
    target = m_list[i]
    if target not in n_dict:
        idx = binary_search(n_list, target, 0, len(n_list)-1)
        if idx is not None:
            count = 0
            for i in range(idx, len(n_list)):
                if n_list[i] == target:
                    count += 1
                else:
                    break
        else:
            count = 0
        n_dict[target] = count

print(' '.join(str(n_dict[x]) for x in m_list))

