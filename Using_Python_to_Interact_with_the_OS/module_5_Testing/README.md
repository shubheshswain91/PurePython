# unittest
A unittest provides developers with a set of tools to construct and run tests. These tests can be run on individual components or by isolating units of code to ensure their correctness. By running unittests, developers can identify and fix any bugs that appear, creating a more reliable code. In this reading, you will learn about unittest concepts, how to use and when to use them, and view an example along the way.

Concepts
Unittest relies on the following concepts:

Test fixture: This refers to preparing to perform one or more tests. In addition, test fixtures also include any actions involved in testing cleanup. This could involve creating temporary or proxy databases, directories, or starting a server process.

Test case: This is the individual unit of testing that looks for a specific response to a set of inputs. If needed, TestCase is a base class provided by unittest and can be used to create new test cases.

Test suite: This is a collection of test cases, test suites, or a combination of both. It is used to compile tests that should be executed together.

Test runner: This runs the test and provides developers with the outcome’s data. The test runner can use different interfaces, like graphical or textual, to provide the developer with the test results. It can also provide a special value to developers to communicate the test results. 