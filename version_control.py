def encoder(password):
    # Split the password from a string to a list so I can loop through it
    password = list(password)

    # Loop through the indeces of the password
    for index in range(len(password)):
        # The number at the index += 3
        password[index] = int(password[index]) + 3
        # If adding 3 makes the number greater than or equal to 10, subtract 10
        if password[index] >= 10:
            password[index] -= 10
        password[index] = str(password[index])

    # Return the password as a string
    return "".join(password)

def decode(password):
    # encoder(password)
    # for i in encoder(password):
    #     list = []
    list = []
    newlist = []
    for letter in password:
        list.append(letter)
    for i in list:
        add = -3
        i = int(i)
        add += i
        # print(add, end="")
        newlist.append(add)

    final = ''.join(map(str, newlist))

    return final

def main():
    stored_pass = False
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit\n")

        choice = int(input("Please enter an option: "))

        # If the user wants to encode
        if choice == 1:
            pass_to_encode = input("Please enter your password to encode: ")
            stored_pass = encoder(pass_to_encode)
            print("Your password has been encoded and stored!\n")

        # If the user wants to decode
        elif choice == 2:
            # print("Decode has not been implemented yet.\n")
            print(f"The decoded password is {encoder(pass_to_encode)}, and the original password is {decode(encoder(pass_to_encode))}.")

        # If the user wants to quit
        elif choice == 3:
            break


if __name__ == "__main__":
    main()