# Selection Sort (short)
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = min(range(i, len(arr)), key=arr.__getitem__)
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Merge Sort (short)
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left, right = merge_sort(arr[:mid]), merge_sort(arr[mid:])
    merged = []
    while left and right:
        merged.append(left.pop(0) if left[0] < right[0] else right.pop(0))
    return merged + left + right

# Example
lst1 = [64, 25, 12, 22, 11]
lst2 = [38, 27, 43, 3, 9, 82, 10]

print("Selection Sort:", selection_sort(lst1.copy()))
print("Merge Sort:", merge_sort(lst2))
