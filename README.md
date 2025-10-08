# Object Detection with YOLOv11: Peanut Recognition
* 영상 속 제 강아지인 **땅콩이(Peanut)** 의 위치를 탐지하고 그 위치를 기반으로 땅콩이의 개별 이미지를 추출하는 것을 목표로 합니다. 
* **Roboflow**를 사용하여 라벨링한 **812**개의 이미지 데이터를 **Yolov11** 모델로 학습시켰으며, 훈련된 모델은 새로운 이미지와 동영상에서 땅콩이를 정확하게 인식합니다.
___
## 🎥 Prediction Result
<p align="center">
  <img src="https://github.com/xo0ol/Object-Detection-Yolov11---Peanut/blob/44aa5602a6e0e0d29aa253dc9fe0fe4104ee0607/images/output_gif.gif" width="450" />
  <img src="https://github.com/xo0ol/Object-Detection-Yolov11---Peanut/blob/29c0a974b3487d8d5525744d5ec56bf71a268c7b/images/video2.gif" width="450" />
  <img src="https://github.com/xo0ol/Object-Detection-Yolov11---Peanut/blob/ea377651e7a16d0a23dd2ba72cbdc9cb8066ad4e/images/peanut_test_video_output_images.png" width="450" />
  <img src="https://github.com/xo0ol/Object-Detection-Yolov11---Peanut/blob/29c0a974b3487d8d5525744d5ec56bf71a268c7b/images/video2.png" width="450" />
</p>


___

## 📝 Overview

