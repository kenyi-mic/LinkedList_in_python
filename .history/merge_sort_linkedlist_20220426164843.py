from re import L
from linkedList import LinkedList


def merge_sort(linkedList):
    if linkedList.size() == 1:
        return linkedList

    elif linkedList.head is None:
        return linkedList

    left_half, right_half = split(linkedList)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)


def split(linkedList):
    """
    Davide the unsorted list at midpoint into sublists
    """
    if linkedList == None or linkedList.head == None:
        left_half = linkedList
        right_half = None

        return left_half, right_half

    else:
        size = linkedList.size()
        mid = size//2

        mid_node = linkedList.node_at_index(mid-1)

        left_half = linkedList
        right_half = LinkedList()
        right_half.head = mid_node.next_node
        mid_node.next = None
