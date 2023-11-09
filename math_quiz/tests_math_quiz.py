import unittest
from math_quiz import random_int, random_operator, function_C


class TestMathGame(unittest.TestCase):

    def test_random_int(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = random_int(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_random_operator(self):
        #test if the random operator is 1 of the operators given
        operators = ['+', '-', '*']
        for _ in range(1000):  # Test a large number of random values
            rand_operator = random_operator()
            self.assertIn(rand_operator, operators)
            
            
    def test_perform_operation(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (11, 4, '-', '10-4', 11),
                (5, 6, '*', '5*6' , '30')
            ]
            #test if expected answer is same as output answer from code
            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                problem, answer = perform_operation(num1, num2, operator)
                self.assertEqual(problem, expected_problem)
                self.assertEqual(answer, expected_answer)

if __name__ == "__main__":
    unittest.main()
