def find_first_true(arr: list[bool]) -> int:
    left, right = 0, len(arr) - 1
    res = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid]:
            res = mid
            right = mid -1
        else:
            left = mid + 1
    return res

if __name__ == "__main__":
    print(find_first_true([False, False, False, True, True, True, True, True]))