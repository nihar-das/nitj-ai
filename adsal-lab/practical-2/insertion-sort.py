def take_inputs():
    try:
        nums = input("Enter space separated values:").strip()

        if not nums:
            return None

        nums = [float(item) for item in nums.split()]

    except ValueError:
        return None

    return nums


def insertion_sort(nums):
    nums_len = len(nums)

    for i in range(1, nums_len):
        for j in range(i, 0, -1):
            if nums[j] < nums[j - 1]:
                temp = nums[j]
                nums[j] = nums[j - 1]
                nums[j - 1] = temp
            else:
                continue
    return nums


def main():
    nums = take_inputs()
    if nums is None:
        print("Invalid inputs")
        return
    res = insertion_sort(nums)
    print(res)


if __name__ == "__main__":
    main()
