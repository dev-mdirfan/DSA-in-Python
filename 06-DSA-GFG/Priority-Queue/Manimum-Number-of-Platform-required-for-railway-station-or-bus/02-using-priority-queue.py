# Using Priority Queue

from heapq import *

def solution(arr, dep):
    heap = []
    comb = list(zip(arr, dep))
    count = 1
    for time in comb:
        heappush(heap, time)
        if heap[0][1] >= time[0]:
            print(heap[0][1], )
            count += 1
        else:
            heappop(heap)
    return count


if __name__ == '__main__':
    arr = [540, 580, 590, 660,900, 1080]
    dep = [550, 720, 640, 690, 1140, 1200]
    ans = solution(arr, dep)
    print(ans)



