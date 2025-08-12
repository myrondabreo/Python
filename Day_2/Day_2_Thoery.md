1. Control Flow Basics
Control flow is how a program decides which block of code to execute next depending on conditions or repetition rules.

At its core, Day 2 covers:

Decision Making → if, elif, else, match-case

Looping → for, while

Loop control keywords → break, continue, else, pass

Utility for loops → range()

2. Decision Making
if, elif, else
Python evaluates conditions in order and executes the first block where the condition is True.

Syntax:


if condition1:
    # executes if condition1 is True
elif condition2:
    # executes if condition1 is False and condition2 is True
else:
    # executes if all above are False

Key points:

Conditions must evaluate to a boolean (True or False).

You can use logical operators and, or, not to combine conditions.

Python uses indentation to define code blocks (usually 4 spaces).

Example (with deep insights):


temperature = 25

if temperature > 30:
    print("It's hot outside.")
elif 20 <= temperature <= 30:
    print("It's warm outside.")
else:
    print("It's cold outside.")
Here:

Chained comparison → 20 <= temperature <= 30 is more readable than temperature >= 20 and temperature <= 30.

3. Loops


for loops
Best for known range or iterating over a sequence.

Syntax:


for variable in iterable:
    # code block

Example:


fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)


Pro Tip:
Iterating with index:


for i, fruit in enumerate(fruits):
    print(f"Index {i}: {fruit}")
while loops
Best for unknown repetition count until a condition becomes false.

Syntax:

while condition:
    # code block
Example:


count = 1
while count <= 5:
    print(count)
    count += 1

Danger Zone: Infinite loops happen if the condition never becomes False.

4. Loop Control Statements

break
Ends the loop immediately, regardless of condition.(ends loop doesnt go to any previous steps,it moves on)

break completely ends the loop — it doesn’t just skip the rest of the current iteration like continue does, it stops the loop entirely and jumps to the first line after the loop block.

Example

for i in range(1, 6):
    if i == 3:
        break
    print(i)

print("Loop ended.")
Output:

1
2
Loop ended.


for num in range(1, 10):
    if num == 5:
        break
    print(num)

continue
Skips current iteration and moves to the next.(Skips current and jumps back to first step)
while True:
    [Step 1] Ask for input
    [Step 2] Check something
        if condition met → continue → JUMP back to Step 1
    [Step 3] (skipped entirely)



for num in range(1, 6):
    if num == 3:
        continue
    print(num)

else with loops
Executes only if loop completes without break.


for num in range(1, 5):
    print(num)
else:
    print("Loop finished without break.")


5. range() Function
Generates a sequence of numbers (lazy — doesn’t store all at once).

Syntax:


range(start, stop, step)
start → default 0

stop → required, exclusive

step → default 1


for i in range(2, 11, 2):
    print(i)
Prints even numbers 2 to 10.

6. match-case (Python 3.10+)
Pattern matching, similar to switch in other languages but more powerful.

Syntax:


match variable:
    case value1:
        # code
    case value2:
        # code
    case _:
        # default case

Example:


grade = "B"

match grade:
    case "A":
        print("Excellent")
    case "B":
        print("Good")
    case "C":
        print("Average")
    case _:
        print("Invalid grade")

7. pass Statement
A do-nothing placeholder for blocks you plan to fill later.


def future_function():
    pass  # TODO: implement later