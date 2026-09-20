def combine(left_list, right_list):
    combined_list = []
    i = j = 0

    while (i < len(left_list)) and (j < len(right_list)):
        if left_list[i] <= right_list[j]:
            combined_list.append(left_list[i])
            i += 1
        elif left_list[i] > right_list[j]:
            combined_list.append(right_list[j])
            j += 1

    while i < len(left_list):
        combined_list.append(left_list[i])
        i += 1

    while j < len(right_list):
        combined_list.append(right_list[j])
        j += 1
    return combined_list


def merge_sort(nums, start, end):
    if start == end:
        return [nums[start]]

    mid = (start + end) // 2

    # dive into 2 solved sub-problems
    left_list = merge_sort(nums, start, mid)
    right_list = merge_sort(nums, mid + 1, end)

    # merge sub-problems
    return combine(left_list, right_list)


def take_inputs():
    try:
        nums = input("Enter space separated values:").strip()

        if not nums:
            return None

        nums = [float(item) for item in nums.split()]

    except ValueError:
        return None

    return nums


def main():
    nums = take_inputs()

    if nums is None:
        print("Invalid inputs")
        return

    end = len(nums) - 1

    res = merge_sort(nums, 0, end)
    print(res)


if __name__ == "__main__":
    main()
