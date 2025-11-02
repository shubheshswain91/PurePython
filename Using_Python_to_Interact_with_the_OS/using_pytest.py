""" 
Pytest fixtures
Fixtures are used to separate parts of code that only run for tests. They are reusable pieces of test setups and teardown code that are shared across multiple tests. Fixtures benefit developers by assisting in keeping their tests clean and avoiding code duplication. Let’s look at an example of using a pytest in Python:

 """

# Importing the math and pytest libraries
import math
import pytest

# Creating the common function for input
@pytest.fixture
def input_value():
   input = 8
   return input

# Creating first test case
def test_check_difference(input_value):
   assert 99-93==input_value

# Creating second test case
def test_check_square_root(input_value):
   assert input_value==math.sqrt(64)




