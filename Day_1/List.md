🔹 PART 1: Python List – Deep Explanation
🔸 What is a List?
A list in Python is an ordered, mutable collection of elements.

It can hold items of different types (int, float, string, list, etc.).

Lists are defined using square brackets:

my_list = [1, 2, "hello", [3, 4]]
🔸 List Creation

empty_list = []
numbers = [1, 2, 3, 4]
words = ["apple", "banana", "cherry"]
mixed = [1, "hi", 3.5, [1, 2]]

🔸 Accessing Elements

print(words[0])     # "apple"
print(words[-1])    # "cherry" (last element)

🔸 Modifying Elements

words[1] = "orange"
print(words)  # ["apple", "orange", "cherry"]

🔸 List Methods (Most Common)
Method	Use
append()	Adds element to end
insert(i, x)	Inserts at index i
remove(x)	Removes first occurrence of x
pop(i)	Removes and returns element at index i (default: last)
sort()	Sorts list (in-place)
reverse()	Reverses list (in-place)
index(x)	Returns first index of x
count(x)	Returns count of x
copy()	Returns a shallow copy
clear()	Empties the list

🔸 Iterating Through Lists

for item in my_list:
    print(item)

for i in range(len(my_list)):
    print(i, my_list[i])

🔸 List Comprehension

squares = [x*x for x in range(5)]  # [0, 1, 4, 9, 16]

🔸 Slicing

Edit
a = [10, 20, 30, 40, 50]
print(a[1:4])  # [20, 30, 40]
print(a[::-1]) # [50, 40, 30, 20, 10]

🔸 Membership Test

if 20 in a:
    print("Found")

🔸 Nested Lists

matrix = [[1,2], [3,4]]
print(matrix[1][0])  # 3