# 04. Customer Churn - Prediction & Exploratory Data Analysis (EDA)

본 프로젝트는 실제 통신사 고객 이탈(Customer Churn) 데이터셋을 활용하여 이탈에 영향을 미치는 요인을 분석하고, 이탈 여부를 예측하는 분류 모델을 구축한 프로젝트입니다.

## 1. 개요

데이터셋: Telecom Customer Churn Dataset (OpenML, 5,000개 샘플, 21개 변수)
주요 변수: account_length, international_plan, voice_mail_plan, total_day_minutes, total_day_calls 등 통화 및 요금 관련 변수
실행 파일: customer_churn_eda.ipynb

## 2. 데이터 정제

결측치 점검: 전체 21개 컬럼 결측치 0건 확인
상관관계 분석 및 다중공선성 제거: total_day_minutes와 total_day_charge 등 minutes-charge 계열 변수쌍에서 상관계수 1.0000 확인, 요금이 통화량에서 파생된 중복 변수임을 검증하고 charge 계열 컬럼 제거

## 3. 예측 모델

방법: StandardScaler와 LogisticRegression(class_weight=balanced)을 Pipeline으로 구성해 클래스 불균형(이탈 비율 약 14퍼센트) 대응

Precision: 0.3607
Recall: 0.7163
F1 Score: 0.4798

이탈 고객 141명 중 101명을 실제로 탐지(재현율 71.63퍼센트), 이탈 예측 비용보다 이탈 고객을 놓치는 비용이 큰 비즈니스 상황을 고려해 재현율 우선 전략 적용

## 4. 인사이트

Month-to-month 계약 고객의 이탈률(약 27.2퍼센트)이 One year(약 25.8퍼센트), Two year(약 31.3퍼센트) 대비 뚜렷하게 나타나는 경향 확인 (계약 형태별 재계산 필요, 초기 EDA 기준) 