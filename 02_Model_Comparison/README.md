# 02. Model Comparison - Multi-Classifier Performance

본 프로젝트는 두 단계로 구성됩니다. 1단계는 Iris 데이터셋으로 3개 분류 알고리즘의 기본 성능을 비교했고, 2단계는 Breast Cancer 데이터셋에 Pipeline과 GridSearchCV, K-Fold 교차검증을 적용해 실제 하이퍼파라미터 튜닝 효과를 검증했습니다.

## 1. Iris 데이터셋 기본 비교

데이터셋: Iris Dataset (load_iris, 150개 샘플)
실행 파일: model_comparison.ipynb
평가 지표: Accuracy Score
모델별 정확도: Logistic Regression 1.00, Decision Tree Classifier 1.00, Random Forest Classifier 1.00

참고, Iris 데이터셋은 클래스 간 구분이 뚜렷해 대부분 모델이 만점에 가까운 정확도를 보입니다. 하이퍼파라미터 튜닝 효과를 확인하기 위해 2단계에서 더 복잡한 데이터셋을 사용했습니다.

## 2. Breast Cancer 데이터셋 Pipeline 및 하이퍼파라미터 튜닝

데이터셋: Breast Cancer Wisconsin Dataset (load_breast_cancer, 569개 샘플)
방법: StandardScaler와 분류기를 Pipeline으로 묶어 Data Leakage 방지, StratifiedKFold(5-Fold) 교차검증, GridSearchCV로 하이퍼파라미터 탐색

| Model | Before CV Accuracy | After CV Accuracy | Best Params | Test Accuracy | Test F1 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Logistic Regression | 0.9780 | 0.9824 | C=0.1 | 0.9737 | 0.9793 |
| Decision Tree | 0.9165 | 0.9319 | max_depth=2 | 0.8947 | 0.9118 |
| Random Forest | 0.9626 | 0.9626 | 다수 조합 중 변화 없음 | 0.9561 | 0.9655 |

## 3. 주요 발견

Decision Tree는 GridSearchCV로 max_depth를 2로 제한한 결과, K-Fold 교차검증 정확도가 0.9165에서 0.9319로 개선되어 과적합 억제 효과가 뚜렷하게 나타났습니다.
Random Forest는 튜닝 전후 정확도 변화가 없어, 기본 파라미터가 이미 안정적인 성능을 보이는 것으로 판단됩니다.