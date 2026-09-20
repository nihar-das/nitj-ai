def linear_search(nums, key):
    i = 0
    while i < len(nums):
        if nums[i] == key:
            print(f"Key found")
            break
        i += 1

    if i == len(nums):
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

    linear_search(nums, key)


if __name__ == "__main__":
    main()