### 1. **모델 학습용 데이터 준비: <RoboFlow 데이터 라벨링>**
  - **데이터 획득 및 증강**
    - 모델 훈련에 필요한 충분한 양의 땅콩이 이미지를 확보하기 위해, 직접 촬영한 동영상에서 OpenCV(cv2) 라이브러리를 활용하여 프레임 단위로 이미지를 추출했습니다.
    이 과정을 통해 다양한 각도와 배경을 가진 812개의 이미지를 확보합니다.

      >**모델 학습을 위한 데이터 증강 과정에서 활용된 동영상 프레임 추출 코드는 [<video_to_frames.py>](https://github.com/xo0ol/Object-Detection-Yolov11---Peanut/blob/main/src/video_to_frames.py)를 사용했습니다.**
    
  - **라벨링**
    - [Roboflow](https://roboflow.com/)를 사용하여 추출된 이미지와 추가 수집된 이미지를 포함한 총 812개의 땅콩이 이미지 데이터를 직접 라벨링하여 준비했습니다.
<p align="center">
  <img src="https://github.com/xo0ol/Train_YOLO_Peanut/blob/e7c292095a768c6384387aab9192d0becc7fe80d/images/robo_1.png" width="800" />
  <img src="https://github.com/xo0ol/Train_YOLO_Peanut/blob/e7c292095a768c6384387aab9192d0becc7fe80d/images/robo_3.png" width="800" />
  <img src="https://github.com/xo0ol/Train_YOLO_Peanut/blob/e7c292095a768c6384387aab9192d0becc7fe80d/images/robo_2.png" width="800" />
</p>

### 2. **Train Test 데이터 분할 및 data.yaml 파일 생성 : 오픈소스 사용**
  - 학습용 데이터를 Train-Test로 분할하기 위한 작업과, Yolov11 모델 학습에 필요한 data.yaml 파일을 생성하기 위해서 **EdjeElectronics의 GitHub 저장소**에 공유된 소스코드를 사용했습니다.
  - 참고 자료는 아래 **[<📚 References>](#-references)** 에서 확인하실 수 있습니다. 
    
### 3. **YOLOv11 모델 훈련**
  - 준비된 데이터셋을 바탕으로 YOLOv11의 경량 버전인 Yolo11s 훈련을 시작합니다.
  - 훈련 환경: Google Colab
    
    ```python
    !pip install ultralytics
    !yolo detect train data=/content/data.yaml model=yolo11s.pt epochs=50 imgsz=640 batch=8 
    ```
    
### 4. **훈련 결과**
  - 모델 훈련 후 반환된 results.png 파일을 통해 손실(loss) 감소 추이와 정밀도(precision) 및 재현율(recall)을 확인할 수 있습니다.
  - 모델은 훈련 초반부터 train loss와 validation loss를 빠르게 감소시켰으며, 약 40 에포크 시점에서 손실이 최저치에 근접했습니다.
  - 동시에 모델의 정밀도와 재현율은 40 에포크 이전에 이미 1.0에 도달했습니다. 결과적으로 모델은 주어진 데이터셋에서 단일 클래스의 특징을 효과적으로 학습했습니다.
  - 아래 이미지는 모델 훈련 후 반환된 **result.png**와 **val_batch_pred.jpg** 입니다.
<p align="center">
  <img src="https://github.com/xo0ol/Train_YOLO_Peanut/blob/b980a71acd2207d4632fcdd3178b4d71133f0b7b/images/results.png" width="800" />
  <img src="https://github.com/xo0ol/Train_YOLO_Peanut/blob/b980a71acd2207d4632fcdd3178b4d71133f0b7b/images/val_batch2_pred.jpg" width="500" />
</p>

### 5. **새 데이터 예측 및 검증**
  - 모델의 일반화 성능을 확인하기 위해 훈련에 사용하지 않은 새로운 이미지를 예측했습니다.
  - 모델은 사진 속 땅콩이 객체를 0.71의 신뢰도로 탐지하며, 훈련 데이터 외의 환경에서도 좋은 성능을 보였습니다.
    <img src="https://github.com/xo0ol/Object-Detection-Yolov11---Peanut/blob/ea377651e7a16d0a23dd2ba72cbdc9cb8066ad4e/images/prediction.png" width="300">


### **END. 땅콩이 이미지 추출**
  - 훈련된 모델을 활용하여 동영상에서 땅콩이 객체를 탐지하고, 각 프레임에서 탐지된 객체를 바운딩 박스에 맞춰 추출하여 새 비디오를 작성합니다.
    > [<extract_objects_from_video.py>](https://github.com/xo0ol/Object-Detection-Yolov11---Peanut/blob/main/src/extract_objects_from_video.py) 스크립트 실행
    ```python
    # !python create_annotated_video.py <model_path> <video_path> <output_path>
    !python create_annotated_video.py {model_path} {video_path} {output_path}
    ```
    <p align="center">
      <img src="https://github.com/xo0ol/Object-Detection-Yolov11---Peanut/blob/44aa5602a6e0e0d29aa253dc9fe0fe4104ee0607/images/output_gif.gif" width="600" />
    </p>

  - 바운딩 박스에 맞춰 프레임별 개별 이미지를 추출합니다.
    >[<extract_objects_from_video.py>](https://github.com/xo0ol/Object-Detection-Yolov11---Peanut/blob/main/src/extract_objects_from_video.py) 스크립트 실행
      ```python
      # !python extract_objects_from_video.py <model path> <video path> <output_dir> <confidence_threshold>
      !python extract_objects_from_video.py /content/yolov11_peanut_e50_b8.pt /content/peanut_test_video.mp4 /content/peanut_test_video_output 0.5
      ```
      <p align="center">
        <img src="https://github.com/xo0ol/Object-Detection-Yolov11---Peanut/blob/ea377651e7a16d0a23dd2ba72cbdc9cb8066ad4e/images/peanut_test_video_output_images.png" width="600" />
      </p>
___
## 📚 References
이 프로젝트는 아래의 오픈소스 프로젝트와 튜토리얼을 기반으로 제작되었습니다.

* **원본 GitHub 저장소**
  [![GitHub](https://img.shields.io/badge/GitHub-EdjeElectronics-blue)](https://github.com/EdjeElectronics/Train-and-Deploy-YOLO-Models)
* **Google Colab Notebook**
  [![Colab](https://img.shields.io/badge/Colab-EdjeElectronics-orange)](https://colab.research.google.com/github/EdjeElectronics/Train-and-Deploy-YOLO-Models/blob/main/Train_YOLO_Models.ipynb)
* **관련 YouTube 튜토리얼**
  프로젝트 전반적인 과정을 이해하기 위해 [Edje Electronics의 YouTube 튜토리얼](https://www.youtube.com/watch?v=r0RspiLG260)영상을 참고했습니다.
  [![How to Train YOLO Object Detection Models in Google Colab (YOLO11, YOLOv8, YOLOv5)](https://img.youtube.com/vi/r0RspiLG260/maxresdefault.jpg)](https://www.youtube.com/watch?v=r0RspiLG260)

    
