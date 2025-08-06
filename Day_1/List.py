# # q] Remove Duplicates
# Input: [1, 2, 2, 3, 4, 4, 5]
# Output: [1, 2, 3, 4, 5]

values=input("Enter values:").split(' ')

while all(value.isnumeric() for value in values):
    lst=map(int,values)
    lst=list(lst)

    lst.sort()

    sett=set(lst)

    lst=list(sett)
    print(lst)
    break

# Q2] Count Frequency of Each Element
# Input: [1, 2, 2, 3, 3, 3]
# Output:
# 1 → 1  
# 2 → 2  
# 3 → 3

#using count and set

elements=list(map(int,input("Enter values:").split(",")))

unique_elements=set(elements)
unique_list=sorted(list(unique_elements))

print("Count  ||  Element")

for i  in range(len(unique_elements)):
    print(f"   {elements.count(unique_list[i])}   ||     {unique_list[i]}")

#OR usimg counter from collections

from collections import Counter
elements=list(map(int,input("Enter values:").split(",")))

countdict=Counter(elements)
for key,value in countdict.items():
    print(key,value)

#OR using double for loop

elements=list(map(int,input("Enter Values:").split(",")))

counted=[]

for  i in range(len(elements)):
    if elements[i] not in counted:
        count=0
        for j in range(len(elements)):
            if elements[i]==elements[j]:
                count +=1
        counted.append(elements[i])
        print(count,counted[i])


# Q3] Find All Elements Greater Than Average
# Input: [1, 4, 5, 2, 3]
# Output: [4, 5]
# (Average = 3, return values > 3)


values=list(map(int,input("Enter values:").split(",")))

avg_values=sum(values)/len(values)

for value in values:
    if value>avg_values:
        print(value)


# Q4️] Compress Consecutive Elements
# Like your earlier string problem:
# Input: ["a", "a", "b", "b", "c"]
# Output: ["a2", "b2", "c1"]

#Doesnt work too well but first try

elements=list(map(str,input("Enter Values:").split(",")))

unique_element=set(elements)
unique_list=sorted(unique_element)
lst=[]

for index in range(len(unique_element)):
    if elements.count(unique_list[index])>=1:
            lst.append(elements.count(unique_list[index]))

print(lst,unique_list)

#OR brute force does not count for consecutive elements 

elements=list(map(str,input("Enter Values:").split(",")))

counted=[]

for i in range(len(elements)):
    if elements[i] not in counted:
        count=0
        for j in range(len(elements)):
            if elements[i]==elements[j]:
                count +=1
        countstr=str(count)
        new_elem=elements[i]+countstr
        counted.append(new_elem)
sett=set(counted)
unique_counted=sorted(sett)
print(unique_counted)

#OR

elements=list(map(str,input("Enter Values:").split(",")))

result=[]
i=0

while i <len(elements):
    count=1
    while i+1<len(elements) and elements[i]==elements[i+1]:
        count+=1
        i+=1
    result.append(elements[i]+str(count))
    i+=1
print(result)


# Q6]Group Consecutive Numbers
# 📝 Problem:
# Given a list of integers, compress consecutive duplicates by storing them as [value, count] sublists.

# 📥 Input Example:

# Enter numbers (comma separated): 1,1,1,2,2,3,1
# 📤 Expected Output:

# [[1, 3], [2, 2], [3, 1], [1, 1]]


numbers=list(map(str,input("Enter Value").split(",")))
print(numbers)
counted=[]

for i in range(len(numbers)):
    if numbers[i] not in counted:
        count=0
        for j in range(len(numbers)):
            if numbers[i]==numbers[j]:
                count=+1
        counted.append(numbers[i])
count=list(count)
print(counted+count)

#OR

numbers=list(map(str,input("Enter Value").split(",")))
counted=[]
i=0

while i <len(numbers):
    count=1
    while i +1<len(numbers) and numbers[i]==numbers[i+1]:
        count+=1
        i+=1
    counted.append([numbers[i],str(count)])        
    i+=1
print(counted)

#OR Perfect code

numbers=list(map(int,input("Enter Values:").split(',')))
counted=[]
i=0

while i <len(numbers):
    count=1
    while i+1<len(numbers) and numbers[i]==numbers[i+1]:
        count+=1
        i+=1
    counted.append([count,numbers[i]])
    i+=1
print(counted)


# Q7] Flatten a Nested List
# Input: [[1, 2], [3, 4], [5]]
# Output: [1, 2, 3, 4, 5]

rows=int(input("Enter number of rows:"))

nested=[]
counted=[]
for i in range(rows):
    row=list(map(int,input(f"Enter numbers for row {i+1}:").split()))
    nested.append(row)

for row in nested:
    for item in row:
        counted.append(item)

print(counted)
