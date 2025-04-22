class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
#creating nodes
node1=Node(10)
node2=Node(20)
node3=Node(30)
node4=Node(40)

#Linking nodes
node1.next=node2  #1->2
node2.next=node3  #2->3
node3.next=node4  #3->4

#head of linkedlist
head=node1
def print_list(head):
    current =head  #head stores node1 address
    while current:
        print("[",current.data ,"| next","]", end=" -> " if current.next else "\n")
        current=current.next
        
#calling function        
print_list(head)


 
'''     
class SingleLinkedlist:
    node1=Node(10):
    node2=Node(20)
    node3=Node(30)
    node4=Node(40)
'''
   























