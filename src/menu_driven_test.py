def display_menu():
    print("===== Test Menu =====")
    print("1. Test New Customer")
    print("2. Test Edit Customer")
    print("3. Test Delete Customer")
    print("4. Test New Account")
    print("5. Test Edit Account")
    print("6. Test Delete Account")
    print("7. Test Balance Enquiry")
    print("8. Test Mini Statement")
    print("9. Test Customized Statement")
    print("0. Exit")
    print("=====================")

def menu_driven_test():
    while True:
        display_menu()
        choice = input("Enter your choice (0-9): ")

        if choice == "1":
            print("Testing New Customer functionality...")
            # test_new_customer_creation()
        elif choice == "2":
            print("Testing Edit Customer functionality...")
            # test_edit_customer()

if __name__ == "__main__":
    menu_driven_test()