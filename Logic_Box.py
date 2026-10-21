print("Welcome to the pattern generator and number analyzer!")

while (True):
    print("\nSelect an option:")
    print("1. Generate a pattern")
    print("2. Analyze a Range of Numbers")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    match choice:
        case 1:
            rows = int(input("Enter number of rows for the pattern: "))
            print("pattern:")

            for i in range(1, rows + 1):
                print("*" *i)

        case 2:
            start = int(input("Enter the start of the range: "))
            end = int(input("Enter the end of the range: "))
            total = 0

            for num in range(start, end + 1):
                if num % 2 == 0:
                    print(num, "is Even")
                else:
                    print(num, "is Odd")

                total = total + num

            print("Sum of all numbers:", total)

        case 3:
            print("Thank you! Goodbye!")
            break

        case _:
            print("Invalid choice! Please try again.")
