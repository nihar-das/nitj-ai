def take_inputs():
    try:
        nums = input("Enter space separated values:").strip()

        if not nums:
            return None

        nums = [float(item) for item in nums.split()]

    except ValueError:
        return None

    return nums


def selection_sort(nums):
    nums_len = len(nums)

    pos = -1
    for _ in range(nums_len - 1):
        # find min
        min_pos = None
        for j in range(pos + 1, nums_len):
            if min_pos is None:
                min_pos = j
            elif nums[j] < nums[min_pos]:
                min_pos = j

        pos += 1
        temp = nums[min_pos]
        nums[min_pos] = nums[pos]
        nums[pos] = temp
    return nums


def main():
    nums = take_inputs()
    if nums is None:
        print("Invalid inputs")
        return
    res = selection_sort(nums)
    print(res)


if __name__ == "__main__":
    main()
