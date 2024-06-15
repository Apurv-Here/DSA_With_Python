
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



    # Adding Node AFTER certain point, x is position
    def add_after(self, data, x):
        if self.head is None:
            print("Linked List is empty");
        else:
            n = self.head;
            while n is not None:
                if x == n.data:
                    break;
            else:
                n = n.nref;
            if n is None:
                print("Given node is not present in Doubly LL");
            else:
                # Now n is pointing to x, we need to insert just after it
                # Be careful about the last node

                new_node = Node(data);
                new_node.nref = n.nref;
                new_node.pref = n;
                if n.nref is not None:
                    n.nref.pref = new_node;
                # If x is the last node, n.nref.pref this will give error
                n.nref = new_node;


    # Adding Node BEFORE certain point
    def add_before(self, data, x):
        if self.head is None:
            print("Linked List is empty");
        else:
            n = self.head;
            while n is not None:
                if x == n.data:
                    break;
            else:
                n = n.nref;
            if n is None:
                print("Given node is not present in Doubly LL");
            else:
                # Be careful that x is not the first node
                new_node = Node(data);
                new_node.nref = n;
                new_node.pref = n.pref;
                # Node/x is not first node
                if n.pref is not None:
                    n.pref.nref= new_node;
                else:
                    # x is first node
                    self.head = new_node;
                n.pref = new_node;


    # Delete operations
    # Delete begin, delete end, delete by value

    def delete_begin(self):
        if self.head is None:
            print("Doubly Linked List is empty so can't delete");
            return;
        # If the LL has exactly one node, and you try to delete from start
        elif self.head.nref is None:
            self.head = None;
            print("Doubly Linked List is empty now");
        else:
            self.head = self.head.nref;
            self.head.pref = None;


    def delete_end(self):
        if self.head is None:
            print("Doubly Linked List is empty so can't delete");
            return;
        # If the LL has exactly one node, and you try to delete from end
        elif self.head.nref is None:
            self.head = None;
            print("Doubly Linked List is empty now");
        else:
            n = self.head;
            while n.nref is not None:
                n = n.nref;
            n.pref.nref = None;

        





if __name__ == "__main__":

    DL1 = doublyLL();


    # Inserting in an empty linked list
    # DL1.insert_empty(10);
    # DL1.print_LL_reverse();
    # DL1.print_LL_forward();

    # Inserting before and after at x in Doubly LL
    # DL1.add_begin(4);
    # DL1.add_after(10, 4);
    # DL1.print_LL_forward();
    # DL1.print_LL_reverse();
    # DL1.add_before(1000, 4);
    # print();
    # DL1.print_LL_forward();
    # DL1.print_LL_reverse();

    # Delete from begin and end operations
    DL1.add_begin(4);
    DL1.add_begin(6);
    DL1.add_begin(8);
    DL1.add_begin(10);
    DL1.print_LL_forward();
    DL1.delete_begin();
    DL1.print_LL_forward();
    DL1.delete_end();
    DL1.print_LL_forward();






