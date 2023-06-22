n = 1
while n == 1:
    print ("------calculator------")

    num1 = float(input("Enter the first value: "))
    num2 = float(input("Enter second value: "))

    print("press 1 for add \npress 2 for subtract \npress 3 for mul \npress 4 for div")

    choice = int(input("Select the required operation"))

    if choice == 1:
        print(num1+num2)
        
    elif choice == 2:
        print(num1-num2)

    elif choice == 3:
        print(num1*num2)

    elif choice == 4:
        print(num1/num2)

    else: print("wrong choice")   
      
 

    
    

        






    