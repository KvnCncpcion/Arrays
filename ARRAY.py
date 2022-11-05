print("**********************PROGRAMMED BY***********************")
print("***************Kevin Joseph G. Concepcion*****************")

Array = [1, 4, 3, 4, 4, 5, 6 ,2 ,56, 200]

def menu():
    print("\n>>>>>>>> MENU <<<<<<<<")
    print("1 -> Add an Element")
    print("2 -> Insert an Element")
    print("3 -> Modify an Element")
    print("4 -> Delete an Element")
    print("5 -> Arrange in Ascending Order")
    print("6 -> Arrange in Descending Order")
    print("7 -> Find the Smallest Number")
    print("8 -> Find the Biggest Number")
    print("9 -> Find the Sum of all the Elements")
    print("10 -> Count how many times an element appeared")
    print("11 -> Count how many elements in the list")
    print("12 -> Remove the last element")
    print("13 -> Exit")

def exit():
    print("\nThank you for using the program!!!")

while True:
    menu()
    print("")
    print("This is the list:",Array)

    choice = int(input("\nInput the number of the command: "))
    if choice == 1:
        app = int(input("Enter the number of your choice: "))
        Array.append(app)
        print("The element inserted:",app)
        print("This is the result:",Array)

    elif choice == 2:
        ins = int(input("Enter the number of your choice: "))
        idx = int(input("Enter your choice of index(0-9 only): "))
        Array.insert(idx, ins)
        print("The element inserted:", ins)
        print("This is the result:",Array)

    elif choice == 3:
        mod = int(input("Enter your number of choice to replace the element: "))
        idx = int(input("Enter your choice of index(0-9 only): "))
        Array[idx] = mod
        print("This is the replacement of the element:",mod)
        print("This is the result:",Array)

    elif choice == 4:
        num = int(input("Enter number of your choice(only within the list): "))
        Array.remove(num)
        print("This is the result:",Array)

    elif choice == 5:
        Array.sort()
        print("This is the result:",Array)

    elif choice == 6:
        Array.sort()
        Array.reverse()
        print("This is the result:",Array)

    elif choice == 7:
        smallest_num = min(Array)
        print("This is the smallest number in the list is:",smallest_num)

    elif choice == 8:
        biggest_num = max(Array)
        print("This is the biggest number in the list is:",biggest_num)

    elif choice == 9:
        total = sum(Array)
        print("The total is:",total)

    elif choice == 10:
        elem = int(input("Enter the number of your choice(only within the list): "))
        count = Array.count(elem)
        print("This is the number of time/s that", elem, "appeared:", count)

    elif choice == 11:
        length = len(Array)
        print("The elements present in the list is:", length)

    elif choice == 12:
        Array.pop()
        print("This is the result:", Array)

    elif choice == 13:
        exit()
        break

    else:
        print("Invalid Option")

    ques_ans = input("\nWould you like to try again?(Y/N): ")
    ans = ques_ans.capitalize()
    if ans == "Y":
        continue
    else:
        print("\nThank you for using the program!!!")
        break