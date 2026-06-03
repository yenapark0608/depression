import json


def load_keywords(path="data/keywords.json"):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def match_keywords(tokens, keywords):
    matched = []
    seen = set()
    for token in tokens:
        if token in seen:
            continue
        for grade, data in keywords.items():
            if token in data["keywords"]:
                matched.append({
                    "word": token,
                    "grade": grade,
                    "weight": data["weight"]
                })
                seen.add(token)
    return matched