# ✅ Day 1 – Getting Started & Python Basics

# 🔹 Section 1: Launching Python

# Python can be run in two modes:

# Interactive Mode

# Open your terminal (Command Prompt or Bash) and type python or python3.

  

# You can write and execute line-by-line code interactively.

  

# bash

# Copy

# Edit

# $ python

# >>> print("Hello World")

# Script Mode

  

# Create a file hello.py and write your code inside it.

  

# Run the script via terminal:

  

# bash

# Copy

# Edit

# python hello.py

# 💡 BONUS TIP:

# Use IDEs like VS Code, PyCharm, or Jupyter Notebook for better workflow.

  

# 🔹 Section 2: Variables, Expressions, and Types

# 🧠 THEORY

# Variable: A name pointing to a value in memory.

  

# python

# Copy

# Edit

# name = "Myron"

# age = 25

# height = 5.9

# Types: Python is dynamically typed.

  

# int: Whole numbers — 1, 2, 99

  

# float: Decimal numbers — 3.14, 2.0

  

# str: Text — "Hello"

  

# list: Ordered collection — [1, 2, 3]

  

# 🧪 PRACTICE

# python

# Copy

# Edit

# name = "Myron"

# age = 24

# city = "Mumbai"

# print(name, age, city)  # Print all in one line

# 🔹 Section 3: Basic Input/Output

# 🧠 THEORY

# Input from user: Always returns a string

  

# python

# Copy

# Edit

# user_input = input("Enter something: ")

# Convert input:

  

# python

# Copy

# Edit

# num = int(input("Enter a number: "))

# Output:

  

# python

# Copy

# Edit

# print("Hello", name)

# print(f"Age: {age}")  # f-string formatting

# 🧪 PRACTICE

# python

# Copy

# Edit

# a = int(input("Enter first number: "))

# b = int(input("Enter second number: "))

# print("Sum:", a + b)

# print("Difference:", a - b)

# print("Product:", a * b)

# 🔹 Section 4: Arithmetic and Logical Operations

# 🧠 THEORY

# Arithmetic: +, -, *, /, //, %, **

  

# Comparison: ==, !=, >, <, >=, <=

  

# Logical: and, or, not

  

# 💡 EXAMPLES

# python

# Copy

# Edit

# x, y = 5, 3

# print(x ** y)     # Exponent: 5^3 = 125

# print(x // y)     # Integer division: 1

# print(x % y)      # Remainder: 2

  

# # Logical

# print(x > 3 and y < 5)  # True

# print(not (x == y))     # True

# 🔹 Section 5: Text and List Basics

# 🧠 THEORY

# Strings:

  

# python

# Copy

# Edit

# s = "Python"

# print(s[0])  # First char

# print(len(s))  # Length

# print(s.upper(), s.lower())  # Case conversion

# Concatenation:

  

# python

# Copy

# Edit

# print("Hello " + "World")

# print("Hi", "there")  # Adds space

# Lists:

  

# python

# Copy

# Edit

# fruits = ["apple", "banana", "cherry"]

# print(fruits[1])  # 'banana'

# fruits.append("grape")  # Add

# print(fruits)

# Indexing:

  

# python

# Copy

# Edit

# print(fruits[-1])  # Last item

# print(fruits[0:2])  # Slicing: 0 and 1


# Raw strings and escape characters.


✅ Option 1: Define the String as a Raw String
Use the r'' or r"" prefix when initializing the string:

python
Copy
Edit
d = r' i have the code\name'
print(d)
# Output:  i have the code\name
✅ This is the cleanest and most direct way when you control the assignment of the string.

✅ Option 2: Escape the Backslash Manually
If the string is already created or coming from a source, you can escape the backslash:

python
Copy
Edit
d = ' i have the code\\name'
print(d)
# Output:  i have the code\name
