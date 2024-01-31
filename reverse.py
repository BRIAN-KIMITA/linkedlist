class node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def reverse_linked_list(head):
    prev = None
    current = head

    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    return prev


# this is the linked list here linked list: 20 -> 48 -> 79 -> 90-> 104
head = node(20, node(48, node(79, node(90, node(104)))))

# Reverse the linked list
new_head = reverse_linked_list(head)

# Print the reversed linked list
while new_head is not None:
    print(new_head.value)
    new_head = new_head.next
