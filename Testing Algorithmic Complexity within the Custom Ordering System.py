from prettytable import PrettyTable
from memory_profiler import profile

def numberchecker(Item1, item, item_number):
#Goes Through each item in the List
        for y in range(0, len(item)):
        #Checks to see If the current item is the same as the inputted one
                if Item1 == item[y]:
                        print("Item Successfully Added")
                        #This now changed Item 1 into the Order Number
                        Item1 = item_number[y]
                        #returns the original inputted items number. 
                        return Item1
                else:
                        y += 1
# If the function return a Null value the system catches later on and asks for another value





@profile
def create(): 
        #Importing Table Library
        RestartLoop = True 
        item = ["Scissors", "EyeWash", "PainKillers", "Plasters", "Bandages", "Safety Pins", "Tweezers", "Anti-Septic Creme"]
        item_number = ["1234", "2345", "3456", "4567", "5678", "6789", "7890", "8912"]
        order_numbers = ["01", "02", "03", "04", "05"]


        table = PrettyTable(["Orders", "P1", "P2", "P3", "P4", "P5"])
        table.add_row(["01", 2345, 7890, 8912, 4567, 5678]) 
        table.add_row(["02", 7890, 1234, 4567, 2345, 8912]) 
        table.add_row(["03", 1234, 5678, 2345, 7890, 4567]) 
        table.add_row(["04", 3456, 2345, 9123, 4567, 7890]) 
        table.add_row(["05", 6789, 3456, 5678, 7890, 2345]) 

        print("Welcome to Jiraya Industries!\n")

        print("Your Current Orders Are: ")
        print(table)

        while RestartLoop == True:
            #Giving The User An Option As to What They Would Like to Do
            UserChoice = input("What Would You Like To Do: \n1 - Create \n2 - Delete \n3 - Modify \n4 - Exit: ")

            #Setting Up What Happens Depending On Their Option
            if UserChoice == "1":
                print("Your Available Options Are:")
                for i in range(0,len(item)):
                    print("Item:", item[i])

                print("==========================================================")
                loop = True
                while loop == True:
                    OrderNumber = input("Enter your order number : ").strip()
                    if OrderNumber.isdigit() and OrderNumber not in order_numbers:
                        order_numbers.append(OrderNumber)
                        order_numbers.sort()
                        loop = False
                    else:
                        print("Your Entry Was Not Valid")
                        print("Please Make Sure You Entered A Number That Does Not Have An Order Already Assigned To It")

                print("Please Enter The Name of The Product")
                
                loop = True
                while loop == True:
                    Item1 = input("Item 1 Number: ")
                    CheckedItem1 = numberchecker(Item1, item, item_number)

                    Item2 = input("Item 2 Number: ")
                    CheckedItem2 = numberchecker(Item2, item, item_number)

                    Item3 = input("Item 3 Number: ")
                    CheckedItem3 = numberchecker(Item3, item, item_number)

                    Item4 = input("Item 4 Number: ")
                    CheckedItem4 = numberchecker(Item4, item, item_number)

                    Item5 = input("Item 5 Number: ")
                    CheckedItem5 = numberchecker(Item5, item, item_number)

                    if CheckedItem1 != None and CheckedItem2 != None and CheckedItem3 != None and CheckedItem4 != None and CheckedItem5 != None:
                        loop = False
                    else: 
                        print("One Of Your Entires Was Invalid, Try Again")

                print("-----------------------------------------------")
                #Adds Row Using The Data That Has Been Entered Above
                table.add_row([OrderNumber, CheckedItem1, CheckedItem2, CheckedItem3, CheckedItem4, CheckedItem5])
                print("Your Orders have been Created\n")
                table.sortby = "Orders"
                print(table)

            elif UserChoice == "2":
                loop = True
                while loop == True:
                    OrderNumber = input("Enter The Order Number For Which You Would Like To Delete: ").strip()
                    if OrderNumber.isdigit() and OrderNumber in order_numbers:
                        loop = False
                        for i in range(0, len(order_numbers)):
                            if order_numbers[i] == str(OrderNumber):
                                table.del_row(i)
                                order_numbers.pop(i)
                                break
                    else:
                        print("You Did Not Enter a number")
                        print("Please Enter a Number")
                #Deletes Row
                print("Your Orders Have Been Deleted\n")
                table.sortby = "Orders"
                print(table)

            elif UserChoice == "3":
                loop = True
                while loop == True:
                    OrderNumber = input("Enter The Order Number For Which You Would Like To Modify: ").strip()
                    if OrderNumber.isdigit() and OrderNumber in order_numbers:
                        loop = False
                        for i in range(0, len(order_numbers)):
                            if order_numbers[i] == OrderNumber:
                                table.del_row(i)
                                order_numbers.pop(i)
                                break
                    else:
                        print("You Did Not Enter a number")
                        print("Please Enter a Number")

                #Adds New Row
                print("Please Enter the new Data. ")
                print("------------------------------")
                loop = True
                while loop == True:
                    OrderNumber = input("Enter your new order number : ").strip()
                    if OrderNumber.isdigit() and OrderNumber not in order_numbers:
                        order_numbers.append(OrderNumber)
                        order_numbers.sort()
                        loop = False
                    else:
                        print("Your Entry Was Not Valid")
                        print("Please Make Sure You Entered A Number That Does Not Have An Order Already Assigned To It")

                print("Please Enter The Name of The Product")
                
                loop = True
                while loop == True:
                    Item1 = input("Item 1 Number: ")
                    CheckedItem1 = numberchecker(Item1, item, item_number)

                    Item2 = input("Item 2 Number: ")
                    CheckedItem2 = numberchecker(Item2, item, item_number)

                    Item3 = input("Item 3 Number: ")
                    CheckedItem3 = numberchecker(Item3, item, item_number)

                    Item4 = input("Item 4 Number: ")
                    CheckedItem4 = numberchecker(Item4, item, item_number)

                    Item5 = input("Item 5 Number: ")
                    CheckedItem5 = numberchecker(Item5, item, item_number)

                    if CheckedItem1 != None and CheckedItem2 != None and CheckedItem3 != None and CheckedItem4 != None and CheckedItem5 != None:
                        loop = False
                    else: 
                        print("One Of Your Entires Was Invalid, Try Again")

                print("-----------------------------------------------")
                #Adds Row Using The Data That Has Been Entered Above
                table.add_row([OrderNumber, CheckedItem1, CheckedItem2, CheckedItem3, CheckedItem4, CheckedItem5])
                table.sortby = "Orders"
                print(table)
                
            elif UserChoice == "4":
                print("Your Final Orders Are:")
                table.sortby = "Orders"
                print(table)
                RestartLoop = False

            #What Happens If You Do Not Enter A Valid Option.
            else:
                print("Stick To The Options I Gave You... ")

create()
