class_static_methods_demo.p
# class_static_methods_demo.py

class Calculator:
    """
    A class demonstrating the use of class and static methods.
    """
    # Define a class attribute
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """
        A static method that adds two numbers.
        It does not have access to the class or instance.
        """
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """
        A class method that multiplies two numbers.
        It has access to the class itself (cls) but not a specific instance.
        """
        # Access the class attribute using the cls parameter
        print(f"Calculation type: {cls.calculation_type}")
        return a * b

