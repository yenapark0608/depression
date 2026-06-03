def calculate_score(matched):
    total_score = 0
    for item in matched:
        total_score += item["weight"]
    return total_score

def get_grade(score):
    if score <= 20:
        return "정상"
    elif score <= 50:
        return "주의"
    elif score <= 80:
        return "위험"
    else:
        return "고위험"