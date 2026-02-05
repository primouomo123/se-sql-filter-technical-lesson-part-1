import sqlite3 
import pandas as pd

conn = sqlite3.connect('data.sqlite')

# Entire employees table
employees = pd.read_sql("""
SELECT *
  FROM employees;
""", conn)
print(employees)

# Employees with last name "Patterson"
print(pd.read_sql("""
SELECT *
  FROM employees
 WHERE lastName = "Patterson";
""", conn))

# First name, last name, and email of employees with last name "Patterson"
print(pd.read_sql("""
SELECT firstName, lastName, email
  FROM employees
 WHERE lastName = "Patterson";
""", conn))

# Employees with first name length of 5
print(pd.read_sql("""
SELECT *, length(firstName) AS name_length
  FROM employees
 WHERE name_length = 5;
""", conn))

# Employees with first name starting with "L"
print(pd.read_sql("""
SELECT *, substr(firstName, 1, 1) AS first_initial
  FROM employees
 WHERE first_initial = "L";
""", conn))

# This will get an error because L is not in quotes
'''print(pd.read_sql("""
SELECT *, substr(firstName, 1, 1) AS first_initial
  FROM employees
 WHERE first_initial = L;
""", conn))'''

# Order details with priceEach rounded to nearest integer equal to 30
print(pd.read_sql("""
SELECT *, CAST(round(priceEach) AS INTEGER) AS rounded_price_int
  FROM orderDetails
 WHERE rounded_price_int = 30;
""", conn))

# Orders placed in January of any year
print(pd.read_sql("""
SELECT *, strftime("%m", orderDate) AS month
  FROM orders
 WHERE month = "01";
""", conn))

# Orders that were shipped late
print(pd.read_sql("""
SELECT *, julianday(shippedDate) - julianday(requiredDate) AS days_late
  FROM orders
 WHERE days_late > 0;
""", conn))

conn.close()