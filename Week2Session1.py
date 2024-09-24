class ListNode:
    def __init__(self, val=0, next=None):
     self.val = val
     self.next = next

"""
Problem 1: https://leetcode.com/problems/odd-even-linked-list/
Problem 2: https://leetcode.com/problems/swap-nodes-in-pairs/
Problem 3: https://leetcode.com/problems/rotate-list/
Problem 4: https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
"""

# PROBLEM 1
"""
1. Could the input list be empty?
2. Linked list - likely, two pointers, likely
3. Since we can't use extra memory and must write an algorithm that uses linear time, the ideal solution would just be an iteration through the linked list. Keep track of two pointers: the odd list and the even list. After the traversal, set the next pointer last node of the odd list to be the head of the even list.
4.
check for edge cases, like when the input node is None or only contains one node

initialize the first node of the odd list
initialize the first node of the even list
initialize the index of the first node
loop through the linked list
    check if the index is odd or even
    if odd, append the node to the odd list
    if even, append the node to the even list
    increment the pointer

set the next pointer of the odd pointer to head node of the even list
return the head of the odd list
5. See code below.
6. I think that overall, this implementation is very efficient. It loops through the linked list only once and doens't use any extra space.
"""

def oddEvenList(head):
  if not head or not head.next:
    return head

  odd = head
  tmp_odd = odd # reference to the first node in the odd sequence
  even = head.next
  curr = head.next.next
  tmp_even = even # reference to the first node in the even sequence
  idx = 3
  while curr:
    if idx % 2 != 0: # odd index
        odd.next = curr
        odd = odd.next
    else:
        even.next = curr
        even = even.next
    # print(odd.val, even.val)
    curr = curr.next
    idx += 1

  # avoid cycles
  odd.next = None
  even.next = None

  odd.next = tmp_even
  return tmp_odd

# PROBLEM 2
"""
1. Could the head node be empty? Is there always going to be an even, or odd number of nodes in the list?
2. Linked list - likely, two pointers - likely
3. Use two pointers, prev and curr. For every iteration, temporarily store the node after curr in a temporary variable and set the next pointer of the curr node to prev and the next node of prev to the next node after curr. Do a one time iteration across the linked list.
4. 
initialize a prev and a curr node
while the curr and the node after curr is valid:
    set the temporary node to be the next node of the next node of curr
    set the next node of the prev node to be the next node of the curr node
    set the next node of the next node of curr to be curr itself
    set the next node of the curr node to the the temporary node

    set the prev node to be the curr node
    set curr to be its next node
return the head
5. See tode below.
6. I think that overall, the code is very efficient. Aside from the dummy node that I created at the start, there isn't additional memory being used. Moreover, I only iterate over the linked list once, so that would be O(n) time complexity.
"""

def swapPairs(head):
    if not head:
        return None

    curr = head
    ref = prev = ListNode()
    prev.next = head

    while curr and curr.next:
        tmp = curr.next.next
        prev.next = curr.next
        curr.next.next = curr
        curr.next = tmp

        prev = curr
        curr = curr.next
    return ref.next
    
# PROBLEM 3
"""
1. Can the values of the nodes be changed or only the nodes themselves?
2. Linked list - likely, two pointers - neutral
3. Make the linked list a cycle first. Set the next node of the tail to the head. From there, find the new tail and new head of the list. Break the cycle before returning the new head
4. 
check for edge cases: empty list or only 1 node

loop through the linked list, finding the tail, and setting the next pointer of the tail to the head, creating a cycle
NOTE: keep track of the number of nodes in the list using a variable called count

initialize a cvariable called new_tail
loop all the way to the index count - k % count - 1
    update the new tail
update the new_head to the next pointer of the new_tail node

break the cycle

return the new_head node

5. See the code below.
6. I think oveall, this code is very efficient. The time complexity is O(n), since I'm at most iterating over the linked list, and the space complexity would be O(1), since I'm not allocating additional memory for data structures.

Actually, my initial approach involved using a dictionary to map the position of the node to the node and then to manually modify the values of the nodes. This wouldn't be as efficient, since I would have to allocate additional memory to accomodate for those data structures.
"""

def rotateRight(head, k):
    # base cases
    if not head:
        return None
    if not head.next:
        return head

    old_tail = head
    count = 1
    while old_tail.next:
        old_tail = old_tail.next
        count += 1
    old_tail.next = head # create the cycle

    new_tail = head
    for i in range(count - (k % count) - 1):
        new_tail = new_tail.next
    new_head = new_tail.next

    new_tail.next = None # break the cycle

    return new_head

# PROBLEM 4
"""
1. Could the list be empty? Will the values only be integers?
2. Linked list - likely, two pointers - neutral
3. First, get the number of nodes in the list and set the variable to count. Then, loop through the first (count - n) nodes of the list. Set the next pointe of the that (total - n)th node to the next next node.
4.
create a dummy node

initialize a cur node to the head
initialize the total number of nodes
iterate through the linked list
    increment the total count
    increment the linked list pointer

set the curr pointer to the dummy node
loop through the first (total - n) nodes
    increment the curr pointer

adjust the pointers accordingly
- if the next 2 nodes in front of curr are valid, set the next pointer of curr to the 2nd node away
- otherwise, set the next pointer to None

return the node after the dummy node

5. See code below.
6. 
"""

def removeNthFromEnd(head, n):
    dummy = ListNode(0, head)

    curr = head
    total = 0
    while curr:
        total += 1
        curr = curr.next

    curr = dummy
    count = 0
    while count < total - n:
        curr = curr.next
        count += 1

    if curr.next and curr.next.next:
        curr.next = curr.next.next
    else:
        curr.next = None

    return dummy.next