import sys
import unittest
sys.path.append(r'C:\Users\EMG\Documents\Bug-Tracker-Report\test')
from test_new_customer import TestNewCustomerCreation
from test_edit_customer import TestEditCustomerCreation
from test_delete_customer import TestDeleteCustomer
from test_new_account import TestNewAccount

def main_menu():
    print("===== Test Menu =====")
    print("1. Test New Customer")
    print("2. Test Edit Customer")
    print("3. Test Delete Customer")
    print("4. Test New Account")
    # Add more options for other test classes
    print("0. Exit")
    print("=====================")

if __name__ == "__main__":
    while True:
        main_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestNewCustomerCreation))
        elif choice == "2":
            unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestEditCustomerCreation))
        elif choice == "3":
            unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestDeleteCustomer))
        elif choice == "4":
            unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestNewAccount))
        # Add more cases for other test classes
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please enter a valid option.")