
"""
PRIORITY QUEUE

Priority queue is a linear data structure which worls on FIFO

# It worrks like hospital, the most crirtical patient gets treatment first

Elements are added normally but the popping will be based on priority

# Two ways for priority:
- Higest value elemnt having priority first
- Or set lowest value elemnt having priority first
- Depending upon the condition

- If you take lowest as priority:
Then it will check the lowest element in the whole queue 

q = 10 20 30 100 70 50

first 10 will be removed
then 20 will be removed
then 30
then 50 will be removed (look at queue again 100 will be last to move out)

### Implementation

two ways
1. priority queue class itself
2. Using LIST

While uing LIST
- First add all the elements then you have to sort before removal


"""

import queue;

print("Using priority queue class");

print("First we will give priority to lowest value");

q_low = queue.PriorityQueue();
print(q_low);
print(type(q_low));
print();


q_low.put(10);
q_low.put(60);
q_low.put(30);
q_low.put(40);

# q.put() is used to pop for queue class 
print("Removed element:", q_low.get())
print("Removed element:", q_low.get())
print("Removed element:", q_low.get())
print();

print("Using tuples with priority queue");

# We will use list
q_tup = [];

q_tup.append((1, "alexa"));
q_tup.append((2, "chris"));
q_tup.append((4, "dante"));

print("Unsorted list:")
print(q_tup);

print();
print("Printing sorted list ascending order: ");

q_tup.sort();
print(q_tup);

print();
print("Printing sorted list descending order: ");

q_tup.sort(reverse = True);
print(q_tup);

# While poppping we have to 0 like pop(0) to remove 4 first
q_tup.pop(0);
print(q_tup);




