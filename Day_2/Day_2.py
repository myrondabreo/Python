# Q1]1. Check if a number is positive, negative, or zero

# while True:
#     num=int(input("Enter Number:"))
#     if num==0:
#         print(num)
#     elif num<0:
#         print("Negative")
#     elif num>0:
#         print("Positive")

#OR Better version

# while True:
#     user_ip=input("Enter value:")

#     if user_ip.lower()=="quit":
#         print("Exit")
#         break

# #lstrip because isdidgits does not classify negative numbers so it we input -1 it will be invalid
#     elif not user_ip.lstrip("-").isdigit():
#         print("Invalid")
#         continue

#     nums=int(user_ip)

#     if nums==0:
#         print("Zero")
#     elif nums<0:
#         print("Negative")
#     elif nums>0:
#         print("Positive")


# Q2]Print first 10 even numbers using for loop.

# lst=list(range(1,21))
# count=0

# for value in lst:
#     if value%2==0:
#         count+=1
#         print(count,value)

# Q3]Use a while loop to reverse digits of a number.

# num=int(input("Enter Number:"))
# rev=0

# while num>0:
#     digit=num%10
#     rev=rev*10+digit
#     num//=10
# print(rev)

# Q4] Palindrome Number Check
# Ask the user for a number, reverse it using the above logic, and check if it’s the same as the original.

# Input: 121 → Output: Palindrome
# Input: 123 → Output: Not Palindrome

# num=int(input("Enter Number:"))
# rev=0
# stored=num

# while num>0:
#     digit=num%10
#     rev=rev*10+digit
#     num//=10


# if rev==stored:
#     print("Palindrome")

# else:
#     print("NOT")

# Q5] Reverse Until Negative
# Keep asking the user for a number and reverse it using the while loop.
# If the user enters a negative number, stop the program.

# while True:
#     user_input=input("Enter number:")

#     if user_input.lower=="quit":
#         print("Exit")
#         break

#     elif not user_input.lstrip("-").isdigit():
#         print("Invalid")
#         continue

#     num=int(user_input)
#     rev=0
#     if num<0:
#         print("First Negative Number")
#         break

#     while num>0:
#         digit=num%10
#         rev=rev*10+digit
#         num//=10
#     print(rev)

#Q6] Reverse Without Losing Leading Zeros
# Example: 1050 → 0501 (but as a string, because integers drop leading zeros).    

# user_input=input("Enter Value:")

# if not user_input.isdigit():
#     print("Invalid")

# rev=reversed(user_input)
# lst=list(rev)

# print("".join(lst))


# Q]Use match-case to print grade from letter input.

grade=input("Enter Grade:")
grade=grade.upper()

match grade:
    case "A":
        print("Excellent")
    case "B":
        print("Good")
    case "C":
        print("Meh")
    case "D":
        print("Below Meh")
    case "E":
        print("Just Pass")
    case "F":
        print("Fail")
    case _:
        print("Invalid Grade")

# Print Fibonacci sequence up to n terms.
