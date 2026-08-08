# 04. Customer Churn - Exploratory Data Analysis (EDA)

본 프로젝트는 고객 이탈(Customer Churn) 데이터를 탐색적으로 분석하여 이탈에 영향을 미치는 주요 요인을 파악하는 프로젝트입니다.

## 1. 개요
- **데이터셋**: 가상 고객 이탈 데이터셋 (500개 샘플)
- **주요 변수**: `Tenure`(가입 기간), `MonthlyCharges`(월 요금), `Contract`(계약 형태), `Churn`(이탈 여부)
- **실행 파일**: `customer_churn_eda.ipynb`

## 2. 주요 EDA 및 시각화
- **계약 형태별 이탈 수 (`sns.countplot`)**: Month-to-month 계약 고객에서 이탈자 수가 가장 높게 나타남
- **월 요금 분포 (`sns.boxplot`)**: 이탈 여부별 월 요금 수준 및 분포 비교
- **계약 형태별 평균 이탈률**:
  - `Month-to-month`: ~27.2%
  - `One year`: ~25.8%
  - `Two year`: ~31.3%
