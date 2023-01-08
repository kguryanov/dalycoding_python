"""
Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
"""
import logging


class Node:
    def __init__(self, val: 'Node', left: 'Node' = None, right: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right


def serialize(node: 'Node' = None) -> str:
    if node is None:
        return ''

    return f'{node.val}|{serialize(node.left)}|{serialize(node.right)}'


def deserialize(data: str) -> 'Node':
    def helper():
        val = next(vals)
        if val == '':
            return None

        node = Node(val)
        node.left = helper()
        node.right = helper()
        return node

    vals = iter(data.split('|'))
    return helper()


def main():
    log_format = '%(levelname)s: %(asctime)s - %(message)s'
    logging.basicConfig(level=logging.DEBUG, format=log_format)
    logger = logging.getLogger()
    node = Node('root', Node('left', Node('left.left')), Node('right'))

    logger.info(serialize(node))

    logger.info(serialize(deserialize(serialize(node))))
    node2 = deserialize(serialize(node))
    assert deserialize(serialize(node)).left.left.val == 'left.left'


if __name__ == '__main__':
    main()
    # val, nodes = 'root:right:||left:|left.left:|'.split(':', maxsplit=1)
    # print(val, nodes)
    #
    # left, right = '|'.split("|", maxsplit=1)
    # print(left, right)
