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

# n=list(map(int,input("Enter Value").split(" ")))
# n.sort()
# #Fails for dupes
# print(n[-2])
# print(n[1])

# #Works for dupes
# sortedn=list(set(n))
# print(sortedn[-2])
# print(sortedn[1])

#OR

# n=list(map(int,input("Enter Value").split(" ")))
# # float('inf') → Positive infinity (a number larger than any real number).
# # float('-inf') → Negative infinity (a number smaller than any real number).
# largest=float('-inf')
# smallest=float('inf')

# for number in n:
#     if largest<number:
#         largest=number
#     if smallest>number:
#         smallest=number
# print(largest)
# print(smallest)

# second_largest=float('-inf')
# second_smallest=float('inf')
# for number in n:
#     if largest>number>second_largest:
#         second_largest=number
#     if smallest<number<second_smallest:
#         second_smallest=number
# print(second_largest)
# print(second_smallest)

# 9. Remove Duplicates
# Take a list of numbers and create a new list without duplicates (without using set()).

# n=list(map(int,input("Enter  Numbers:").split(" ")))
# nodupes=[]

# for number in n:
#     if number not in nodupes:
#         nodupes.append(number)
# print(nodupes)
    

# 10. remove duplicates but keep the last occurrence

# n=list(map(int,input("Enter Numbers:").split(" ")))
# n.reverse()
# nodupes=[]

# for number in n:
#     if number not in nodupes:
#         nodupes.append(number)
# nodupes.reverse()
# print(nodupes)

#OR Instead of reversing n use reversed(n)

# n=list(map(int,input("Enter Numbers:").split(" ")))
# nodupes=[]

# for number in reversed(n):
#     if number not in nodupes:
#         nodupes.append(number)
# nodupes.reverse()
# print(nodupes)

# 11.  Reverse a List Manually
# Write a program to reverse a list using a loop (don’t use reverse()).

# n=list(map(int,input("Enter Numbers").split(" ")))
# store=[]

# for number in reversed(n):
#     store.append(number)

# print(store)

#OR doesnt work for double digit

# store=""
# for number in n:
#     store=str(number)+store

# print(list(map(int,store)))

#OR

# n=list(map(int,input("Enter Value").split()))

# rev_list=[]

# for number in n:
    #inserts each number at index 0
#     rev_list.insert(0,number)
# print(rev_list)


# 12.  Sum of Even and Odd Numbers Separately
# From a list of integers, calculate the sum of even numbers and odd numbers.

# n=list(map(int,input("Enter Numbers:").split()))
# even=0
# odd=0

# for number in n:
#     if number%2==0:
#        #even=number+even
#        even+=number
#     else:
#        #odd=number+odd
#        odd+=number

# print(even)
# print(odd)

# 13.Find Missing Number
# If you have a list of numbers from 1 to n but one number is missing, find the missing number.

# n=int(input("Enter Range:"))
# lst=list(range(1,n+1))
# missing=list(map(int,input("Enter n with one missing").split()))
# print(lst)

# for number in lst:
#     if number not in missing:
#         print(number)

#OR

n=int(input("Enter Range:"))
missing=list(map(int,input("Enter n with one missing").split()))

original_sum=n*(n+1)//2
missing_sum=sum(missing)

final_sum=original_sum-missing_sum

print(final_sum)

# 14.Rotate a List
# Rotate the elements of a list left by 1 position (e.g. [1,2,3,4] → [2,3,4,1]).

# n=list(map(int,input("Enter Value1:").split(" ")))

# # first=[n[0]]
# # n.remove(n[0])
# # print(n)
# # counted=[]

# # for number in n:
# #     counted.append(number)

# # counted=counted+first
# # print(counted)

#OR

# # lenn=len(n)
# # counted=[]
# # for i in range(1,lenn):
# #     counted.append(n[i])
# # print(counted+[n[0]])


# 15.Find Common Elements
# Given two lists, find elements that are present in both.


# n1=list(map(int,input("Enter Value1:").split(" ")))
# n2=list(map(int,input("Enter Value2:").split(" ")))
# counted=[]

# for number1 in n1:
#     for number2 in n2:
#         if number1==number2:
#             counted.append(number1)
#         else:
#             continue

# counted_set=set(counted)
# lst=list(sorted(counted_set))
# print(lst)

#OR

# n1=list(map(int,input("Enter Value1:").split(" ")))
# n2=list(map(int,input("Enter Value2:").split(" ")))
# counted=[]

# for number in n1:
#     if number in n2 and number not in counted:
#         counted.append(number)

# print(counted)

#OR

# n1=list(map(int,input("Enter Value1:").split(" ")))
# n2=list(map(int,input("Enter Value2:").split(" ")))

# common=sorted(list(set(n1) & set (n2)))
# print(common)