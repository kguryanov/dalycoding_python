"""
An XOR linked list is a more memory efficient doubly linked list. Instead of each node holding next and prev fields, it
holds a field named both, which is an XOR of the next node and the previous node.
Implement an XOR linked list; it has an add(element) which adds the element to the end,
and a get(index) which returns the node at index.

If using a language that has no pointers (such as Python), you can assume you have access
to get_pointer and dereference_pointer functions that converts between nodes and memory addresses.
"""
import logging

import _ctypes


class Node:
    def __init__(self, val: 'Node'):
        self.val = val
        self.both = id(self) ^ id(None)

    def add(self, node: 'Node'):
        next_node = _ctypes.PyObj_FromPtr(self.both ^ id(self))
        if next_node is not None:
            next_node.add(node)
        else:
            node.both = node.both ^ id(self)
            self.both = id(self) ^ id(node)

    def first(self):
        return _ctypes.PyObj_FromPtr(self.both ^ id(None))


def main():
    log_format = '%(levelname)s: %(asctime)s - %(message)s'
    logging.basicConfig(level=logging.DEBUG, format=log_format)
    logger = logging.getLogger()


if __name__ == '__main__':
    # main()
    child = Node('child')
    current = Node('curret')
    root = Node('root')

    print(f'root: {id(root)}')
    print(f'Child: {id(child)}')
    print(f'None: {id(None)}')

    print(f'root\'s links: {root.both}')
    print(f'child\'s links: {child.both}')
    root.add(child)
    print(f'root\'s links new: {root.both}')
    print(f'child\'s links new: {child.both}')
    print(f'child\'s parent: {child.both ^ id(None)}')
    print(f'root\'s child value: {root.first().val}')
