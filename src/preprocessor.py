"""텍스트 전처리 모듈"""

import re
import unicodedata


class TextPreprocessor:
    """텍스트 전처리 클래스"""
    
    @staticmethod
    def normalize_text(text):
        """유니코드 정규화"""
        if not text:
            return ""
        return unicodedata.normalize('NFKC', text)
    
    @staticmethod
    def remove_special_characters(text):
        """특수문자 제거"""
        # 알파벳, 숫자, 한글, 공백, 기본 구두점만 유지
        text = re.sub(r'[^a-zA-Z0-9가-힣\s,.!?;:\-()\"\'']', ' ', text)
        return text
    
    @staticmethod
    def remove_extra_spaces(text):
        """연속된 공백 제거"""
        text = re.sub(r'\s+', ' ', text)
        return text.strip()
    
    @staticmethod
    def convert_to_lowercase(text):
        """소문자 변환 (영어만)"""
        return text.lower()
    
    @staticmethod
    def tokenize_sentences(text):
        """문장 토크나이제이션"""
        # 마침표, 느낌표, 물음표로 분할
        sentences = re.split(r'[.!?]', text)
        return [s.strip() for s in sentences if s.strip()]
    
    @staticmethod
    def tokenize_words(text):
        """단어 토크나이제이션"""
        # 공백으로 분할
        words = text.split()
        return [w.strip(',.!?;:()\"\'') for w in words if w.strip()]
    
    @classmethod
    def preprocess(cls, text):
        """전체 전처리 파이프라인"""
        if not text:
            return ""
        
        # 1. 유니코드 정규화
        text = cls.normalize_text(text)
        
        # 2. 특수문자 제거
        text = cls.remove_special_characters(text)
        
        # 3. 연속 공백 제거
        text = cls.remove_extra_spaces(text)
        
        # 4. 소문자 변환 (영어만)
        text = cls.convert_to_lowercase(text)
        
        return text
