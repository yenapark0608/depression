def calculate_score(matched, total_words):  #점수 계산용 함수. matched(매칭된 키워드)와 total_words(전체 단어 수) 매개변수 사용.
    raw_score = 0 #raw_score 변수는 키워드 가중치 합산용 변수. 0으로 초기화하기.
    for item in matched: #matched 변수의 리스트 안에 있는 항목들을 item 변수에 넣기
        raw_score += item["total"] #item에 있는 항목들 중 빈도 반영된 최종 점수(total)를 꺼내 raw_score 변수에 합산시키기.

    # 전체 단어 수 기준으로 비율 계산 (스크립트 길이 영향 제거)
    if total_words == 0: #전체 단어 수가 0이면 0 반환 (0으로 나누는 오류 방지)
        return 0
    score_per_100 = (raw_score / total_words) * 100 #100단어당 점수로 환산
    return round(score_per_100, 1) #소수점 1자리까지 반환

def get_grade(score): #등급 계산용 함수. score 변수 사용.
    if score < 1.5:
        return "정상"   #100단어당 1.5점 미만이면 정상
    elif score < 1.8:
        return "주의"   #100단어당 1.5점 이상 1.8점 미만이면 주의
    elif score < 4:
        return "위험"   #100단어당 1.8점 이상 4점 미만이면 위험
    else:
        return "고위험" #100단어당 4점 이상이면 고위험