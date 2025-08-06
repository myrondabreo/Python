🔹 What is a Nested List?
A nested list is a list inside another list.

In Python, lists can contain:

Integers

Strings

Other lists

Even a mix of all of these

So a nested list is simply a list that contains one or more sublists.

🔹 Example of a Nested List

nested = [1, 2, [3, 4], [5, [6, 7]], 8]
Here:

3, 4 is a sublist.

5, [6, 7] contains another sublist [6, 7].

🔹 Why Use Nested Lists?
Nested lists are useful for:

Representing matrices or 2D arrays

Grouping related data

Working with hierarchical data like trees or directories

🔹 Accessing Elements
You use multiple indexes to access elements inside sublists:

nested = [1, 2, [3, 4], [5, [6, 7]]]

print(nested[2])        # [3, 4]
print(nested[2][1])     # 4
print(nested[3][1][0])  # 6

🔹 Modifying Elements
You can modify elements at any level using indexing:

nested[2][0] = 10
print(nested)  # [1, 2, [10, 4], [5, [6, 7]]]

🔹 Iterating Over Nested Lists
1. One level nested list (2D list):

matrix = [[1, 2], [3, 4], [5, 6]]

for row in matrix:
    for item in row:
        print(item, end=" ")

2. Unknown depth (recursive traversal):

def flatten_list(lst):
    flat = []
    for item in lst:
        if isinstance(item, list):
            flat.extend(flatten_list(item))
        else:
            flat.append(item)
    return flat

nested = [1, [2, [3, 4]], 5]
print(flatten_list(nested))  # [1, 2, 3, 4, 5]

🔹 Common Operations
Operation	Example
Access item	nested[1][2]
Modify item	nested[0][1] = 100
Append sublist	nested.append([9, 10])
Insert sublist	nested.insert(1, [11, 12])
Delete sublist/item	del nested[2][1]
Flatten	Use recursion or itertools.chain

🔹 2D List Example – Matrix
python
Copy
Edit
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Access 5
print(matrix[1][1])

# Change 9 to 0
matrix[2][2] = 0

🔹 Tips for Working with Nested Lists
Use isinstance(item, list) to check if an item is a sublist.

Use recursion for deeply nested structures.

Use list comprehensions for compact iteration.

Example:

matrix = [[1, 2], [3, 4], [5, 6]]
flat = [num for row in matrix for num in row]
print(flat)  # [1, 2, 3, 4, 5, 6]

🔹 Real-World Use Cases
Grids in games (e.g., Sudoku, chess board)

Image data (pixels in 2D or 3D arrays)

Tree structures

Data tables


✅ Taking a Nested List as Input in Python

When you want to take a nested list input from the user (via input()), there are several approaches depending on your requirements.

🔹 1. 🧠 Smartest Way (Use eval()) — For Learning/Demo Only

nested = eval(input("Enter a nested list: "))
print("Nested List:", nested)

▶ Example Input:

[1, 2, [3, 4], [5, [6, 7]]]

⚠️ Warning:
eval() can execute arbitrary code – never use it with untrusted input.

🔹 2. 🔐 Safe Way (using json.loads())

import json

nested = json.loads(input("Enter a nested list in JSON format: "))
print("Nested List:", nested)

▶ Example Input:

[1, 2, [3, 4], [5, [6, 7]]]
This is much safer than eval().

🔹 3. 🔁 Manual Entry for 2D List
If you want to input something like a 2D matrix, use loops:


rows = int(input("Enter number of rows: "))
nested = []

for i in range(rows):
    row = list(map(int, input(f"Enter row {i+1} (space-separated): ").split()))
    nested.append(row)

print("Nested List (Matrix):", nested)

▶ Example Input:

Enter number of rows: 3
Enter row 1 (space-separated): 1 2 3
Enter row 2 (space-separated): 4 5 6
Enter row 3 (space-separated): 7 8 9

Output:

[[1, 2, 3], [4, 5, 6], [7, 8, 9]]

🔹 4. 🔁 Manual Entry for Jagged Nested List

rows = int(input("Enter number of sublists: "))
nested = []

for i in range(rows):
    elements = input(f"Enter elements of sublist {i+1} (space-separated): ").split()
    nested.append([int(x) for x in elements])

print("Nested List:", nested)

▶ Input:

Enter number of sublists: 3
Enter elements of sublist 1 (space-separated): 1 2
Enter elements of sublist 2 (space-separated): 3 4 5
Enter elements of sublist 3 (space-separated): 6

Output:

[[1, 2], [3, 4, 5], [6]]












