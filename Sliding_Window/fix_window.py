def sliding_window(arr: list[int], window_size: int) -> int:
    window = arr[0:window_size]
    res = sum(window)
    for right in range(window_size, len(arr)):
        window.pop(0)
        window.append(arr[right])
        res = max(res, sum(window))
    return res

def sliding_window_second(arr: list[int], window_size: int) -> int:
    largest = sum(arr[:window_size])
    window_sum = largest
    for right in range(window_size, len(arr)):
        left = right - window_size
        window_sum -= arr[left]
        window_sum += arr[right]
        largest = max(largest, window_sum)
    return largest

if __name__ == "__main__":
    print(sliding_window([1,3,2,6, -1, 4, 1, 8, 2], 3))
    print(sliding_window_second([1,3,2,6, -1, 4, 1, 8, 2], 3))