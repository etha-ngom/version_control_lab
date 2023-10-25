def encoder(password):
    password = password.split()
    for index in range(len(password)):
        password[index] = int(password[index]) + 3
        if password[index] >= 10:
            password[index] -= 10
        password[index] = str(password[index])

    return "".join(password)

def decode():
    pass

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
            print("Decode has not been implemented yet.\n")

        # If the user wants to quit
        elif choice == 3:
            break


if __name__ == "__main__":
    main()