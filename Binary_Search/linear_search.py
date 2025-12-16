def linear_search(arr: list[int], target:int) -> int:
    for i, num in enumerate(arr):
        if num == target:
            return i
    return -1


if __name__ == "__main__":
    print(linear_search([1,2,3,4,5], 3))