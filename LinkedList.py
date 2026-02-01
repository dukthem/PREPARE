class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

a = Node(6)
b = Node(7)
c = Node(8)

a.next = b
b.next = c

head = a

print("Head of the node:", head.data)

# Traverse in LL
def printll(head):
    curr = head
    print("Traverse the LL", end = " ")
    while curr != None:
        print(curr.data, end = " ")
        curr = curr.next
printll(head)

#Insertion in the begin---->

newNode = Node(4)
newNode.next = head
head = newNode
printll(head)

#Insertion in the end---->

newNode = Node(1)
curr = head
while curr.next != None:
    curr = curr.next
curr.next = newNode
printll(head)

#Insertion in the kth index---->
k = 2
newNode = Node(10)
curr = head
for i in range(k-1):
    curr = curr.next
    
newNode.next = curr.next
curr.next = newNode
printll(head)

# Delete the first node --->
head = head.next
printll(head)

#  Delete the last node --->
curr = head
while curr.next.next != None:
    curr = curr.next
    
curr.next = None
printll(head)

#  Delete the kth node --->
k = 2
curr = head
for i in range(k-1):
    curr = curr.next
    
curr.next = curr.next.next
printll(head)