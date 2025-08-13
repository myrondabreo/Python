if __name__=="__main__":

    #The number of numbers to calculate
    no_of_numbers=int(input("Enter number of numbers to calculate:"))

    #Initialising the count of numbers
    numbers=0

    #Checking for valid input
    if no_of_numbers <= 1:
        print("Please enter a valid number greater than 0.")
        exit()

    #Initialising empty list for list
    list_numbers_to_calculate=[]

    # Loop to get the numbers from the user
    while numbers<no_of_numbers:
        numbers_to_calculate =int(input("Enter a number:"))
        list_numbers_to_calculate.append(numbers_to_calculate)
        numbers += 1
    print(list_numbers_to_calculate)


    #Letting user select the operation    
    print("Select your operation: \n1 Add\n2 Sub\n3 Multiply\n4 Div")
    operation= int(input("Enter your choice:"))

    #Initializing result
    result = 0

    for index in range(len(list_numbers_to_calculate)):
        if operation==1:
            result = list_numbers_to_calculate[index] +result
        
        elif operation==2:
            if len(list_numbers_to_calculate)>2:
                print("Subtraction is not possible")
                break
            else:
                result = list_numbers_to_calculate[index]-result
        
        # elif operation==3:
        #     result=list_numbers_to_calculate[index]*result
            


    if operation == 1:
        print(f"Result of addition is: {result}")
    elif operation == 2:
        if result<0:
            print(f"Result of subtraction is: {abs(result)}")
        # elif result==0:
        #     print(f"Result of subtraction is: {result}")
        else:
            print(f"Result of subtraction is: {result}")



    