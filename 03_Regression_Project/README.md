# 03. Regression Project - California Housing Price Prediction

본 프로젝트는 캘리포니아 주택 데이터를 활용하여 주택 가격을 예측하는 회귀(Regression) 모델 프로젝트입니다. 기본 모델 학습 이후, Pipeline과 GridSearchCV, K-Fold 교차검증을 적용해 하이퍼파라미터 튜닝 효과를 검증했습니다.

## 1. 개요

데이터셋: California Housing Dataset (1,000개 샘플 추출)
타겟 변수: MedHouseVal (중위 주택 가격)
적용 모델: Random Forest Regressor
실행 파일: housing_regression.ipynb

## 2. 기본 모델 성능

R2 Score: 0.6885 (설명력 68.85%)
Mean Squared Error (MSE): 0.4737

## 3. Pipeline 및 하이퍼파라미터 튜닝

방법: StandardScaler와 RandomForestRegressor를 Pipeline으로 묶어 Data Leakage 방지, KFold(5-Fold) 교차검증, GridSearchCV로 n_estimators와 max_depth 탐색

튜닝 후 R2: 0.6910, MSE: 0.4700
최적 파라미터: max_depth=None, n_estimators=200
K-Fold(5-Fold) 교차검증 평균 R2: 0.7100

## 4. 시각화 분석

실제 가격(Actual Prices)과 예측 가격(Predicted Prices)의 연관성을 산점도(Scatter Plot)로 시각화
대각선 기준선(y=x)을 추가하여 예측 오차 분포 확인