
"""
LINKED LIST

It is a dynamic data structure
It is not continuous
NODE: Elements of linked list

Each node has date and the address of other element which it points
Node -> Data & Link

Last node points to NULL

You can implement stack, queue and graphs

-- Singly Linked List
-- Doubly Linked List
-- Circular Linked List

There is no built in linked list in python so we will use class concepts

"""

class Node:
    def __init__(self, data):
        self.data = data;
        self.ref = None;
        # We are note taking the reference in the arguments as value
        # Bcz we want to set the reference as NONE (means empty value)

# Now the nodes are created, we have to link them

class LinkedList:
    def __init__(self):
        self.head = None;

    def print_LL(self):
        # self.head = n (for convenience, rather to write whole self.head.data/reference = n.data)
        if self.head is None:
            print("Linked List is empty!");
        else:
            n = self.head;

            while n is not None:
                print(n.data);
                n = n.ref;

    # Method to add a new node in beginning
    def add_begin(self, data):
        new_node = Node(data);
        # This will create a new node -> Data, None

        new_node.ref = self.head;
        self.head = new_node;



if __name__ == "__main__":

    # node1 = Node(10);

    LL1 = LinkedList();
    LL1.add_begin(10);
    LL1.add_begin(20);
    LL1.print_LL();

















