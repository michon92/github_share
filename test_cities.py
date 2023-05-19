# Zadanie 11.1*

import unittest
from city_function import get_formatted_city


class CityTestCase(unittest.TestCase):
    """test dla programu city_function.py"""

    def test_city_country(self):
        """Czy wprowadzane dane w postaci 'Kraków, Polska' będą prawidłowe?"""
        formatted_city = get_formatted_city('kraków', 'polska')
        self.assertEqual(formatted_city, 'Kraków, Polska')


if __name__ == '__main__':
    unittest.main()
