#!/usr/bin/python3
"""
Create a TestAccessNestedMap class that inherits from unittest.TestCase.

Implement the TestAccessNestedMap.test_access_nested_map method 
to test that the method returns what it is supposed to.

Decorate the method with @parameterized.expand 
to test the function for following inputs:
nested_map={"a": 1}, path=("a",)
nested_map={"a": {"b": 2}}, path=("a",)
nested_map={"a": {"b": 2}}, path=("a", "b")
"""
import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """ A unittest test case"""
    
    @parameterized.expand([
        ({'a': 1}, 'a', 1),
        ({"a": {"b": 2}}, 'a', 2),
        ({"a": {"b": 2}}, ('a', 'b'), 2)
        ])
    def test_access_nested_map(self, nested_map, path, expected):
        """_summary_
        """
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected)
