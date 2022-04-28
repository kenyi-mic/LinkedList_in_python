from re import L
from linkedList import LinkedList

linkedlist = LinkedList()


def merge_sort(linkedlist):
    if linkedlist.size() == 1:
        return linkedlist

    elif linkedlist.head is None:
        return linkedlist

    left_half, right_half = split(linkedlist)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)


def split(linkedlist):
    """
    Davide the unsorted list at midpoint into sublists
    """
    if linkedlist == None or linkedlist.head == None:
        left_half = linkedlist
        right_half = None

        return left_half, right_half

    else:
        size = linkedlist.size()
        mid = size//2
