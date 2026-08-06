# 01. Fundamentals – Exploratory Data Analysis (EDA)

이 섹션은 데이터 분석의 기초 역량을 다지기 위한 프로젝트 모음입니다.
데이터 구조 이해, 기초 통계 분석, 시각화를 통해 데이터에서 인사이트를 도출하는 것을 목표로 합니다.

## 주요 학습 내용
- 데이터 구조 및 변수 이해
- 기초 통계량 분석
- 분포 및 변수 간 관계 시각화
- 간단한 인사이트 도출

## 프로젝트 목록
- Track1_CustomerChurn_EDA: 고객 이탈 데이터에 대한 탐색적 데이터 분석(EDA)을 수행한 프로젝트

---

## Track 1: Customer Churn EDA

### 프로젝트 목적
- 고객 이탈(Churn)에 영향을 주는 주요 요인을 탐색적으로 분석
- 데이터 분포, 변수 간 관계, 이탈 패턴 이해

### 데이터 개요
- 고객 정보, 서비스 이용 정보, 계약 정보
- Target: Churn (0 = 유지, 1 = 이탈)

### 주요 분석 내용
- 수치형 변수 분포 분석 (Histogram)
- Churn 기준 평균 비교
- 범주형 변수(Gender, Subscription Type, Contract Length)별 이탈 비율
- 변수 간 상관관계 분석 (Heatmap)

### 주요 인사이트
- 이탈 고객은 Support Calls 및 Payment Delay가 전반적으로 높음
- 장기 계약(Annual) 고객일수록 이탈 비율이 낮고 Total Spend가 큼
- Churn은 단일 변수보다는 서비스 이용 패턴 + 계약 조건의 복합적 영향으로 발생

### 다음 단계
- EDA 결과를 바탕으로 Churn 예측 모델 구축