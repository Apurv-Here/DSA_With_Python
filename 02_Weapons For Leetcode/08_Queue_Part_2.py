
"""
QUEUE Part 2

Implementing Queue (FIFO) with classes

1. deque (class) -> Collections module

Dequeue class provides flexibility to enter data from both sides
And to remove data from both sides

   10   20   30   400
   left           right

enter data from right side -> use append
remove data from right side -> use pop

enter data from left side -> use appendleft
remove data from left side -> use popleft

combination to follow FIFO wil be
if you use appendleft then use pop
if you use append then use popleft

"""

import collections;

# creating an empty queue

q = collections.deque();

print(q);
print(type(q));

q.appendleft(10);
q.appendleft(20);
q.appendleft(30);

print(q);

q.pop();
print(q);

# Since 10 was enetered first so we can only remove from right side
# As we have enetered value from left side (FIFO)

# Implementing the other combination

print("Q2 implementation")

q2 = collections.deque();

print(q2);
print(type(q2));

q2.append(10);
q2.append(20);
q2.append(30);
q2.append(40);
q2.append(50);
print(q2);

# First enetered value was 10 so we have to remove that first (FIFO)
# So we have to remove from left side

q2.popleft();
print(q2);

# TO check first and last element of queue

print("Front element of q2:", q2[0]);
print("Last element of q2:", q2[-1]);

# Check if queue is empty or not

if not q2:
    print("Queue is empty");
else:
    print("Queue is not empty");


q3 = collections.deque();
print("Checking q3");
if not q3:
    print("Queue3 is empty");
else:
    print("Queue3 is not empty");


# ----------------------------------------------

"""

 We will implement queue with queue class

 it has priority queue 

 """

import queue;

#Creating an empty queue class
que = queue.Queue();

print("Now using queue class for implementation");
print(que);
print(type(que));
print("It is an object that is why the memory adrees is showing");
print("You have to print it via other way");

que.put(10);
que.put(20);
que.put(30);
que.put(40);

# Pop method for this
# 10 will be removed first
que.get();
