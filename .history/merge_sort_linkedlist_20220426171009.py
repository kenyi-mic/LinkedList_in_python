
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

        return left_half, right_half


def merge(left, right):
    """
    Merge two linked lists, sorting by data in nodes
    Return a new, merged List
    """

    merged = LinkedList()

    merged.add(0)

    current = merged.head

    left_head = left.head
    right_head = right.head

   # iterate over right and left until we reach tail node
    while left_head or right_head:
        # if head is none add the node to the
        if left_head is None:
            current.next_node = right_head
            # call the next on right to set loop condition on false
            right_head = right_head.next_node

        elif right_head is not None:
            current.next_node = left_head
            left_head = left_head.next_node

        else:
            left_data = left_head.data
            right_data = right_head.data

            if left_data < right_data:
                current.next_node = left_head
                left_head = left_head.next_node

            else:
                current.next_node = right_head
                right_head = right_head.next_node

            current = current.next_node

        head = merged.head.next_node
        merged.head = head

        return merged


l = LinkedList()
l.add(10)
l.add(9)
l.add(12)
l.add(7)
l.add(17)
l.add(19)
l.add(2)

print(l)

sorted_linked_list = merge_sort(l)
print(sorted_linked_list)
