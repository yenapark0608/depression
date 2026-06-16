from flask import Flask, render_template, request
from modules.preprocessor import preprocess
from modules.matcher import load_keywords, match_keywords
from modules.scorer import calculate_score, get_grade

app = Flask(__name__)

@app.route('/')
def index(): #메인 페이지 렌더링
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze(): #스크립트 분석 함수
    script = request.form['script'] #입력받은 스크립트 가져오기
    tokens = preprocess(script) #전처리
    total_words = len(tokens) #전체 단어 수 계산
    keywords = load_keywords() #키워드 파일 불러오기
    matched = match_keywords(tokens, keywords) #키워드 매칭
    score = calculate_score(matched, total_words) #점수 계산 (total_words 추가)
    grade = get_grade(score) #등급 계산
    total_keywords = sum(len(data["keywords"]) for data in keywords.values()) #전체 키워드 수
    matched_count = len(matched) #감지된 키워드 수
    messages = {
        "정상": "현재 정상 범위입니다. 꾸준한 관심과 대화를 유지해주세요.",
        "주의": "경미한 우울 증상이 감지됩니다. 생활 습관 개선과 주기적인 상담을 권장합니다.",
        "위험": "중등도 우울 증상이 감지됩니다. 전문가 상담을 받아보시길 권장합니다.",
        "고위험": "심각한 우울 증상이 감지됩니다. 즉시 전문가 상담이 필요합니다."
    }
    message = messages[grade]
    return render_template('result.html',
        score=score,
        grade=grade,
        matched=matched,
        total_keywords=total_keywords,
        matched_count=matched_count,
        message=message
    )

if __name__ == '__main__':
    app.run(debug=True)