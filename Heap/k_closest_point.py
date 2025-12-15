from heapq import heappop, heappush
def k_closest(points: list[list[int]], k: int) -> list[list[int]]:
    heap: list[tuple[int, list[int]]] = []
    for point in points:
        heappush(heap, (point[0] ** 2 + point[1] ** 2, point))

    res=[]
    for _ in range(k):
        _, pt = heappop(heap)
        res.append(pt)
    return res

if __name__ == "__main__":
    print(k_closest([[1,3],[-2,2],[1,4],[4,3],[-2,3],[1,1],[-2,-2]], 3))