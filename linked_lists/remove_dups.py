# Write code to remove duplicates from an unsorted linked list. How would you solve this problem if a temporary buffer is not allowed?

# Time: O(n), Space: O(n)


def removeDuplicates(head):
    if head is None:
        return head
    items = set()
    items.add(head.val)
    current = head
    while current and current.next:
        if current.next.val in items:
            current.next = current.next.next
        else:
            items.add(current.next.val)
            current = current.next
    return head
