
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

            while n is not None:
                print(n.data, " --> ", end =" ");
                n = n.ref;
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

            # N will reach the last node
            while n is not None:
                n = n.ref;

            # Traverse while from last node = n to head
            while n is not None:
                print(n.data, " --> ", end =" ");
                n = n.pref;



        print();







