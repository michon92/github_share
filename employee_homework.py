class Employee:
    """Pobiera dane prcowników"""
    def __init__(self, first_name, last_name, salary):
        self.first = first_name
        self.last = last_name
        self.salary = salary

    def give_raise(self, salary_raise=5000):
        """Określa podwyżkę dla pracownika"""
        self.salary += salary_raise
