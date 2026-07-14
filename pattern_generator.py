while True:
    print("\n========= PATTERN GENERATOR =========")
    print("1. Solid Square")
    print("2. Right Triangle")
    print("3. Inverted Triangle")
    print("4. Right-Aligned Triangle")
    print("5. Pyramid")
    print("6. Inverted Pyramid")
    print("7. Diamond")
    print("8. Hollow Square")
    print("9. Hollow Right Triangle")
    print("10. Hollow Pyramid")
    print("11. Hollow Diamond")
    print("0. Exit")
    
    choice=int(input("Enter your choice:"))

    if choice == 0:
        print("Thank you for using Pattern Generator!")
        break
    elif choice < 0 or choice > 11:
        print("Invalid Choice!")
        continue

    rows = int(input("Enter number of rows: "))

    if choice == 1:
        print("\nSelected Pattern: Solid Square")
        for i in range(rows):
            for j in range(rows):
                print("*", end=" ")
            print()

    elif choice == 2:
        print("\nSelected Pattern: Right Triangle")
        for i in range(1, rows+1):
            for j in range(i):
                print("*", end=" ")
            print()

    elif choice == 3:
        print("\nSelected Pattern: Inverted Triangle")
        for i in range(rows,0,-1):
            for j in range(i):
                print("*", end=" ")
            print()

    elif choice == 4:
        print("\nSelected Pattern: Right-Aligned Triangle")
        for i in range(1,rows+1):
            for j in range(rows-i):
                print(" ",end=" ")
            for j in range(i):
                print("*",end=" ")
            print()

    elif choice == 5:
        print("\nSelected Pattern: Pyramid")
        for i in range(1,rows+1):
            for j in range(rows-i):
                print(" ",end=" ")
            for j in range(2*i-1):
                print("*",end=" ")
            print()

    elif choice == 6:
        print("\nSelected Pattern: Inverted Pyramid")
        for i in range(rows,0,-1):
            for j in range(rows-i):
                print(" ",end=" ")
            for j in range(2*i-1):
                print("*",end=" ")
            print()

    elif choice == 7:
        print("\nSelected Pattern: Diamond")
        for i in range(1,rows+1):
            for j in range(rows-i):
                print(" ",end="")
            for j in range(2*i-1):
                print("*",end="")
            print()
        for i in range(rows-1,0,-1):
            for j in range(rows-i):
                print(" ",end="")
            for j in range(2*i-1):
                print("*",end="")
            print()

    elif choice == 8:
        print("\nSelected Pattern: Hollow Square")
        for i in range(rows):
            for j in range(rows):
                if i==0 or i==rows-1 or j==0 or j==rows-1:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()

    elif choice == 9:
        print("\nSelected Pattern: Hollow Right Triangle")
        for i in range(1,rows+1):
            for j in range(1,i+1):
                if i==1 or i==rows or j==1 or j==i:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()

    elif choice == 10:
        print("\nSelected Pattern: Hollow Pyramid")
        for i in range(1,rows+1):
            for j in range(rows-i):
                print(" ",end="")
            for j in range(1,2*i):
                if i==1 or i==rows or j==1 or j==2*i-1:
                    print("*",end="")
                else:
                    print(" ",end="")
            print()

    elif choice == 11:
        print("\nSelected Pattern: Hollow Diamond")
        for i in range(1,rows+1):
            for j in range(rows-i):
                print(" ",end="")
            for j in range(1,2*i):
                if i==1 or j==1 or j==2*i-1:
                    print("*",end="")
                else:
                    print(" ",end="")
            print()
        for i in range(rows-1,0,-1):
            for j in range(rows-i):
                print(" ",end="")
            for j in range(1,2*i):
                if i==1 or j==1 or j==2*i-1:
                    print("*",end="")
                else:
                    print(" ",end="")
            print()

    input("Press Enter to continue...")
