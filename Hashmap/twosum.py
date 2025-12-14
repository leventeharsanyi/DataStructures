def twosum(arr:list[int], target: int) -> tuple[int, int] | None:
    seen = dict()
    for i, num in enumerate(arr):
        difference = target - num
        if difference in seen:
            return seen[difference], i
        seen[num] = i
    return None

if __name__ == "__main__":
    print(twosum([0,1,2,3,4,5,6,7,8,9,10], 16))