from typing import List

# O(n^2) time | O(n) space
def three_number_sum(array: List[int], target_sum: int) -> List[int]:
    array.sort()
    triplets = []

    for i in range(len(array) - 2):
        left_idx = i + 1
        right_idx = len(array) - 1

        while left_idx < right_idx:
            c = array[i]
            l = array[left_idx]
            r = array[right_idx]
            current_sum = c + l + r
            if current_sum == target_sum:
                triplets.append([c, l, r])
                left_idx += 1
                right_idx -=1
            if current_sum > target_sum:
                right_idx -=1
            if current_sum < target_sum:
                left_idx +=1

    return triplets


if __name__ == '__main__':
    res = three_number_sum([12, 3, 1, 2, -6, 5, -8, 6], 0)
    expected = [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]
    print(res == expected)
