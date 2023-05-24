import unittest
from employee_homework import Employee

class TestEmployee(unittest.TestCase):
    """Testy dla klasy Employee"""

    def setUp(self):
        """Utworzenie danych jednego pracownika do
        zastosowania we wszystkich testach"""
        self.test_employee = Employee('michal', 'koduje', 50000)

    def test_default_raise(self):
        """Test dla standardowej podwyżki o 5K"""
        self.test_employee.give_raise()
        self.assertEqual(self.test_employee.salary, 55000)

    def test_custom_raise(self):
        """Test dla  podwyżki o 3K"""
        self.test_employee.give_raise(3000)
        self.assertEqual(self.test_employee.salary, 53000)


if __name__ == '__main__':
    unittest.main()

