# Creation of a function which asks to user if he wants to keep on or not
def keep_on_or_not():
    while True:
        continue_choice = input("\nDo you want to continue (yes - no) ? ")
        if continue_choice == 'yes' or continue_choice == 'YES':
            make_choice()
        elif continue_choice == 'no' or continue_choice == 'NO':
            break
        else:
            keep_on_or_not()


# Creation of a main fuction which manages all about this code
def make_choice():
    print("-----------------------------------------------------------------")
    print("Do you want to convert in :\n- binary (b)\n- hexadecimal (h)")
    user_choice = input("Please enter your choice ('b' ou 'h') : ") # Asking about user choice

    # Verify that user respects rules
    while user_choice != 'b' and user_choice != 'h':
        user_choice = input("Invalid choice....... Please restart : ")


    if user_choice == 'b': # First condition : user wants to convert in binary
        print("--------------------------------------")
        print("BINARY CONVERSION")
        num_str = input("Enter your number (decimal) : ")
        # I use try / except condition to avoid errors
        try:
            num = int(num_str)
        except ValueError:
            print("IMPOSSIBLE to convert your entry into an integer !")
            make_choice() # And here i revive the code
        else:
            rest_list = []

            for i in range(num+1): # I am not using my 'i' variable (This is a big error in programming !)
                rest = num % 2
                if num == 0:
                    break
                if rest < 2:
                    rest_list.append(rest) # Stores only results
                    num = num // 2
                bin_conversion = rest_list

            for j in bin_conversion[::-1]: # Allows reverse reading 
                print(j, end='')
    else: # Second condition : user wants to convert in hexadecimal
        print("--------------------------------------")
        print("HEXADECIMAL CONVERSION")
        num_str = input("Enter your number (decimal) : ")
        try:
            num = int(num_str)
        except ValueError:
            print("IMPOSSIBLE to convert your entry into an integer !")
            make_choice()
        else:
            print(hex(num)[2:].upper())


# Call of functions
make_choice()
keep_on_or_not()

# Show my program end
print("\n\n----------END OF OUR PROGRAM----------\n")
