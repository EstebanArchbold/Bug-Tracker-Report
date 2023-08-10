import sys
import unittest
sys.path.append(r'..\Bug-Tracker-Report\test')
from test_new_customer import TestNewCustomerCreation
from test_edit_customer import TestEditCustomerCreation
from test_delete_customer import TestDeleteCustomer
from test_new_account import TestNewAccount
from test_edit_account import TestEditAccount
from test_delete_account import TesDeleteCustomer
from test_balance_enquiry import TesBalanceEnquiry
from test_ministatement import TestMiniStatement



def main_menu():
    print("===== Test Menu =====")
    print("1. Test New Customer")
    print("2. Test Edit Customer")
    print("3. Test Delete Customer")
    print("4. Test New Account")
    print("5. Test Edit Account")
    print("6. Test Delete Account")
    print("7. Test Balance Enquiry")
    print("8. Test Mini Statement")
    print("9. Test Customised Statement")
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
        elif choice == "5":
            unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestEditAccount))
        elif choice == "6":
            unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TesDeleteCustomer))
        elif choice == "7":
            unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TesBalanceEnquiry))
        elif choice == "8":
            unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestMiniStatement))
        # elif choice == "9":
        #     unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestCustomisedStatement))
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please enter a valid option.")