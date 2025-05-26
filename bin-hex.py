def keep_on_or_not():
    while True:
        continue_choice = input("\nDo you want to continue (yes - no) ? ")
        if continue_choice == 'yes' or continue_choice == 'YES':
            make_choice()
        elif continue_choice == 'no' or continue_choice == 'NO':
            break
        else:
            keep_on_or_not()


def make_choice():
    print("-----------------------------------------------------------------")
    print("Do you want to convert in :\n- binary (b)\n- hexadecimal (h)")
    user_choice = input("Please enter your choice ('b' ou 'h') : ")

    while user_choice != 'b' and user_choice != 'h':
        user_choice = input("Invalid choice....... Please restart : ")


    if user_choice == 'b':
        print("--------------------------------------")
        print("BINARY CONVERSION")
        num_str = input("Enter your number (decimal) : ")
        try:
            num = int(num_str)
        except ValueError:
            print("IMPOSSIBLE to convert your entry into an integer !")
        else:
            rest_list = []

            for i in range(num+1):
                rest = num % 2
                if num == 0:
                    break
                if rest < 2:
                    rest_list.append(rest)
                    num = num // 2
                bin_conversion = rest_list

            for j in bin_conversion[::-1]:
                print(j, end='')
    else:
        print("--------------------------------------")
        print("HEXADECIMAL CONVERSION")
        num_str = input("Enter your number (decimal) : ")
        try:
            num = int(num_str)
        except ValueError:
            print("IMPOSSIBLE to convert your entry into an integer !")
        else:
            print(hex(num)[2:].upper())


make_choice()
keep_on_or_not()

print("\n\n----------END OF OUR PROGRAM----------\n")
