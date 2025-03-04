from memory_profiler import profile

@profile
def create(): 
    #Sets Pre-Existing Orders
    orders = [1,2,3,76,85,99]

    print("Welcome To Tanjiro Safety Products Ltd \n")
    print("The Current Orders Are:")
    #Shows Current Orders
    print(orders)

    #Setting Variables So Loops Will Work
    system_loop = True

    while system_loop == True:

        #Asks user What they Would Like to Do
        choice_loop = True
        choice = input("What would you like to do:\n1 - Create an Order \n2 - Delete an Order \n3 - Modify an Order\n4 - Exit \n")
        if choice == "1":
            while choice_loop == True:

                #Removes Spaces Before and After Entry
                try:
                    order_new = input("Please Enter Your Order Number: ")
                except: 
                    print("You Did Not Enter A Valid Number")

                #Checks if entry is a number or if its already in the system
                if order_new in orders:
                    print("The Number Is Already In Our System")
                else:
                    choice_loop = False

            #Adds Users Order Number to The End Of The List
            orders.append(int(order_new))
            orders.sort()
            print(orders)
            print("==================================================\n")

        elif choice == "2":
            while choice_loop == True:

                #Removes Spaces Before and After Entry
                try:
                    order_delete = int(input("Please Enter the Order Number For the Order You Would Like To Delete: "))
                except: 
                    print("You Did Not Enter A Valid Number")
                #Checks if entry is a number and if its already in the system
                if order_delete in orders:

                    #Goes Through Each Item in the List To Find the Matching Order
                    for i in range(0, len(orders)):
                        if orders[i] == order_delete:

                            # Deletes Matching Order Number
                            orders.pop(i)
                            orders.sort()
                            print(orders)
                            choice_loop = False
                            break
                        else:
                            i += 1
                else: 
                    print("Your Entry Is Not In Our System")
            print("==================================================\n")

        elif choice == "3":
            while choice_loop == True:

                #Asks For The Old Order Number That The User Wants To Modify
                try:
                    old_number = int(input("Please Enter The Order Number For The Order You Would Like To Modify: "))
                except: 
                    print("You Did Not Enter A Valid Number")

                #Checks if the number is an actual number and checks if its in the system
                if old_number in orders:

                    #goes through each item in the list to find the correct order number
                    for i in range(0, len(orders)):

                        #verifies that the current position in the list is the same as the one that has been entered
                        if orders[i] == old_number:

                                #deletes the order number they wish to modify
                                orders.pop(i)
                                while choice_loop == True:

                                    #asks for a new order number
                                    try:
                                        order_changed = int(input("Please Enter The New Order Number: "))
                                    except: 
                                        print("You Did Not Enter A Valid Number")

                                    #checks to see if the new number is in the system or if it is a number
                                    if order_changed in orders:
                                        print("This Order Number Already Exists")
                                    else:

                                        #Inserts New Order Number In The Same Place Old Order Number was Deleted From
                                        orders.insert(i, int(order_changed))
                                        
                                        #breaks the new number while loop
                                        choice_loop = False

                                        #exits out of the enire function
                                        break
                        else:
                            i += 1
                else:
                    print("Your Entry Is Not In Our System")
            orders.sort()
            print(orders)
            print("==================================================\n")
            
        elif choice == "4":
            print("Your Final Orders are:")
            orders = sorted(orders)
            print(orders)

            #End Loop, Ending The Program
            system_loop = False
        
        else:
            print("Please Stick To The Options I Gave You")
create()