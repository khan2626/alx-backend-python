#!/usr/bin/env python3
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
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch, Mock


class TestAccessNestedMap(unittest.TestCase):
    """ A unittest test case"""
    
    @parameterized.expand([
        ({'a': 1}, 'a', 1),
        ({"a": {"b": 2}}, ('a','b'), 2),
        ({"a": {"b": 2}}, ('a', 'b'), 2)
        ])

    def test_access_nested_map(self, nested_map, path, expected):
        """_summary_
        """
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected)
        
        @parameterized.expand([
            ({}, 'a', KeyError),
            ({'a': 1}, ('a', 'b'), KeyError)
            ])
        def test_access_nested_map_exception(self, nested_map, path, expected):
            """_summary_
            """
            with self.assertRaises(expected) as cm:
                accesss_nested_map(nested_map, path)

class TestGetJson(unittest.TestCase):
    """Familiarize yourself with the utils.get_json function.
    Define the TestGetJson(unittest.TestCase) class and implement the 
    TestGetJson.test_get_json method to test that utils.get_json 
    returns the expected result.

    We don’t want to make any actual external HTTP calls. 
    Use unittest.mock.patch to patch requests.get. Make sure it 
    returns a Mock object with a json method that returns test_payload 
    which you parametrize alongside the test_url that you will 
    pass to get_json with the following inputs:
    test_url="http://example.com", test_payload={"payload": True}
    test_url="http://holberton.io", test_payload={"payload": False}
    """

    @parameterized.expand([
        ('http://example.com', {'payload': True}),
        ('http://holberton.io', {'payload': False})
        ])
    def test_get_json(self, url, expected_output):
        """_summary_
        """
        mock_response = Mock()
        mock_response.json.return_value = expected_output
        with patch('requests.get', return_value=mock_response):
            response = get_json(url)

            self.assertEqual(response, expected_output)


class TestMemoize(unittest.TestCase):
    """_summary_

    Args:
                    unittest (_type_): _description_
    """

    def test_memoize(self):
        """_summary_

        Returns:
                _type_: _description_
        """

        class TestClass:
            """_summary_
            """

            def a_method(self):
                """_summary_

                Returns:
                        _type_: _description_
                """
                return 42

            @memoize
            def a_property(self):
                """_summary_

                Returns:
                        _type_: _description_
                """
                return self.a_method()

        test_obj = TestClass()

        with patch.object(test_obj, 'a_method') as mock_method:
            mock_method.return_value = 42

            result1 = test_obj.a_property
            result2 = test_obj.a_property

            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)
            mock_method.assert_called_once()
