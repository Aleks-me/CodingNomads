'''
Demonstrate your knowledge of unittest by first creating a function
with input parameters and a return value.

Once you have a function, write at least two tests for the function
that use various assertions. The test should pass.

Also include a test that does not pass.

'''
import unittest


# It will be much better if this function will be imported:
def subtract_divide(dividend, x, y):
    try:
        z = x - y
        return dividend / z
    except ZeroDivisionError as zde:
        raise zde


class TestMarathon(unittest.TestCase):
    def test_subtract_divide(self):
        self.assertEqual(subtract_divide(2, 5, 3), 1)

    def test_raises_zde(self):
        self.assertRaises(ZeroDivisionError, subtract_divide, 2, 2, 2)

    def test_calculation(self):
        self.assertTrue(subtract_divide(10, 5, 3) == 4)


# If not providing __nain__ call, then script could be
# tested by running: python -m unittest test_general.py (or run -m unittest...)
if __name__ == "__main__":
    unittest.main()
