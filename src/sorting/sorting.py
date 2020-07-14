# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    if len(arrA) == 0:
        return arrB

    if len(arrB) == 0:
        return arrA

    result = []
    index_left = index_right = 0

    # Your code here
    while len(result) < len(arrA) + len(arrB):
        if arrA[index_left] <= arrB[index_right]:
            result.append(arrA[index_left])
            index_left += 1
        else:
            result.append(arrB[index_right])
            index_right += 1

        if index_right == len(arrB):
            result += arrA[index_left:]
            break

        if index_left == len(arrA):
            result += arrB[index_right:]
            break

    return result

# TO-DO: implement the Merge Sort function below recursively


def merge_sort(arr):
    # Your code here
    if len(arr) < 2:
        return arr

    midpoint = len(arr) // 2

    return merge(arrA=merge_sort(arr[:midpoint]), arrB=merge_sort(arr[midpoint:]))


my_arr = [3, 2, 5, 6, 2, 9, 2, 1, 8, 9]
print(merge_sort(my_arr))

# STRETCH: implement the recursive logic for merge sort in a way that doesn't
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists
# or data structures; it can only re-use the memory it was given as input


def merge_in_place(arr, start, mid, end):
    # Your code here
    pass


def merge_sort_in_place(arr, l, r):
    # Your code here
    pass
