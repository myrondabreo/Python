# 1. Sum of Digits Until Single Digit

# Description:
# Take a positive integer input from the user and keep summing its digits until you end up with a single-digit number.
# Example:

# Input: 9875  
# Step 1: 9+8+7+5 = 29  
# Step 2: 2+9 = 11  
# Step 3: 1+1 = 2  
# Output: 2


# #Take input of number
# num=list(map(int,input("Enter Number:").split(" ")))

# #Sum the input 
# sum_of_num=sum(num)

# #Create empty list which will contain the digits of sum_of_num
# sum_list=[]

# #Main loop condition which will only stop when we get a single digit number
# while sum_of_num>=10:
#     #This will iterate through sum_of_num to get each number in it. Taking it as string because integers are not iterable
#     for number in str(sum_of_num):
#         #Appending each number of sum_of_num to sum_list.Converting the number into integer so that we can perform sum operation in next step
#         sum_list.append(int(number))
#     #Summing up sum_list and giving it to sum_of_num so that the condition keeps repeating
#     sum_of_num=sum(sum_list)
#     #Re initialising it so that it is empty when we append the next sum_of_num values
#     sum_list=[]
#     print(sum_of_num)

# print("Single digit")
        



# 2. Multiplication Table without * Operator

# Description:
# Print the multiplication table of a given number without using the * operator.
# Hint: Use addition in a loop.
# Example:

# Input: 5  
# Output:  
# 5 x 1 = 5  
# 5 x 2 = 10  
# ...  
# 5 x 10 = 50

# user_input=int(input("Enter number:"))
# value=0

# for _ in range (10):
#     value=user_input+value
#     print(value)

# 3. Number Pyramid Pattern

# Description:
# Print this pattern for n=5:

# 1  
# 1 2  
# 1 2 3  
# 1 2 3 4  
# 1 2 3 4 5



        

        

# 4. Find Largest and Smallest Number Without max() or min()

# Description:
# Take n numbers from the user, store them in a list, and find the largest and smallest values manually.
# Concepts: Loops, lists, comparisons.

# n=list(map(int,input("Enter numbers:").split(" ")))
# print(n)
# result_max=[]
# result_min=[]

# def maximum():
#     for number in n:
#         while len(result_max)>0 and result_max[-1]<number:
#             result_max.pop()
#         result_max.append(number)

#     if len(result_max)==1:
#         print(result_max)
#     else:
#         result_max.pop()
#         print(result_max)

# def minimmum():
#     for number in n:
#         if len(result_min)==0:
#             result_min.append(number)

#         if result_min[-1]>number:
#             result_min.pop()
#             result_min.append(number)
#         else:
#             continue
#     print(result_min)

# minimmum()
# maximum()

# easier version

# n=list(map(int,input("Enter Numbers:").split(" ")))

# largest=n[0]
# smallest=n[0]

# for number in n:
#     if largest<number:
#         largest=number
#     elif smallest>number:
#         smallest=number

# print(largest)
# print(smallest)
    

# 5. Number Guessing Game
# Description:
# Write a loop where the user has to guess a number (hardcode it in the script).
# If guess is too high → print "Too High"
# If guess is too low → print "Too Low"
# If guess is correct → print "Correct" and exit
# Concepts: Loops, conditionals, break.

# while True:
#     user_input=input("Enter Number:")

#     if not user_input.isdigit():
#         print("Invalid")
#         continue

#     num=int(user_input)
#     answer=41

#     if num>50:
#         print("Too High")
#     elif num<20:
#         print("Too Low")
#     elif num==answer:
#         print("Matched")
#         break
#     else:
#         print("Retry")



# 6. Reverse a String Without Slicing

# Description:
# Take a string input and reverse it without using slicing ([::-1]) or reversed().
# Concepts: Loops, string concatenation.

# user_input=input("Enter String:")
# store=""

# for i  in range(len(user_input)):
#     store=user_input[i]+store
    
# print(store)

#OR

# for letter in user_input:
#     store=letter+store

# print(store)

# 7. Count Even and Odd Digits in a Number
# Description:
# Input a number and count how many digits are even and how many are odd.
# Example:
# Input: 24367 → Output: Even = 2, Odd = 3

# while True:
#     nums=input("Enter Value")

#     if not nums.isdigit():
#         print("Invalid")
#         continue

#     lst=[]
#     for d in nums:
#         lst.append(int(d))
#     print(lst)

#     even=[]
#     odd=[]

#     for digit in lst:
#         if digit%2==0:
#             even.append(digit)
#         else:
#             odd.append(digit)
    
#     print(f"Count of even digits:{len(even)}")
#     print(f"Count of odd digits:{len(odd)}")


#8. Second Largest and Second Smallest
# Find the 2nd largest and 2nd smallest number in a list without using max() or min().

# 9. Remove Duplicates
# Take a list of numbers and create a new list without duplicates (without using set()).

# 10. Reverse a List Manually
# Write a program to reverse a list using a loop (don’t use reverse()).

# 11. Sum of Even and Odd Numbers Separately
# From a list of integers, calculate the sum of even numbers and odd numbers.

# 12. Find Missing Number
# If you have a list of numbers from 1 to n but one number is missing, find the missing number.

# 13. Rotate a List
# Rotate the elements of a list left by 1 position (e.g. [1,2,3,4] → [2,3,4,1]).

# 14. Find Common Elements
# Given two lists, find elements that are present in both.