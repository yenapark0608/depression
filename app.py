from flask import Flask, render_template, request
from modules.preprocessor import preprocess
from modules.matcher import load_keywords, match_keywords
from modules.scorer import calculate_score, get_grade

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    script = request.form['script']
    tokens = preprocess(script)
    keywords = load_keywords()
    matched = match_keywords(tokens, keywords)
    score = calculate_score(matched)
    grade = get_grade(score)
    return render_template('result.html',
        score=score,
        grade=grade,
        matched=matched
    )

if __name__ == '__main__':
    app.run(debug=True)