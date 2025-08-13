# Q1] Stop at 7
# Write a loop that prints numbers from 1 to 10,
# but stops completely if it reaches 7.

for i in range(1,10):
    if i==7:
        break
    print(i)


# Q2] Skip Multiples of 3
# Print numbers from 1 to 15,
# but skip any number that is a multiple of 3.

for i in range(1,16):
    if i%3==0:
        continue
    print(i)

# Q3] First Negative Finder
# Keep asking the user for numbers.

# If they enter a negative number, print "First negative found!" and stop.
# Otherwise, keep asking.

while True:
    user_input=input("Enter number:")

    if not user_input.lstrip("-").isdigit():
        print("Invalid")
        continue

    elif user_input.lower()=="quit":
        print("Exit")

    nums=int(user_input)
    if nums<0:
        print("First Negative number")
        break


# Q4] Skip Empty Inputs
# Keep asking the user for text.
# If the user just presses Enter (empty string), skip that turn.
# If they type "stop", end the loop completely.
# Otherwise, print their text in uppercase.

while True:
    user_input=input("Enter a value:")

    if not user_input.isalpha():
        print("invalid")
        continue

    if user_input.lower()=="stop":
        break

    elif user_input=="":
        continue

    else:
        print(user_input.upper())

# Q5] Search in List

# nums = [2, 4, 6, 8, 10, 12, 14]
# Search for a number the user enters:

# If found → print "Found!" and stop searching.

# If not found after the loop ends → print "Not found"

nums = [2, 4, 6, 8, 10, 12, 14]
user_input=int(input("Enter value:"))

for number in nums:
    if user_input==number:
        print("Found")
        break
    else:
        continue
else:
    print("Not found")


# Q6] Skip Vowels
# Take a string from the user and print each letter,
# but skip vowels (a, e, i, o, u).

user_input=input("Enter String:")

vowels="aeiou"

for letter in user_input:
    if letter in vowels:
        continue
    else:
        print(letter,end="")


# Q7] Password Attempts
# Ask the user for a password.
# If it’s correct ("python123"), print "Access Granted" and stop.
# If not, let them try again up to 3 times before stopping.

password=input("Enter Password:")

for _ in range(3):
    if password=="python123":
        print("Access Granted")
        break
    else:
        password=input("Retry:")
        