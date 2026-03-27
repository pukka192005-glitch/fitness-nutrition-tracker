import csv

FOOD_FILE = "foods.csv"

def main():
    print("Welcome to the Fitness & Nutrition Tracker")
    print("Please give the name of the food")
    print("And don't forget to add the grams :), to get the exact measure")
    print("If you are done with calculating total, say: DONE")

    database = load_food_database()

    meals = []
    total_protein = 0
    total_calories = 0
    total_carbs = 0
    total_fat = 0

    while True:
        food = input("Enter food (or type 'done'): ").lower().strip()

        if food == "done":
            print_table(meals, total_protein, total_carbs, total_fat, total_calories)
            print("Thank you for using the tracker!")
            break   

        data = search_food(food, database)

        if data is None:
            print("Food not found")
            continue

        
        try:
            grams = float(input("Enter the grams you ate: "))
        except:
            print("Please enter a valid number")
            continue

        macros = calculate_macros(data, grams)

        meal = {
            "food": food,
            "grams": grams,
            "protein": macros["protein"],
            "carbs": macros["carbs"],
            "fat": macros["fat"],
            "calories": macros["calories"]
        }

        meals.append(meal)

        total_protein += macros["protein"]
        total_calories += macros["calories"]
        total_carbs += macros["carbs"]
        total_fat += macros["fat"]

        print(f"{food} added successfully!\n")

        
        print_table(meals, total_protein, total_carbs, total_fat, total_calories)


def load_food_database():
    database = {}

    with open(FOOD_FILE, "r") as file:   
        reader = csv.DictReader(file)

        for row in reader:
            food_name = row["food"].lower()

            database[food_name] = {
                "protein": float(row["protein"]),   
                "calories": float(row["calories"]),
                "carbs": float(row["carbs"]),
                "fat": float(row["fat"])
            }

    return database


def search_food(x, y):
    if x in y:
        return y[x]
    else:
        return None


def calculate_macros(data, grams):
    protein = (data["protein"] * grams) / 100
    calories = (data["calories"] * grams) / 100
    carbs = (data["carbs"] * grams) / 100
    fat = (data["fat"] * grams) / 100

    return {
        "protein": protein,
        "calories": calories,
        "carbs": carbs,
        "fat": fat
    }


def print_table(meals, total_protein, total_carbs, total_fat, total_calories):
    print("\n" + "-" * 65)
    print(f"{'Food':<20}{'Protein':<10}{'Carbs':<10}{'Fat':<10}{'Calories':<10}")
    print("-" * 65)

    for meal in meals:
        print(f"{meal['food']:<20}{meal['protein']:<10.1f}{meal['carbs']:<10.1f}{meal['fat']:<10.1f}{meal['calories']:<10.1f}")

    print("-" * 65)
    print(f"{'TOTAL':<20}{total_protein:<10.1f}{total_carbs:<10.1f}{total_fat:<10.1f}{total_calories:<10.1f}")
    print("-" * 65 + "\n")


if __name__ == "__main__":
    main()