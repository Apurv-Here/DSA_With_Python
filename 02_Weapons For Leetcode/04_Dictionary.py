
"""
DICTIONARY

1. Key value pair, they are mutable, unrordered

2. Keys are unique, you can't have duplicate keys

3. keys has to immutable objects

4. cannot have list as a key

5. You can have integers, strings, tuple as a key

"""

# Creating an empty dictionary

d = {};
d = dict();
print(d);

dict1 = {"key1" : "value1", "key2" : "value2"};
print(dict1);

dict2 = {"i" : 1, "i" : 2, "j" : 3};
print(dict2);
# Isme i ki val ab 2 ho jaegi, 1 nhi rahegi, ek hi i rahegam duplicate keys allowed nhi rehte

del dict2["i"];
print(dict2);

dict2["j"] = 5


