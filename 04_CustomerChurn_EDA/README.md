# 04. Customer Churn - Exploratory Data Analysis (EDA)

본 프로젝트는 고객 이탈(Customer Churn) 데이터를 탐색적으로 분석(EDA)하여 주요 이탈 패턴과 특성을 파악하는 프로젝트입니다.

## 분석 데이터 및 주요 변수
- **데이터**: 가상 고객 데이터셋 (500개 샘플)
- **주요 변수**: `Tenure` (가입 기간), `MonthlyCharges` (월 요금), `Contract` (계약 형태), `Churn` (이탈 여부)

## 주요 분석 및 시각화
- **계약 형태별 이탈 분포**: `sns.countplot`을 활용해 계약 기간(Month-to-month, One year, Two year)에 따른 이탈/유지 고객 수 분석
- **월 요금과 이탈 연관성**: `sns.boxplot`을 활용해 이탈 여부별 월 요금 분포 비교
- **계약 유형별 이탈률 집계**: `groupby()` 기반 비율 계산

## 실행 파일
- `customer_churn_eda.ipynb`
