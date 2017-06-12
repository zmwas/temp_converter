import unittest
from temp_converter import convert_celcius_to_farenheit

class TempConverterTestCase(unittest.TestCase):


    def test_celcius_converted_to_farenheit(self):
        """
        F = C*9/5 +32

        """
        actual = convert_celcius_to_farenheit(10)
        expected = 50
        self.assertEqual(actual,expected,msg='The value is not converted to farenheit')
