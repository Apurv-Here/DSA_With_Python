
"""
SETS

1. Collection of unique items

2. Cannot of duplicates, is mutable

3. Can be defined by curly braces for empty set

4. Set is unordered, set can only have immutable objects as element

"""

# Creating an empty set

s = set();
print(s);

# creating set by constructor and curly braces

s1 = set([1, 2, 3, 4]);

s2 = {1, 2, 3, 4};

print(s1);
print(s2);

s3 = {1, 1, 1, 2, 4};
print(s3);

# This below line will give error
# s = ( [1, 2, 3], 4, 5);
# Bcz s is having list as element, List is mutable object

print("Printing set1 elements: ");
set1 = {1, 2, 3, 4};

for i in set1:
    print(i);

print("Checking if element is there or not");
print(1 in set1);
print(12 in set1);