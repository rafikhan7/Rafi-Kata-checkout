import unittest
from tests import *


if __name__ == '__main__':
    test_suite = unittest.TestLoader().loadTestsFromTestCase(TestCheckout)
    test_result = unittest.TextTestRunner().run(test_suite)

    # Count passing test cases
    passed_count = test_result.testsRun - len(test_result.failures) - len(test_result.errors)
    print(f"{passed_count} test cases passed.")
