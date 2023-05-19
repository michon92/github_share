# Zadanie 11.1*
import unittest
from city_function import get_formatted_city


class CityTestCase(unittest.TestCase):
    """test dla programu city_function.py"""

    def test_city_country(self):
        """Czy wprowadzane dane w postaci 'Kraków, Polska' będą prawidłowe?"""
        formatted_city = get_formatted_city('kraków', 'polska')
        self.assertEqual(formatted_city, 'Kraków, Polska')

    def test_city_country_population(self):
        """Czy date 'santiago', 'chile' i 'population=5000000' będą OK?"""
        formatted_city = get_formatted_city('santiego', 'chile', '5000000')
        self.assertEqual(formatted_city, 'Santiego, Chile, Populacja: 5000000')


if __name__ == '__main__':
    unittest.main()
