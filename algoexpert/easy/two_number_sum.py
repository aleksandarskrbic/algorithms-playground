from typing import List


# O(n^2) time | O(1) space
def two_number_sum_1(array: List[int], target_sum: int) -> List[int]:
    for i in range(len(array) - 1):
        current = array[i]
        for j in range(i + 1, len(array)):
            next = array[j]
            if (current + next == target_sum):
                return [current, next]

    return []


# O(n) time | O(n) space
def two_number_sum_2(array: List[int], target_sum: int) -> List[int]:
    cache = {}

    for num in array:
        maybe_match = target_sum - num
        if maybe_match in cache:
            return [maybe_match, num]
        else:
            cache[num] = True

    return []


# O(nLog(n)) time | O(1) space
def two_number_sum_3(array: List[int], target_sum: int) -> List[int]:
    array.sort()

    left_idx = 0
    right_idx = len(array) - 1

    while left_idx < right_idx:
        left = array[left_idx]
        right = array[right_idx]
        result = left + right

        if result > target_sum:
            right_idx -= 1
        elif result < target_sum:
            left_idx += 1
        else:
            return [right, left]

    return []


if __name__ == '__main__':
    res = two_number_sum_2([3, 5, -4, 8, 11, 1, -1, 6], 10)
    print(res)
