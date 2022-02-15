class BST:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None


#
def find_closest_value_in_bst(tree: BST, target: int) -> int:
    current_node = tree
    previous_node = current_node

    current_diff = int('inf')
    previous_diff = int('inf')

    if target > current_node.value:
        current_node = current_node.right
    else:
        current_node = current_node.left

    while current_node != None:
        print(current_node.value)
        current_diff = abs(target - current_node.value)
        if target == current_node.value:
            return target
        elif target > current_node.value:
            current_node = current_node.right
        else:
            current_node = current_node.left

        previous_node = current_node

    return current_node.value


if __name__ == '__main__':
    root = BST(10)
    root.left = BST(5)
    root.left.left = BST(2)
    root.left.left.left = BST(1)
    root.left.right = BST(5)
    root.right = BST(15)
    root.right.left = BST(13)
    root.right.left.right = BST(14)
    root.right.right = BST(22)

    expected = 13
    res = find_closest_value_in_bst(root, 12)
    print(res)
    print(expected == res)
