import heapq

def heapsort(itr: list[int]) -> list[int]:
    heap = []
    for value in itr:
        heapq.heappush(heap, value)
    return [heapq.heappop(heap) for _ in range(len(itr))]

def create_heap(itr: list[int]) -> list[int]:
    heap = itr
    heapq.heapify(heap)
    return heap

def get_k_smallest(values, k, key):
    return heapq.nsmallest(k, values, key=key)

def get_k_largest(values, k, key):
    return heapq.nlargest(k, values, key=key)

def max_heap(itr: list[int]) -> list[int]:
    heap = [-x for x in itr]
    heapq.heapify(heap)
    return [-heapq.heappop(heap) for _ in range(len(heap))]

if __name__ == "__main__":
    trees = [
        {"id": 1, "age": 12},
        {"id": 2, "age": 45},
        {"id": 3, "age": 8},
        {"id": 4, "age": 30},
    ]
    print(heapsort([3,7,9,10,2,1,5,6,4]))
    print(create_heap([8,3,7,9,10,2,1,5,6,4]))
    print(get_k_smallest(trees, 2, key=lambda x: x["age"]))
    print(get_k_largest(trees, 2, key=lambda x: x["age"]))
    print(max_heap([3,7,9,10,2,1,5,6,4]))