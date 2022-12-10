from linked_list_Implementation import *

l1=Singly_linked_list("holaaa")
l1.insert_head(Node("A"))
l1.insert_head(Node("B"))
l1.insert_head(Node("C"))
print(l1.list_traversed())
l1.delete_node("A")
print(l1.list_traversed())
