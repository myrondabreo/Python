# 3. Number Pyramid Pattern

# Description:
# Print this pattern for n=5:

# 1  
# 1 2  
# 1 2 3  
# 1 2 3 4  
# 1 2 3 4 5



#Q1] Print this pattern

# * * * * * 

# * * * * * 

# * * * * * 

# * * * * * 

# * * * * * 

# n=int(input("Enter Number:"))

# for i in range(n):
#     for j in range(n):
#         print("*",end=" ")
#     print("\n")

# Q2]Print this pattern

# 

# # 

# # # 

# # # # 

# n=int(input("Enter Number:"))

# for i in range(n):
#     for j in range(i+1):
#         print("#",end=" ")
#     print("\n")

#Q3]Print this pattern
# * * * * 

# * * * 

# * * 

# * 

# n=int(input("Enter Number:"))

# for i in range(n):
#     for j in range(i,n):
#         print("*",end=" ")
#     print("\n")


#Q4]Print this pattern

# * * * * * * * * * * 

#    * * * * * * * * * 

#       * * * * * * * * 

#          * * * * * * * 

#             * * * * * * 

#                * * * * * 

#                   * * * *

#                      * * *

#                         * *

#                            *


# n=int(input("Enter Number:"))

# for i in range(n):
#     for j in range(i):
#         print("  ",end=" ")
#     for j in range(i,n):
#         print("*",end=" ")
#     print("\n")

#Q5]Print this pattern

# * * * * * * * * * * 

#   * * * * * * * * 

#     * * * * * * 

#       * * * * 

#         * * 

# n=int(input("Enter Number:"))

# for i in range(n):
#     for j in range(i):
#         print(" ",end=" ")
#     for j in range(i,n):
#         print("*",end=" ")
#     for j in range(i,n):
#         print("*",end=" ")
#     print("\n")

#Q6]Print this pattern

#         * * 

#       * * * * 

#     * * * * * * 

#   * * * * * * * * 


# n=int(input("Enter Number:"))

# for i in range(n):
#     for j in range(i,n):
#         print(" ",end=" ")
#     for j in range(i+1):
#         print("*",end=" ")
#     for j in range(i+1):
#         print("*",end=" ")
#     print("\n")

#Q6]Print this pattern
# 1 

# 1 2

# 1 2 3

# 1 2 3 4

# 1 2 3 4 5


# n=int(input("Enter Number:"))

# for i in range(n):
#     for j in range(i+1):
#         j+=1
#         print(j,end=" ")
#     print("\n")


#Q7]Print this pattern
# 1 1 

# 2 2 2 

# 3 3 3 3 

# 4 4 4 4 4 

# n=int(input("Enter Number:"))
# for i in range(n+1):
#     for j in range(i+1):
#         if i>=1:
#             print(i,end=" ")
#     print("\n")

#Q8]Print this pattern

#       1 1 

#     1 2 1 2 

#   1 2 3 1 2 3 

#   1 2 3 1 2 3 

#     1 2 1 2 

#       1 1 

# n=int(input("Enter Number:"))
# for i in range(n):
#     for j in range(i,n):
#         print(" ",end=" ")
#     for j in range(i+1):
#         j+=1
#         print(j,end=" ")
#     for j in range(i+1):
#         j+=1
#         print(j,end=" ")
#     print("\n")
# for i in range(n):
#     for j in range(i+1):
#         print(" ",end=" ")
#     for j in range(n-i):
#         print(j+1,end=" ")
#     for j in range(n-i):
#         print(j+1,end=" ")
#     print("\n")
    

#Q9]Print this pattern

n=int(input("Enter Number:"))

for i in range(n,0,-1):
    print(i)
