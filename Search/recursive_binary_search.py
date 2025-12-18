def recursive_binary_search(arr: list[int], target: int) -> bool:
    if len(arr) == 0:
        return False
    else:
        mid = len(arr) // 2
        if arr[mid] == target:
            return  True
        else:
            if arr[mid] < target:
                return recursive_binary_search(arr[mid+1:], target)
            else:
                return recursive_binary_search(arr[:mid], target)


if __name__ == "__main__":
    print(recursive_binary_search([1,2,3,4,5,6,7,8,9,10], 10))