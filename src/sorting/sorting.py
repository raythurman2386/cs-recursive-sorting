from random import shuffle

# TO-DO: complete the helper function below to merge 2 sorted arrays
my_arr = [num for num in range(1, 26)]
shuffle(my_arr)
print("Starting Array: ", my_arr)


def merge(left, right):
    # If the left array is 0 return the right array
    if len(left) == 0:
        return right

    # If the right array is 0 return the left array
    if len(right) == 0:
        return left

    # instantiate the returning array, and the indexes
    result = []
    index_left = index_right = 0

    # Your code here
    # go through both arrays till all elements
    # make it into the result array
    while len(result) < len(left) + len(right):
        # Decide which element needs to be sorted
        # add that item to the array
        if left[index_left] <= right[index_right]:
            result.append(left[index_left])
            index_left += 1
        else:
            result.append(right[index_right])
            index_right += 1

        # If we reach the end of the array, add
        # remaining elements to the results and
        # break out of the loop
        if index_right == len(right):
            result += left[index_left:]
            break

        if index_left == len(left):
            result += right[index_right:]
            break

    return result

# TO-DO: implement the Merge Sort function below recursively


def merge_sort(arr):
    # Your code here
    if len(arr) < 2:
        return arr

    # Find the midpoint of the array
    midpoint = len(arr) // 2

    # recursively run the helper function merge()
    # split the arrays into left and right depending on the midpoint
    return merge(left=merge_sort(arr[:midpoint]), right=merge_sort(arr[midpoint:]))


print("Ending Array: ", merge_sort(my_arr))

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
