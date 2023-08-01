import unittest
# from new_customer_test import TestNewCustomer
# from edit_customer_test import TestEditCustomer


def test_suite():
    # Create a test suite
    suite = unittest.TestSuite()

    # Add individual test cases to the suite
    # suite.addTest(unittest.makeSuite(TestNewCustomer))
    # suite.addTest(unittest.makeSuite(TestEditCustomer))


    return suite

if __name__ == "__main__":
    # Run the test suite
    runner = unittest.TextTestRunner()
    test_suite = test_suite()
    runner.run(test_suite)