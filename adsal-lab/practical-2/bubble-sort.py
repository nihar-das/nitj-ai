def take_inputs():
    try:
        nums = input("Enter space separated values:").strip()

        if not nums:
            return None

        nums = [float(item) for item in nums.split()]

    except ValueError:
        return None

    return nums


def bubble_sort(nums):
    nums_len = len(nums)

    for i in range(nums_len - 1):
        for j in range(1, nums_len - i):
            if nums[j] < nums[j - 1]:
                temp = nums[j]
                nums[j] = nums[j - 1]
                nums[j - 1] = temp
    return nums


def main():
    nums = take_inputs()
    if nums is None:
        print("Invalid inputs")
        return
    res = bubble_sort(nums)
    print(res)


if __name__ == "__main__":
    main()
