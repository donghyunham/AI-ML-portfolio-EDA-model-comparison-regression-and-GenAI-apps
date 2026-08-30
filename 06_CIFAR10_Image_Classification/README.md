# 06_CIFAR10_Image_Classification

## 프로젝트 개요
CIFAR-10 데이터셋으로 이미지 분류 모델을 구축하고, Baseline CNN과 데이터 증강/구조 개선을 적용한 Improved CNN의 성능을 정량 비교한 프로젝트입니다.

---

## Tech Stack
- Framework: TensorFlow, Keras
- Data: CIFAR-10 (tf.keras.datasets.cifar10)
- Data Split: Scikit-learn train_test_split (stratify)
- Training Environment: Google Colab, T4 GPU
- Visualization: Matplotlib

---

## Architecture & Workflow
1. 데이터 준비
   - tf.keras.datasets.cifar10으로 Train 50000장, Test 10000장을 불러오고 정규화(0-1 스케일) 처리
   - Train에서 20퍼센트를 stratify 방식으로 분리해 Train 40000장, Validation 10000장, Test 10000장으로 구성
2. Baseline CNN
   - Conv2D(32), Conv2D(64) 두 블록에 Flatten, Dense(128), Dropout(0.5) 구조로 15 epoch 학습
3. Improved CNN
   - RandomFlip, RandomRotation, RandomZoom 데이터 증강과 BatchNormalization을 추가하고 Conv2D(128) 블록을 더해 30 epoch 학습

---

## 성능 비교, Baseline CNN vs Improved CNN
- Baseline, Test Accuracy 0.6989 (15 epoch)
- Improved, Test Accuracy 0.7438 (30 epoch), Baseline 대비 4.49퍼센트포인트 개선
- 두 모델 모두 Validation Accuracy와 Test Accuracy가 비슷한 범위에서 일치, 데이터 파이프라인 문제 없음을 확인함
- Improved 모델은 데이터 증강으로 초반 학습이 불안정했으나, 15 epoch 이후로 Baseline을 넘어서는 성능을 보임

---

## 실행 방법
06_CIFAR10_Image_Classification.ipynb 파일을 Google Colab에서 열어 GPU 런타임(T4 이상)으로 순서대로 실행합니다.

---

## 주요 성과 및 인사이트
- Train/Validation/Test를 사전에 정확히 분리하여 검증 정확도와 테스트 정확도 간 불일치 문제를 방지함
- 데이터 증강과 배치 정규화를 통한 개선 전후 성능을 정량적으로 비교함
- ModelCheckpoint(save_best_only=True)로 Validation Accuracy 기준 최적 시점의 가중치를 저장함