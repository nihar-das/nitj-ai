def sort_arr(nums):
    # sort the array (selection sort, inplace sort)
    i = -1
    while i < len(nums) - 1:
        j = i + 1
        min_idx = j
        while j < len(nums):
            if nums[j] < nums[min_idx]:
                min_idx = j
            j += 1
        # swap min of this run with i'th index
        i += 1
        temp = nums[i]
        nums[i] = nums[min_idx]
        nums[min_idx] = temp


def binary_search(nums, key):
    sort_arr(nums)

    low, high = 0, len(nums) - 1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == key:
            print(f"Key found")
            break
        elif key < nums[mid]:
            high = mid - 1
        else:
            low = mid + 1

    if low > high:
        print("Key not found")


def take_inputs():
    try:
        nums = input("Enter space separated values:").strip()
        key = input("Enter key to search:").strip()

        if not nums or not key:
            return None, None

        nums = [float(item) for item in nums.split()]
        key = float(key)

    except ValueError:
        return None, None

    return nums, key


def main():
    nums, key = take_inputs()

    if (nums is None) or (key is None):
        print("Invalid inputs")
        return

    binary_search(nums, key)


if __name__ == "__main__":
    main()
