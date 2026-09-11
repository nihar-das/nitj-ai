def partition(nums, start, end):
    pivot = nums[end]
    i = start - 1

    for j in range(start, end):
        if nums[j] < pivot:
            i += 1
            # swap i and j elems
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp

    correct_pos = i + 1
    # swam pivot with correct position
    temp = nums[end]
    nums[end] = nums[correct_pos]
    nums[correct_pos] = temp
    return correct_pos


def quicksort(nums, start, end):
    # base case
    if start >= end:
        return
    correct_pos = partition(nums, start, end)
    quicksort(nums, start, correct_pos - 1)
    quicksort(nums, correct_pos + 1, end)


ip = [5, 2, 9, 1, 7, 6, 3]
quicksort(ip, 0, len(ip) - 1)
print(ip)
