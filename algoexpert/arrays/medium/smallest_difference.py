from typing import List

def smallest_difference(array_one: List[int], array_two: List[int]) -> List[int]:
    array_one.sort()
    array_two.sort()
    return []


if __name__ == '__main__':
    res = smallest_difference([-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17])
    expected = [28, 26]
    print(res == expected)