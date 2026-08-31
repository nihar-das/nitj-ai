def linear_search(nums, key):
    i = 0
    while i < len(nums):
        if nums[i] == key:
            print(f"Key found")
            break
        i += 1

    if i == len(nums):
        print("Key not found")


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


def get_fk(n):
    fib_seq = [1, 1]
    a, b = 1, 1
    while True:
        fk = a + b
        fib_seq.append(fk)
        if fk >= n:
            # return fk, b, a
            return fib_seq, len(fib_seq) - 1
        a = b
        b = fk


def fibonacci_search(nums, key):
    sort_arr(nums)
    # fk, fk_1, fk_2 = get_fk(len(nums))
    fib_seq, L = get_fk(len(nums))
    fk_2 = fib_seq[L]
    offset = -1

    while L >= 0:
        idx = offset + fk_2

        if nums[idx] == key:
            print("Key found")
            return
        elif nums[idx] < key:
            offset = idx

            fk_2 = fib_seq[L - 1]
            L -= 1
            # fk = fk_1
            # fk_1 = fk_2
            # fk_2 = fk - fk_1
        else:
            fk_2 = fib_seq[L - 2]
            L -= 2
            # fk = fk_2
            # fk_1 = fk_1 - fk_2
            # fk_2 = fk_2 - fk_1

    if nums[idx + 1] == key:
        print("Key found")
    else:
        print("Key not found")


def test():
    nums = [2, 2, 12, 0, -1, 2, 5, 336]
    # nums = [3, 5, 7, 10]
    key = 336
    print("Linear search")
    linear_search(nums, key)
    # print("Binary search")
    # binary_search(nums, key)
    # print("Fibonacci search")
    # fibonacci_search(nums, key)


test()
