import unittest

# Leetcode 678
def is_balanced(s: str):
    left_min, left_max = 0,0
    for char in s:
        if char == '(':
            left_min += 1
            left_max += 1
        elif char == ')':
            left_min -= 1
            left_max -= 1
        elif char == '*':
            left_min -= 1
            left_max += 1
        if left_max < 0:
            return False
        left_min = max(left_min, 0)
    return left_min == 0

class TestAddition(unittest.TestCase):
    def test_addition(self):
        test_cases = [
            ("", True),
            ("()", True),
            ("(()", False),
            ("(*", True),
            ("((*", False),
        ]
        
        for a, expected in test_cases:
            with self.subTest(a=a):
                result = is_balanced(a)
                self.assertEqual(result, expected)

