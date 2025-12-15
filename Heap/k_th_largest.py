from heapq import heappop, heapify

def kth_largest(nums: list[int], k: int) -> int:
    nums = [-x for x in nums]
    heapify(nums)
    for _ in range(k-1):
        heappop(nums)
    return -heappop(nums)

if __name__ == "__main__":
    print(kth_largest([3,2,1,5,6,4], 2))