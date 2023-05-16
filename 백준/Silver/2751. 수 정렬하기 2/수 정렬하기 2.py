# Heap Sort
import heapq
import sys

n = int(sys.stdin.readline())
nlist = []

for i in range(n):
    nlist.append(int(int(sys.stdin.readline())))

def heap_sort(nlist):
    heap = []
    for n in nlist:
        heapq.heappush(heap, n)
    sorted_nums = []
    while heap:
        sorted_nums.append(heapq.heappop(heap))
    return sorted_nums

nlist = heap_sort(nlist)

for n in nlist:
    print(n)