# Fitness & Nutrition Tracker (CS50P Final Project)

## Overview
A Python-based command-line application that tracks daily nutrition including protein, calories, carbohydrates, and fat using a CSV database of 200+ food items.

---

## Features
- Tracks multiple food entries
- Calculates macros based on quantity
- Real-time cumulative totals
- CSV-based food database (200+ items)
- Clean tabular output
- Unit tested using pytest

---

## Demo Video: https://www.youtube.com/watch?v=8LtFlnDzNwE

---

## How to Run:
1. Run the program: python project.py
2. Run tests: pytest test_project.py

---
**Project Structure**:
1. project.py (Main application logic)
2. test_project.py (Unit tests)
3. foods.csv (Food database)
4. README.md (Documentation)


**Skills Demonstrated:**
Python programming, Data handling using CSV, Problem solving, Modular programming and Unit testing

---
**Detailed Explanation:**

This Fitness & Nutrition Tracker is a simple command-line Python application that allows users to track their daily nutrition intake. You can enter the foods you eat in grams and the application will provide you with the total amount of protein, calories, carbs, and fat in your diet.

Food entries are stored in a database (CSV format) containing over 200 different types of food with corresponding nutritional values (per 100g). This data is loaded into memory to allow for quick and easy lookups in a dictionary.

The main loop of the application will allow the user to continue entering food entries until they input the word "done." After entering the food item, the application will use the food entry to search through the database and then calculate the nutritional values using the input amount (by scaling).

The user will have access to a structured and organized view of their meals with appropriate cumulative totals, allowing for easy tracking of overall dietary intake.

This project demonstrates practical usage of Python fundamentals including file handling, data structures, loops, functions, and testing, and reflects an effort toward building real-world, data-driven applications.
