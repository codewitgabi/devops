def bubble_sort(arr: list) -> list:
    for i in range(0, len(arr)):
        for i in range(0, len(arr) - 1):
            if arr[i + 1] < arr[i]:
                arr[i + 1], arr[i] = arr[i], arr[i + 1]
    return arr


print(bubble_sort([5, 4, 3, 2, 1]))
