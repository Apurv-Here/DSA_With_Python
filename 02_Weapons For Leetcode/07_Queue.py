
"""
QUEUE

1.FIFO or LILO

Eg: If you stand in grocery line
The first person will be out first
If you are last at line your order will be processed last in queue

meaning of front and rear

        10     20   30   40     50
      front                    rear

      10 is front/head: 50 is rear/back/tail

Operations:
1. Enqueue -> add element to queue
2. Dequeue -> removing element from queue
3. isFull
4. isEmpty

Implementation:
1. Using List
2. Using Modules

LIST:
1. Enqueue -> use append method
2. Dequeue -> use pop method

"""

# Implementing queue using list 

queue = [];

queue.append(10);
queue.append(20);
queue.append(30);
queue.append(40);
print(queue);

# Note: if you just use queue.pop()
# Then it will remove the element like stack, we don't want that
# So we will use pop with indexing, 
# pop(0) means list element at 0 index is removed
# use pop mindfully, an empty list will give error while using pop

queue.pop(0);
print(queue);


# Another different way

print("Another way: ");

queue_ano = [];

queue_ano.insert(0, 10);
# this will insert at 0 index the value 10
print(queue_ano);

queue_ano.insert(0, 20);
print(queue_ano);

queue_ano.insert(0, 30);
print(queue_ano);

# Now we can use pop without index 

queue_ano.pop();
print(queue_ano);

queue_ano.pop();
print(queue_ano);


# Check if queue is empty or not

sample_queue = [];

if not sample_queue == True:
    print("Queue is empty");



















