
"""
LINKED LIST

DELETE Operations

"""

class Node:
    def __init__(self, data):
        self.data = data;
        self.ref = None;

class LinkedList:
    def __init__(self):
        self.head = None;

    def print_LL(self):
        if self.head is None:
            print("Linked List is empty!");
        else:
            n = self.head;

            while n is not None:
                print(n.data, " --> ", end =" ");
                n = n.ref;
        print();




    # Insert at end
    def add_end(self, data):
        new_node = Node(data);
        if self.head is None:
            self.head = new_node;
        else:
            n = self.head;

            while n.ref is not None:
                n = n.ref;

            n.ref = new_node;


    def delete_begin(self):
        if self.head is None:
            print("Linked List is empty can't delete!")
        else:
            self.head=self.head.ref
  


    # Delete Last Node
    # We have to travel to second last node then delete last node
    def delete_end(self):
        if self.head is None:
            print("LL is empty so can't delete");
        # If LL has only one node
        elif self.head.ref is None:
            self.head = None;
        else:
            n = self.head;
            while n.ref.ref is not None:
                n = n.ref;
            n.ref = None;


    # Delete any node in LL
    def delete_by_value(self, x):
        if self.head is None:
            print("LL is empty so can't delete");
            return;

        # If the x is first node itself
        if x == self.head.data:
            self.head = self.head.ref;
            return;

        # Deleting other node position
        n = self.head;
        while n.ref is not None:
            if x == n.ref.data:
                break;
            n = n.ref;
        if n.ref is None:
            print("Node is not present in LL");
        else:
            n.ref = n.ref.ref;




if __name__ == "__main__":

    # node1 = Node(10);

    LL1 = LinkedList();

    # Delete from start
    # LL1.add_end(10);
    # LL1.add_end(20);
    # LL1.print_LL();
    # LL1.delete_begin();
    # LL1.print_LL();


    # Delete from end
    # LL1.add_end(10);
    # LL1.add_end(20);
    # LL1.add_end(30);
    # LL1.add_end(40);
    # LL1.print_LL();
    # LL1.delete_end();
    # LL1.print_LL();


    # Delete any node
    # LL1.add_end(10);
    # LL1.add_end(20);
    # LL1.add_end(30);
    # LL1.add_end(40);
    # LL1.print_LL();
    # LL1.delete_by_value(30);
    # LL1.print_LL();



    # LL1.print_LL();

















