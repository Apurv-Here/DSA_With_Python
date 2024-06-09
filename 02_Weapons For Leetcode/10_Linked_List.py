
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
                print(n.data, " --> ", end =" ");
                n = n.ref;

    # Method to add a new node in beginning

    """
        Algorithm:

        earlier the head contains address of node1

        LL = node1 -> node2 -> node3 -> NULL
                |
              head

        Now we have to  insert new_node at start

        Earlier -( head = address of node1 )
        We have to change the head now

        head = address of new_node
        and [ new_node = address of node1 = HEAD (as head was having address of node 1) ]

        LL = new_node -> node1 -> node2 -> node3 -> NULL
                |
              head  
                
        1. new_node = Data(100) (Creating a new node first)
        2. new_node.ref = head
        3. head = new_node
    """
    def add_begin(self, data):
        new_node = Node(data);
        # This will create a new node -> Data, None

        new_node.ref = self.head;
        self.head = new_node;


    # Insert at end
    """
        Two conditions:
        1. If LL is empty , then directly head -> new_node
        2. If LL is not empty then go to last node (main code)
    """
    def add_end(self, data):
        new_node = Node(data);
        if self.head is None:
            self.head = new_node;
        else:
            n = self.head;

            while n.ref is not None:
                n = n.ref;

            n.ref = new_node;


    # Add node AFTER x position/node
    def add_after(self, data, x):
        n = self.head;

        while n is not None:
            if x == n.data:
                break;
            else:
                n = n.ref;

        if n is None:
            print("Node x is not present in LL");
        else:
            # The node is present
            new_node = Node(data);
            new_node.ref = n.ref;
            n.ref = new_node;


    # Add node BEFORE x position/node
    def add_before(self, data, x):
        # Check if LL is empty or not
        if self.head is None:
            print("Linked List is empty!");
            return;

        # Check if the x is first node
        if self.head.data == x:
            # Execute add begin function code
            new_node = Node(data); 
            new_node.ref = self.head;
            self.head = new_node;
            return;

        # Trick is if you want to insert before x, 
        # then you have to know info about just previous node of x
        # Then add node after the previous node, instead of adding node before x
        # Process is same like adding after x, see above method

        


if __name__ == "__main__":

    # node1 = Node(10);

    LL1 = LinkedList();

    # LL1.add_begin(10);
    # LL1.add_begin(20);
    # LL1.add_end(100);

    LL1.add_end(100);
    LL1.add_end(20);
    LL1.add_begin(10);
    LL1.add_after(3000, 100);

    LL1.print_LL();

















