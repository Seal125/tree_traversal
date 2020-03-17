from exercises import Node, insert_left
from typing import List

def test_Node():
    t = Node(1)
    assert t.value == 1
    t.left = Node(2)
    assert t.left.value == 2
    t.right = Node(3)
    assert t.right.value == 3

def test_insert_left():
    t = Node(1)
    insert_left(t, 2)
    assert t.left.value == 2
    insert_left(t, 3)
    assert t.left.value == 3
    assert t.left.left.value == 2