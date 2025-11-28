from merge_lists import ListNode, merge_two_lists_with_dummy, merge_two_lists_without_dummy

def list_to_array(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

def array_to_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

list1 = array_to_list([1, 2, 4])
list2 = array_to_list([1, 3, 4])
merged_with_dummy = merge_two_lists_with_dummy(list1, list2)
merged_without_dummy = merge_two_lists_without_dummy(array_to_list([1, 2, 4]), array_to_list([1, 3, 4]))
assert list_to_array(merged_with_dummy) == [1, 1, 2, 3, 4, 4]
assert list_to_array(merged_without_dummy) == [1, 1, 2, 3, 4, 4]

list1 = array_to_list([1, 2, 3])
list2 = None
merged_with_dummy = merge_two_lists_with_dummy(list1, list2)
merged_without_dummy = merge_two_lists_without_dummy(array_to_list([1, 2, 3]), None)
assert list_to_array(merged_with_dummy) == [1, 2, 3]
assert list_to_array(merged_without_dummy) == [1, 2, 3]

assert merge_two_lists_with_dummy(None, None) is None
assert merge_two_lists_without_dummy(None, None) is None

list1 = array_to_list([1, 3, 5, 7])
list2 = array_to_list([2, 4, 6])
merged_with_dummy = merge_two_lists_with_dummy(list1, list2)
merged_without_dummy = merge_two_lists_without_dummy(array_to_list([1, 3, 5, 7]), array_to_list([2, 4, 6]))
assert list_to_array(merged_with_dummy) == [1, 2, 3, 4, 5, 6, 7]
assert list_to_array(merged_without_dummy) == [1, 2, 3, 4, 5, 6, 7]

list1 = array_to_list([2, 2, 2])
list2 = array_to_list([2, 2])
merged_with_dummy = merge_two_lists_with_dummy(list1, list2)
merged_without_dummy = merge_two_lists_without_dummy(array_to_list([2, 2, 2]), array_to_list([2, 2]))
assert list_to_array(merged_with_dummy) == [2, 2, 2, 2, 2]
assert list_to_array(merged_without_dummy) == [2, 2, 2, 2, 2]

list1 = array_to_list([-5, -3, 0])
list2 = array_to_list([-4, -2, 1])
merged_with_dummy = merge_two_lists_with_dummy(list1, list2)
merged_without_dummy = merge_two_lists_without_dummy(array_to_list([-5, -3, 0]), array_to_list([-4, -2, 1]))
assert list_to_array(merged_with_dummy) == [-5, -4, -3, -2, 0, 1]
assert list_to_array(merged_without_dummy) == [-5, -4, -3, -2, 0, 1]

list1 = array_to_list(list(range(0, 10000, 2)))
list2 = array_to_list(list(range(1, 10000, 2)))
merged_with_dummy = merge_two_lists_with_dummy(list1, list2)
assert list_to_array(merged_with_dummy) == list(range(0, 10000))