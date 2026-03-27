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

## How to Run

1. Run the program: python project.py

2. Run tests: pytest test_project.py

Project Structure
project.py          # Main application logic
test_project.py     # Unit tests
foods.csv           # Food database
README.md           # Documentation

Skills Demonstrated
Python programming
Data handling using CSV
Problem solving
Modular programming
Unit testing

Detailed Explanation:
The Fitness & Nutrition Tracker is a command-line Python application designed to help users monitor their daily nutritional intake in a simple and efficient way. The program allows users to input the foods they consume along with their quantities in grams, and it calculates the corresponding nutritional values including protein, calories, carbohydrates, and fat.

The application uses a CSV file as its database, which contains over 200 food items along with their nutritional values per 100 grams. This data is loaded into memory and stored in a dictionary for efficient lookup.

The main function controls an interactive loop where the user continuously inputs food items until they type "done". The program then searches for the food in the database and calculates macros using a scaling formula based on the input quantity.

Each meal is stored and displayed in a structured table along with cumulative totals, making it easy to track overall daily intake.

The project follows a modular design with separate functions for loading data, searching foods, calculating macros, and displaying results. Unit tests have also been implemented using pytest to ensure correctness and reliability.

This project demonstrates practical usage of Python fundamentals including file handling, data structures, loops, functions, and testing, and reflects an effort toward building real-world, data-driven applications.
