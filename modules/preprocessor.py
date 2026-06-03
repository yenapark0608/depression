from kiwipiepy import Kiwi
import re

kiwi = Kiwi()

def load_stopwords(path="data/stopwords.txt"):
    with open(path, "r", encoding="utf-8") as f:
        return set(line.strip() for line in f if line.strip())

def extract_patient_speech(script):
    lines = script.split("\n")
    patient_lines = []
    for line in lines:
        if re.match(r"^내담자\s*:", line):
            text = re.sub(r"^내담자\s*:", "", line)
            patient_lines.append(text.strip())
    return " ".join(patient_lines)

def clean_text(text):
    text = re.sub(r"[^\w\s가-힣]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

def extract_morphs(text):
    tokens = kiwi.tokenize(text)
    allowed_pos = {"NNG", "NNP", "VA", "VV"}
    result = []
    for token in tokens:
        if token.tag in allowed_pos:
            word = token.form
            if token.tag in {"VA", "VV"}:
                word = word + "다"
            if len(word) > 1:
                result.append(word)
    return result

def remove_stopwords(tokens, stopwords):
    return [t for t in tokens if t not in stopwords]

def preprocess(script):
    stopwords = load_stopwords()
    patient_text = extract_patient_speech(script)
    cleaned = clean_text(patient_text)
    morphs = extract_morphs(cleaned)
    tokens = remove_stopwords(morphs, stopwords)
    return tokens