from typing import List


# O(nLogn) time | O(1) space
def non_constructible_change(coins: List[int]) -> int:
    coins.sort()
    change = 0

    for coin in coins:
        if coin > change + 1:
            return change + 1

        change += coin

    return change + 1


if __name__ == '__main__':
    input = [5, 7, 1, 1, 2, 3, 22]
    expected = 20
    res = non_constructible_change(input)
    print(expected == res)
