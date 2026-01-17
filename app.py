"""
SonarQube Demo Application - Intentionally contains various code issues
"""

import os
import sys
import hashlib
import pickle
import random

# Security Issue: Hard-coded credentials
DATABASE_PASSWORD = "admin123"
API_KEY = "sk-1234567890abcdef"

# Code Smell: Unused variable
unused_variable = "This is never used"


class UserManager:
    """User management with multiple issues"""
    
    def __init__(self):
        self.users = []
        self.admin_password = "password123"  # Security: Hard-coded password
    
    # Bug: Mutable default argument
    def add_user(self, name, roles=[]):
        user = {"name": name, "roles": roles}
        self.users.append(user)
        return user
    
    # Security: SQL Injection vulnerability
    def find_user_by_name(self, name):
        query = "SELECT * FROM users WHERE name = '" + name + "'"
        # This would execute unsafe SQL
        return query
    
    # Code Smell: Too many return statements
    def validate_password(self, password):
        if len(password) < 8:
            return False
        if not any(c.isupper() for c in password):
            return False
        if not any(c.islower() for c in password):
            return False
        if not any(c.isdigit() for c in password):
            return False
        if not any(c in "!@#$%^&*" for c in password):
            return False
        return True
    
    # Security: Insecure deserialization
    def load_user_data(self, filename):
        with open(filename, 'rb') as f:
            data = pickle.load(f)  # Dangerous!
        return data
    
    # Bug: Except block too broad
    def get_user_data(self, user_id):
        try:
            user = self.users[user_id]
            return user
        except:  # Too broad exception
            pass


# Code Smell: Function with too many parameters
def create_user_profile(username, email, first_name, last_name, age, 
                       country, city, street, postal_code, phone, 
                       company, position):
    return {
        "username": username,
        "email": email,
        "first_name": first_name,
        "last_name": last_name,
        "age": age,
        "country": country,
        "city": city,
        "street": street,
        "postal_code": postal_code,
        "phone": phone,
        "company": company,
        "position": position
    }


# Code Smell: Cognitive Complexity too high
def complex_function(data, flag1, flag2, flag3):
    result = []
    
    if flag1:
        if flag2:
            if flag3:
                for item in data:
                    if item > 0:
                        if item % 2 == 0:
                            if item < 100:
                                result.append(item * 2)
                            else:
                                result.append(item)
                        else:
                            if item < 50:
                                result.append(item + 1)
                            else:
                                result.append(item - 1)
                    else:
                        if abs(item) > 10:
                            result.append(abs(item))
            else:
                for item in data:
                    result.append(item)
        else:
            for item in data:
                if item != 0:
                    result.append(item)
    else:
        result = data
    
    return result


# Security: Weak cryptographic hash
def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()  # MD5 is insecure!


# Bug: Division by zero possibility
def calculate_average(numbers):
    total = sum(numbers)
    return total / len(numbers)  # What if numbers is empty?


# Code Smell: Dead code
def old_function():
    print("This function is never called")
    return "dead code"


# Code Smell: Duplicate code
def process_data_type_a(data):
    result = []
    for item in data:
        if item > 0:
            result.append(item * 2)
        else:
            result.append(0)
    return result


def process_data_type_b(data):
    result = []
    for item in data:
        if item > 0:
            result.append(item * 2)
        else:
            result.append(0)
    return result


# Security: Command injection vulnerability
def execute_command(user_input):
    command = "ls " + user_input
    os.system(command)  # Dangerous!


# Bug: Comparison with None using ==
def check_value(value):
    if value == None:  # Should use 'is None'
        return False
    return True


# Code Smell: Too many local variables
def process_order():
    customer_name = "John"
    customer_email = "john@example.com"
    customer_phone = "123456789"
    customer_address = "123 Main St"
    product_name = "Widget"
    product_price = 19.99
    product_quantity = 5
    tax_rate = 0.08
    shipping_cost = 5.99
    discount_code = "SAVE10"
    discount_amount = 2.00
    subtotal = product_price * product_quantity
    tax = subtotal * tax_rate
    total = subtotal + tax + shipping_cost - discount_amount
    order_date = "2026-01-17"
    order_status = "pending"
    
    return total


# Security: Eval usage
def calculate_expression(expr):
    return eval(expr)  # Extremely dangerous!


# Bug: Modifying list while iterating
def remove_negatives(numbers):
    for num in numbers:
        if num < 0:
            numbers.remove(num)  # Dangerous pattern
    return numbers


# Code Smell: Print statements (should use logging)
def debug_function(x, y):
    print("Starting debug function")
    print(f"x = {x}")
    print(f"y = {y}")
    result = x + y
    print(f"result = {result}")
    return result


# Code Smell: Magic numbers
def calculate_price(base_price):
    if base_price > 100:
        return base_price * 0.85  # What is 0.85?
    elif base_price > 50:
        return base_price * 0.90  # What is 0.90?
    else:
        return base_price * 0.95  # What is 0.95?


# Main execution
if __name__ == "__main__":
    print("SonarQube Demo Application")
    
    # Using the problematic code
    manager = UserManager()
    manager.add_user("Alice")
    
    # This will crash if list is empty
    numbers = [1, 2, 3, 4, 5]
    avg = calculate_average(numbers)
    
    # Insecure password hashing
    hashed = hash_password("mypassword")
    
    print("Application completed")
