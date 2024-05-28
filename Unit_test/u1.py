#  a Python unit test program to check if a given number is prime or not.

import unittest

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

# Define a test case class 'PrimeNumberTestCase' that inherits from 'unittest.Testcase'

class PrimeNumberTestCase(unittest.TestCase):
     # Define a test method 'test_prime_numbers' to test prime numbers.
     def test_prime_numbers(self):
        prime_numbers = [2,3,5,7,11,13,17,19,23,29,31]
        print("Prime numbers: ", prime_numbers)
        # Iterate through prime numbers and assert that they are recognised as prime.
        for number in prime_numbers:
            self.assertTrue(is_prime(number),f"{number} is not recognised as a prime number")

     def test_non_prime_numbers(self):
         non_prime_numbers = [4,6,8,9,10,12,14,16,18,20]
         print("Non-prime numbers: ", non_prime_numbers)
         for number in non_prime_numbers:
             self.assertFalse(is_prime(number),f"{number} is incorrectly recognised as a prime number")

if __name__ == '__main__':
    unittest.main()             
                
