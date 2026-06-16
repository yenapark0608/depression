import json #키워드 파일 읽기 위해 json 파일 읽는 기능 가져오기


def load_keywords(path="data/keywords.json"): #json 파일 파이썬에서 쓸 수 있는 형태로 만들어주는 함수로 load keyword 정의하기.
    with open(path, "r", encoding="utf-8") as f: #키워드 파일 읽고 f라는 변수에 내용 담기
        return json.load(f)


def match_keywords(tokens, keywords): #스크립트랑 키워드 맞춰보는 함수로 match keyword 정의하기. 이 함수에선 전처리한 스크립트랑 키워드 사용.
    matched = [] #매칭된 키워드를 담을 matched 라는 빈 리스트 생성
    seen = set() #키워드 중복 추가 안되게 하는 역할

    # 단어별 출현 빈도 계산
    freq = {} #단어별 등장 횟수를 담을 빈 딕셔너리 생성
    for token in tokens: #tokens 리스트에서 단어 하나씩 꺼내기
        freq[token] = freq.get(token, 0) + 1 #단어가 나올 때마다 횟수 1씩 올리기. 처음 나오는 단어면 0에서 시작.

    for token in tokens: #전처리된 스크립트 단어들 모여있는 tokens 리스트에서 단어들 하나씩 꺼내서 token이라는 변수에 저장.
        if token in seen: #이미 매칭한 단어면 건너뛰기
            continue
        for grade, data in keywords.items(): #키워드 파일에서 등급명이랑 그 내용을 각각 grade와 data라는 변수에 저장.
            if token in data["keywords"]: #키워드 내용들이 전처리한 스크립트 내용에 들어있다면
                count = freq[token] #해당 단어의 등장 횟수 가져오기
                matched.append({
                    "word": token,
                    "grade": grade,
                    "weight": data["weight"],
                    "count": count, #단어 등장 횟수
                    "total": data["weight"] * count #가중치 × 등장 횟수 = 최종 점수
                }) #그 단어, 등급, 가중치, 빈도수, 최종 점수를 한데 묶기
                seen.add(token) #매칭된 단어 seen에 추가해서 중복 방지
    return matched