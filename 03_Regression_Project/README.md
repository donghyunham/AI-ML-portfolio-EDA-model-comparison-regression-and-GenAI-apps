# 03. Regression Project - California Housing Price Prediction

본 프로젝트는 캘리포니아 주택 데이터를 활용하여 주택 가격을 예측하는 회귀(Regression) 모델 구축 프로젝트입니다.

## 사용 데이터셋 및 모델
- **데이터셋**: California Housing Dataset (`fetch_california_housing`, Sample size: 1,000)
- **타겟 변수**: `MedHouseVal` (중위 주택 가격)
- **적용 모델**: Random Forest Regressor

## 모델 평가 및 시각화
- **평가 지표**:
  - $R^2$ Score: `0.6885`
  - Mean Squared Error (MSE): `0.4737`
- **시각화**: 실제값(Actual Prices) vs 예측값(Predicted Prices) 산점도(Scatter Plot) 및 대각선 기준선 표시

## 실행 파일
- `housing_regression.ipynb`
