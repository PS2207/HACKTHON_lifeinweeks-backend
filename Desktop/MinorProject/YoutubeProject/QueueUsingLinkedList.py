#Stack implementation Using LinkedList
'''
push()- Inserting node in the begining
pop() deleting node from beginning

#Queue using Linked List
enque(Q,x)- head->[x| ]  
enque(Q,y)- head->[y| ] ->[x| ]   
enque(Q,z)- head->[z| ]->[y| ]->[x| ]

deque() 
'''
'''
findMiddle(l.head):
    p=l.head
    q=l.head
    while(q.next != Null):
        p=p.next  #by 1 step
        q=q.next.next   #by 2 step
    return p   
''' 
#linked list implementation to findmiddle
def findMiddle(head):
    if head is None:  # Handle empty list case
        return None
    
    slow = head
    fast = head
    
    while fast and fast.next:  # Check both fast and fast.next
        slow = slow.next  # Move slow by 1 step
        fast = fast.next.next  # Move fast by 2 steps
    
    return slow  # slow will be at the middle
Searching in circular linked list
Insertion in circular linked list
Deletion in circular linked list

Doubly linked list
head -> [pre | key | next] <==> [pre | key | next] <==> [pre | key | next]
600 ->  [NULL | 50 | next] <==> [pre | 55 | next] <==> [pre | 66 | NULL]

prev: Location to the previous node
next: Location to the next node
key:information


def addNode(head, B):
     new_node= DLN(B)
     if not head:
         return new_node
     current=head
     while current.next:
         current.next
     current.next = new_node    
























