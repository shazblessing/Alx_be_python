def main():
    #Prompt the User for Pattern Size
    size = int(input("Enter the size of the pattern: ")) 

    #Initialize row counter
    row = 0

    #Draw the pattern using while loop
    while row < size:
        print("*", end="")

    #Print a new line after completing the row

    print()

    #Increment thr row counter
    row += 1

if __name__ == "__main__":
    main()
    