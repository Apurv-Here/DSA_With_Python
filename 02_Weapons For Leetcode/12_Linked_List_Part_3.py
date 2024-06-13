
"""
DOUBLY LINKED LIST

Three main operations

1. Insertion: begin, end, middle

2. Deletion: begin, end, by value

3. Traversal: forward traversal & backward traversal


"""

class Node:
    def __init__(self, data):
        self.data = data;
        self.pref = None;
        self.nref = None;
 
    # None  10isData    None  
    # pref    data       nref
    

class doublyLL:
    def __init__(self):
        # We start from an empty LL so head is pointing None
        self.head = None;

    def print_LL_forward(self):
        if self.head is None:
            print("Linked List is empty!");
        else:
            n = self.head;
            print("Printing forward traversal");
            while n is not None:
                print(n.data, " --> ", end =" ");
                n = n.nref;
        print();
    

    """
        To print in reverse you have to start from last node
        How will you go to last node? use a while loop till is not none
        Even though you get last node how to get previos from last node? use lastnode.pref

    """
    def print_LL_reverse(self):
        if self.head is None:
            print("Linked List is empty!");
        else:
            n = self.head;
            print("Printing reverse traversal");
            # N will reach the last node
            while n.nref is not None:
                n = n.nref;

            # Traverse while from last node = n to head
            while n is not None:
                print(n.data, " --> ", end =" ");
                n = n.pref;

        print();

    # Inserting when Doubly LL is empty
    def insert_empty(self, data):
        if self.head is None:
            new_node = Node(data);
            self.head = new_node;
        else:
            print("Linked List is not empty");


    # Adding at beginning of DLL
    def add_begin(self, data):
        new_node = Node(data);
        if self.head is None:
            self.head = new_node;
        # If the LL is not empty
        else:
            new_node.nref = self.head;
            self.head.pref = new_node;
            self.head = new_node;


     # Adding at end of DLL
    def add_end(self, data):
        new_node = Node(data);
        if self.head is None:
            self.head = new_node;
        else:
            n = self.head;
            while n.ref is not None:
                n = n.ref;
                n.nref = new_node;
                new_node.pref = n;





if __name__ == "__main__":

    DL1 = doublyLL();


    # Inserting in an empty linked list
    DL1.insert_empty(10);
    DL1.print_LL_reverse();
    DL1.print_LL_forward();





