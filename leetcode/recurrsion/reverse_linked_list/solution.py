# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


def reverse_list(head):
    if head is None or head.next is None:
        return head

    p = reverse_list(head.next)
    head.next.next = head
    head.next = None
    return p
