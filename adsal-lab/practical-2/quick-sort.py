def take_inputs():
    try:
        nums = input("Enter space separated values:").strip()

        if not nums:
            return None

        nums = [float(item) for item in nums.split()]

    except ValueError:
        return None

    return nums


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


def main():
    nums = take_inputs()

    if nums is None:
        print("Invalid inputs")
        return

    end = len(nums) - 1

    quicksort(nums, 0, end)
    print(nums)


if __name__ == "__main__":
    main()
