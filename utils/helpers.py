def apply_margin(price, margin=0.2):
    return price * (1 + margin)

def get_confidence_score(task):
    low_confidence_keywords = ["maybe", "possibly", "consider"]
    for word in low_confidence_keywords:
        if word in task.lower():
            return 0.5
    return 0.9

def adjust_city_factor(price, city):
    city_factor = {
        "marseille": 1.0,
        "paris": 1.2,
        "lyon": 1.1
    }
    return price * city_factor.get(city.lower(), 1.0)
