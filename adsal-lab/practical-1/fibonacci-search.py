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


def fibonacci_search(nums, key):
    sort_arr(nums)
    n = len(nums)

    fk_2, fk_1 = 0, 1
    fk = fk_1 + fk_2

    # find smallest fibonacci number >= length of nums
    while fk < n:
        fk_2, fk_1 = fk_1, fk
        fk = fk_1 + fk_2

    offset = -1

    while fk > 1:
        idx = min(offset + fk_2, n - 1)

        if nums[idx] == key:
            print("Key found")
            return
        elif nums[idx] < key:
            offset = idx
            fk, fk_1, fk_2 = fk_1, fk_2, fk_1 - fk_2
        else:
            fk, fk_1, fk_2 = fk_2, fk_1 - fk_2, 2 * fk_2 - fk_1

    candidate = offset + 1
    if fk_1 and candidate < n and nums[candidate] == key:
        print("Key found")
    else:
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

    fibonacci_search(nums, key)


if __name__ == "__main__":
    main()
