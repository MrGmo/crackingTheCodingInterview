# Implement an algorithm to find the kth to last element of a singly linked list.

# Time: O(n), Space: O(1)

def return_kth_node(head, k):
    fast = head
    for i in range(k):
        if fast:
            fast = fast.next
        else:
            return None

    slow = head

    while fast:
        fast = fast.next
        slow = slow.next
    return slow
