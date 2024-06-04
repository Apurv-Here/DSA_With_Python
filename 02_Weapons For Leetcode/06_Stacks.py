
"""
STACKS

1.FILO or LIFO

operations on stack:
push, pop, peek or top, isEmpty

Stack implementation -> List And Modules

"""

# Creating an empty stack

st = [];


# We can use stack by List and by using modules as well

# Implement stack using List
# push -> append
# pop -> pop

stack = [];
print(stack);
stack.append(10);
stack.append(20);
stack.append(30);
print(stack);

# Pop operation

# Before pop we have to check if the length is 0 or not to avoid error

print("Length of stack is :", len(stack));

while len(stack) != 0:
    stack.pop();

print(stack);


stack.append(10);
stack.append(20);
stack.append(30);

# Top element of stack
top_element = stack[-1];
print("Top element of stack is:", top_element);

# -----------------------------------------------------

stack = [];

def push_element():
    element = input("Enter the element:");
    stack.append(element);
    print(stack);

def pop_element():

    # Stack khaali ka check karne ka tareeka python me
    if not stack:
        print("Stack is empty!");
    else:
        e = stack.pop();
        print("Removed element:", e);
        print(stack);

while True:
    print("Select the operation: 1. Push, 2. Pop, 3. Break");

    choice = int(input("Enter your choice: "));

    if choice == 1:
        push_element();

    elif choice == 2:
        pop_element();

    elif choice == 3:
        break;
    
    else:
        print("Enter the correct input");


# Stack implementation using modules

# we can use: Collections -> Deque (one side only)

import collections;

print("*****Stack using modules****");

stack = collections.deque();
print(stack);

stack.append(10);
stack.append(90);
stack.append(60);
print(stack);

stack.pop();
print(stack);










# -----------------------------------------------------