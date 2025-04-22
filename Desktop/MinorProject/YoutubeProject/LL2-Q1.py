class LinkedListNode:
    def __init__(self, data):
        self.data = data #data stores values of the nodes
        self.next = None #next points to the next node(initialized as None)

def reverse(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

def print_linked_list(head):
    current = head
    while current:
        print(current.data, end=" ")
        current = current.next
    print()

def solve():
    t = int(input())  # number of test cases
    for _ in range(t):
        n = int(input())  # number of elements in the linked list
        if n == 0:
            print()  # empty list case(0 element in list)
            continue
        
        head = None #initially no value
        for _ in range(n):
            data = int(input())
            new_node = LinkedListNode(data)
            new_node.next = head
            head = new_node
        
        # Reverse the linked list
        head = reverse(head)
        
        # Print the reversed list
        print_linked_list(head)
        
solve()
        

'''        
input:
2(testcase)
3(input no)
2
3
4
4(input no)
2
3
4
5  
output:
4 3 2 
5 4 3 2     
'''