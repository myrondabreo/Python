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

while True:
    user_ip=input("Enter value:")

    if user_ip.lower()=="quit":
        print("Exit")
        break

#lstrip because isdidgits does not classify negative numbers so it we input -1 it will be invalid
    elif not user_ip.lstrip("-").isdigit():
        print("Invalid")
        continue

    nums=int(user_ip)

    if nums==0:
        print("Zero")
    elif nums<0:
        print("Negative")
    elif nums>0:
        print("Positive")



 
