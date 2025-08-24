# Object Detection with YOLOv8: Peanut Recognition Project 🥜
이 프로젝트는 YOLOv8 모델을 사용하여 저의 강아지인 땅콩(Peanut) 객체를 탐지하는 것을 목표로 합니다. 
YOLOv8 모델을 학습하고, 훈련된 모델로 새로운 이미지와 동영상에서 땅콩을 인식하는 과정을 담고 있습니다.

**>>노트북 바로가기 [Click!](https://colab.research.google.com/github/xo0ol/Train_YOLO_Peanut/blob/main/Object_Detection_Yolov8_Peanut.ipynb)**

## 🎥 Prediction Result Video
이 프로젝트에서 훈련된 모델로 땅콩을 탐지한 결과 영상입니다.

## Project Details
For details of this project please check 

## Overview
이 프로젝트는 YOLO 모델 학습 및 배포 과정을 전체적으로 이해하기 위해 진행되었습니다. 
다음의 주요 단계를 포함합니다.
|Task|Details|
|---|---|
학습용 데이터 준비|Roboflow를 사용해 라벨링된 총 812개의 땅콩 이미지 데이터를 준비했습니다.
데이터셋 분할|학습 및 검증을 위해 데이터를 90%와 10%로 나눴습니다.(이 스크립트는 EdjeElectronics의 GitHub 저장소에서 가져왔습니다.)
data.yaml 생성|YOLOv8 모델 학습을 위해 데이터 경로와 클래스 정보를 담은 data.yaml 파일을 생성했습니다.(이 파일 생성에 사용된 create_data_yaml() 함수 역시 EdjeElectronics의 GitHub 저장소에서 가져왔습니다.)
YOLOv8 모델 훈련|준비된 데이터셋을 바탕으로 YOLOv8 모델을 훈련했습니다.
결과 확인|훈련된 모델의 성능을 평가하고, 새로운 데이터에 대한 예측을 수행했습니다.
동영상 객체 탐지|훈련된 모델을 사용해 peanut_test_video.mp4 영상에서 땅콩을 탐지하고, 결과 동영상을 생성했습니다.


## 📚 References
이 프로젝트는 아래의 오픈 소스 프로젝트와 튜토리얼을 기반으로 제작되었습니다.

* **원본 GitHub 저장소**
  - [![GitHub](https://img.shields.io/badge/GitHub-EdjeElectronics-blue)](https://github.com/EdjeElectronics/Train-and-Deploy-YOLO-Models)
* **Google Colab Notebook**
  - [![Colab](https://img.shields.io/badge/Colab-EdjeElectronics-orange)](https://colab.research.google.com/github/EdjeElectronics/Train-and-Deploy-YOLO-Models/blob/main/Train_YOLO_Models.ipynb)
* **관련 YouTube 튜토리얼**
  - 프로젝트 전반적인 과정을 이해하기 위해 [Edje Electronics의 YouTube 튜토리얼](https://www.youtube.com/watch?v=r0RspiLG260)영상을 참고했습니다.
    [![How to Train YOLO Object Detection Models in Google Colab (YOLO11, YOLOv8, YOLOv5)](https://img.youtube.com/vi/r0RspiLG260/maxresdefault.jpg)](https://www.youtube.com/watch?v=r0RspiLG260)
