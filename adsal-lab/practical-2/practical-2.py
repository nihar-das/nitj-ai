from copy import deepcopy


def bubble_sort(nums):
    nums_c = deepcopy(nums)
    nums_len = len(nums_c)

    for i in range(nums_len - 1):
        for j in range(1, nums_len - i):
            if nums_c[j] < nums_c[j - 1]:
                temp = nums_c[j]
                nums_c[j] = nums_c[j - 1]
                nums_c[j - 1] = temp
    return nums_c


def insertion_sort(nums):
    nums_c = deepcopy(nums)
    nums_len = len(nums_c)

    for i in range(1, nums_len):
        for j in range(i, 0, -1):
            if nums_c[j] < nums_c[j - 1]:
                temp = nums_c[j]
                nums_c[j] = nums_c[j - 1]
                nums_c[j - 1] = temp
            else:
                continue
    return nums_c


def selection_sort(nums):
    nums_c = deepcopy(nums)
    nums_len = len(nums_c)

    pos = -1
    for _ in range(nums_len - 1):
        # find min
        min_pos = None
        for j in range(pos + 1, nums_len):
            if min_pos is None:
                min_pos = j
            elif nums_c[j] < nums_c[min_pos]:
                min_pos = j

        pos += 1
        temp = nums_c[min_pos]
        nums_c[min_pos] = nums_c[pos]
        nums_c[pos] = temp
    return nums_c


def main():
    ip = [5, 2, 9, 1, 7, 6, 3]
    print(f"Bubble sort: {bubble_sort(ip)}")
    print(f"Insertion sort: {insertion_sort(ip)}")
    print(f"Selection sort: {selection_sort(ip)}")


if __name__ == "__main__":
    main()
