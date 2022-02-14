from cgitb import small
from typing import List


def sorted_squared_array(array: List[int]) -> List[int]:
    squared = [0 for _ in array]
    smaller_idx = 0
    larger_idx = len(array) - 1

    for idx in reversed(range(len(array))):
        smaller = array[smaller_idx]
        larger = array[larger_idx]

        if abs(smaller) > abs(larger):
            squared[idx] = smaller * smaller
            smaller_idx += 1
        else:
            squared[idx] = larger * larger
            larger_idx -= 1

    return squared


if __name__ == '__main__':
    input = [1, 2, 3, 5, 6, 8, 9]
    expected = [1, 4, 9, 25, 36, 64, 81]
    res = sorted_squared_array(input)
    print(res)
    print(expected == res)
