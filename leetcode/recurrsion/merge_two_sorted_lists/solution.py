# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def merge_two_lists(list1, list2):
    if list1 is None:
        return list2

    elif list2 is None:
        return list1

    elif list1.val < list2.val:
        list1.next = merge_two_lists(list1.next, list2)
        return list1

    else:
        list2.next = merge_two_lists(list1, list2.next)
        return list2
