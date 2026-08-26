# 01. Fundamentals - Data Preprocessing Basics

본 프로젝트는 Pandas와 NumPy를 활용한 데이터 전처리 및 조건부 판정 로직 구현 실습입니다.

## 1. 개요
- 주제: 학생 성적 데이터 전처리 및 합격/불합격 판정
- 실행 파일: data_preprocessing_basics.ipynb

## 2. 주요 전처리 과정
- 결측치(NaN) 처리: 수학(Math) 및 영어(English) 과목의 결측치를 각 과목 평균값으로 임퓨테이션
- 파생 변수 생성: Total_Score(총점) 및 Average(평균) 파생 변수 산출
- 조건부 평가: 평균 점수 85점 이상 및 출석률 80퍼센트 이상 조건 충족 시 Pass, 미달 시 Fail 부여

## 3. 요약 결과
| Status | Average Score |
| :--- | :--- |
| Fail | 84.38 |
| Pass | 88.54 |