"""
우울증 진단 프로그램 - 메인 실행 파일
사용법: python main.py
"""

import sys
import os

# src 디렉토리를 경로에 추가
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from classifier import DepressionClassifier


def print_menu():
    """메뉴 출력"""
    print("""
╔════════════════════════════════════════════════════════════╗
║          우울증 선별 진단 프로그램 v1.0                    ║
╚════════════════════════════════════════════════════════════╝

【 메인 메뉴 】

1. CSV 파일 분석 (대량 데이터)
2. 단일 텍스트 분석
3. 종료

선택해주세요 (1-3):""")


def analyze_csv():
    """CSV 파일 분석"""
    print("\n【 CSV 파일 분석 】\n")
    
    csv_path = input("CSV 파일 경로를 입력하세요 (기본값: data/sample_transcripts.csv): ").strip()
    if not csv_path:
        csv_path = 'data/sample_transcripts.csv'
    
    classifier = DepressionClassifier()
    
    # CSV 로드
    transcripts = classifier.load_transcripts_from_csv(csv_path)
    
    if not transcripts:
        print("분석할 데이터가 없습니다.")
        return
    
    # 분류
    print("\n분석 진행 중...\n")
    results = classifier.classify_batch(transcripts)
    
    # 결과 저장
    print("\n결과 저장 중...\n")
    classifier.save_results_to_json(results)
    classifier.save_results_to_csv(results)
    
    # 요약 보고서 출력
    summary = classifier.generate_summary_report(results)
    print(summary)
    
    # 결과 파일 출력 여부
    save_summary = input("\n요약 보고서를 파일로 저장하시겠습니까? (y/n): ").strip().lower()
    if save_summary == 'y':
        try:
            os.makedirs('results', exist_ok=True)
            with open('results/summary_report.txt', 'w', encoding='utf-8') as f:
                f.write(summary)
            print("✓ 요약 보고서를 저장했습니다: results/summary_report.txt")
        except Exception as e:
            print(f"✗ 저장 중 오류 발생: {e}")


def analyze_single_text():
    """단일 텍스트 분석"""
    print("\n【 단일 텍스트 분석 】\n")
    
    print("상담 스크랩트를 입력하세요. (여러 줄 가능, 'END'를 입력하면 종료):")
    print("-" * 50)
    
    lines = []
    while True:
        line = input()
        if line.strip().upper() == 'END':
            break
        lines.append(line)
    
    text = '\n'.join(lines)
    
    if not text.strip():
        print("입력된 텍스트가 없습니다.")
        return
    
    classifier = DepressionClassifier()
    
    print("\n분석 중...\n")
    result = classifier.analyzer.analyze_text(text)
    
    # 상세 보고서 출력
    report = classifier.analyzer.generate_report(result)
    print(report)


def main():
    """메인 함수"""
    while True:
        print_menu()
        choice = input().strip()
        
        if choice == '1':
            analyze_csv()
        elif choice == '2':
            analyze_single_text()
        elif choice == '3':
            print("\n프로그램을 종료합니다. 감사합니다!")
            break
        else:
            print("유효하지 않은 선택입니다. 다시 선택해주세요.\n")
        
        input("\n계속하려면 Enter를 누르세요...")
        print("\n" * 2)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n프로그램이 중단되었습니다.")
    except Exception as e:
        print(f"\n오류가 발생했습니다: {e}")
