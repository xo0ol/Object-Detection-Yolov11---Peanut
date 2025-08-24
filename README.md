# Object Detection with YOLOv8: Peanut Recognition Project 🥜
이 프로젝트는 영상 속에서 저의 강아지인 **땅콩이(Peanut)** 객체의 위치를 찾고, 그 위치를 기반으로 땅콩이 개별 사진을 얻는 것을 목표로 합니다.
**roboflow**를 사용하여 라벨링한 812개의 이미지 데이터를 **YOLOv8** 모델로 학습합니다. 훈련된 모델은 새로운 이미지와 동영상에서 땅콩이를 인식하는 과정을 담고 있습니다.  

**>>노트북 바로가기 [Click!](https://colab.research.google.com/github/xo0ol/Train_YOLO_Peanut/blob/main/Object_Detection_Yolov8_Peanut.ipynb)**
___
## 🎥 Prediction Result
이 프로젝트에서 훈련된 모델로 땅콩을 탐지한 결과 영상입니다.
___
## Overview

* 모델 학습용 데이터 준비: <RoboFlow 데이터 라벨링>
  - Roboflow를 사용해 라벨링된 총 812개의 땅콩 이미지 데이터를 준비했습니다.
<p align="center">
  <img src="https://github.com/xo0ol/Train_YOLO_Peanut/blob/e7c292095a768c6384387aab9192d0becc7fe80d/images/robo_1.png" width="800" />
  <img src="https://github.com/xo0ol/Train_YOLO_Peanut/blob/e7c292095a768c6384387aab9192d0becc7fe80d/images/robo_2.png" width="800" />
  <img src="https://github.com/xo0ol/Train_YOLO_Peanut/blob/e7c292095a768c6384387aab9192d0becc7fe80d/images/robo_3.png" width="800" />
</p>

* Train Test 데이터 분할 : 오픈소스 사용
  - 학습용 데이터를 Train-Test로 분할하기 위한 작업과, Yolov8 모델 학습을 위한 data.yaml 파일 생성을 위한 소스코드는 EdjeElectronics의 GitHub 저장소에서 가져왔습니다.
  - 참고 자료는 아래 <📚 References>에서 확인하실 수 있습니다.
    
* YOLOv8 모델 훈련
  - 준비된 데이터셋을 바탕으로 YOLOv8 모델을 훈련했습니다. 훈련 정보는 다음과 같습니다.
    |Hyperparameter|Details|Details|
    |--|--|--|
    |Epoch|50|3번의 학습 결과, 가장 정확도가 높은 50을 사용
    |Batch Size|8|3번의 학습 결과, 가장 정확도가 높은 8을 사용
    |Image Size|640|내용을 추가해줘 예를 들어 'Yolo모델에 맞게 이미지 사이즈 640으로 고정' 이런 식으로|

* 새 데이터 예측하기
  - 본격적으로 영상에서 땅콩이 객체를 탐지하기 전, 모델 훈련에 사용하지 않았던 새 이미지를 예측하여 모델 성능을 점검합니다.
  - ㄴㅇ

* 훈련된 모델을 사용하여 영상에서 객체 탐지하기
  - ㄴㅇㄹ
<p align="center">
  <img src="https://github.com/xo0ol/Train_YOLO_Peanut/blob/b980a71acd2207d4632fcdd3178b4d71133f0b7b/images/results.png" width="800" />
  <img src="https://github.com/xo0ol/Train_YOLO_Peanut/blob/b980a71acd2207d4632fcdd3178b4d71133f0b7b/images/val_batch2_pred.jpg" width="800" />
</p>

* 동영상 객체 탐지
  - 훈련된 모델을 사용해 peanut_test_video.mp4 영상에서 땅콩을 탐지하고, 결과 동영상을 생성했습니다.
___
## 📚 References
이 프로젝트는 아래의 오픈 소스 프로젝트와 튜토리얼을 기반으로 제작되었습니다.

* **원본 GitHub 저장소**
  - [![GitHub](https://img.shields.io/badge/GitHub-EdjeElectronics-blue)](https://github.com/EdjeElectronics/Train-and-Deploy-YOLO-Models)
* **Google Colab Notebook**
  - [![Colab](https://img.shields.io/badge/Colab-EdjeElectronics-orange)](https://colab.research.google.com/github/EdjeElectronics/Train-and-Deploy-YOLO-Models/blob/main/Train_YOLO_Models.ipynb)
* **관련 YouTube 튜토리얼**
  - 프로젝트 전반적인 과정을 이해하기 위해 [Edje Electronics의 YouTube 튜토리얼](https://www.youtube.com/watch?v=r0RspiLG260)영상을 참고했습니다.
    [![How to Train YOLO Object Detection Models in Google Colab (YOLO11, YOLOv8, YOLOv5)](https://img.youtube.com/vi/r0RspiLG260/maxresdefault.jpg)](https://www.youtube.com/watch?v=r0RspiLG260)

    
