from typing import List


# O(n) time | O(1) space
def is_valid_subsequence_1(array: List[int], sequence: List[int]) -> bool:
    seq_idx = 0
    arr_idx = 0
    while seq_idx < len(sequence) and arr_idx < len(array):
        if sequence[seq_idx] == array[arr_idx]:
            seq_idx += 1
            arr_idx += 1
        else:
            arr_idx += 1
    return seq_idx == len(sequence)


# O(n) time | O(1) space
def is_valid_subsequence_2(array: List[int], sequence: List[int]) -> bool:
    seq_idx = 0

    for num in array:
        if seq_idx == len(sequence):
            return True

        if sequence[seq_idx] == num:
            seq_idx += 1

    return seq_idx == len(sequence)


if __name__ == '__main__':
    res = is_valid_subsequence_2([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10])
    print(res)
