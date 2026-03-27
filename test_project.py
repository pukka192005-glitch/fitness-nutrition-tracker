from project import calculate_macros, search_food

def test_calculate_macros_basic():
    data = {
        "protein": 10,
        "calories": 100,
        "carbs": 20,
        "fat": 5
    }

    result = calculate_macros(data, 100)

    assert result["protein"] == 10
    assert result["calories"] == 100
    assert result["carbs"] == 20
    assert result["fat"] == 5


def test_calculate_macros_scaled():
    data = {
        "protein": 10,
        "calories": 100,
        "carbs": 20,
        "fat": 5
    }

    result = calculate_macros(data, 200)

    assert result["protein"] == 20
    assert result["calories"] == 200
    assert result["carbs"] == 40
    assert result["fat"] == 10



def test_search_food_found():
    database = {
        "paneer": {"protein": 18},
        "egg": {"protein": 13}
    }

    result = search_food("paneer", database)

    assert result == {"protein": 18}


def test_search_food_not_found():
    database = {
        "paneer": {"protein": 18}
    }

    result = search_food("pizza", database)

    assert result is None