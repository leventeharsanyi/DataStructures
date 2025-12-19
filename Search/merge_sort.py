def split(array: list[int]) -> tuple[list[int], list[int]]:
    """
    Divide the unsorted list at midpoint into sublists.
    Returns two sublists - left and right.

    Takes overall O(k* log n) time complexity.
    """
    midpoint = len(array) // 2
    left = array[:midpoint]
    right = array[midpoint:]
    return left, right

def merge(left: list[int], right: list[int]) -> list[int]:
    """
    Merge two sorted lists, sorting then in the process.
    Returns the sorted lists.

    Takes overall O(n) time complexity.
    """
    l = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1
        else:
            l.append(right[j])
            j += 1
    while i < len(left):
        l.append(left[i])
        i += 1
    while j < len(right):
        l.append(right[j])
        j += 1
    return l

def merge_sort(arr: list[int]) -> list[int]:
    """
    Sorts a list in ascending order.
    Returns a new sorted list.

    Divide: Find the midpoint of the list and divide into sublists.
    Conquer: Recursively sort the sublists created in the previous step.
    Combine: Merge the sorted sublists created in the previous step.

    Takes overall O(k*n * log n) time complexity.
    """
    if len(arr) <= 1:
        return arr

    left_half, right_half = split(arr)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)

if __name__ == '__main__':
    my_list = [1,5,3,8,2,4,9,7,6,0]
    print(merge_sort(my_list))