import os
import cv2

def extract_objects_from_video(model, video_path, output_dir, confidence_threshold=0.5):
    """
    비디오에서 객체를 탐지하고 각 프레임마다 객체를 잘라서 저장하는 함수
    
    Args:
        model: YOLO 모델
        video_path (str): 입력 비디오 파일 경로
        output_dir (str): 출력 폴더 경로
        confidence_threshold (float): 신뢰도 임계값 (기본값: 0.5)
    """
    # 출력 폴더 생성
    os.makedirs(output_dir, exist_ok=True)
    
    # 비디오 캡처 객체 생성
    cap = cv2.VideoCapture(video_path)
    
    if not cap.isOpened():
        print(f"비디오 파일을 열 수 없습니다: {video_path}")
        return
    
    frame_count = 0
    object_count = 0
    
    print("객체 추출 시작...")
    
    while True:
        # 프레임 읽기
        ret, frame = cap.read()
        
        if not ret:
            break
        
        frame_count += 1
        
        # YOLO 모델로 객체 탐지
        results = model(frame, conf=confidence_threshold)
        
        # 각 탐지 결과에 대해 처리
        for result in results:
            boxes = result.boxes
            
            if boxes is not None:
                for i, box in enumerate(boxes):
                    # 바운딩 박스 좌표 추출
                    x1, y1, x2, y2 = box.xyxy[0].cpu().numpy()
                    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                    
                    # 신뢰도 점수
                    confidence = float(box.conf[0])
                    
                    # 객체 영역 잘라내기
                    cropped_object = frame[y1:y2, x1:x2]
                    
                    # 잘라낸 객체가 유효한지 확인
                    if cropped_object.size > 0:
                        object_count += 1
                        
                        # 파일명 생성 (프레임번호_객체번호.jpg)
                        filename = f"frame_{frame_count:04d}_object_{object_count:04d}.jpg"
                        output_path = os.path.join(output_dir, filename)
                        
                        # 이미지 저장
                        cv2.imwrite(output_path, cropped_object)
                        
                        print(f"저장됨: {filename} (신뢰도: {confidence:.3f})")
        
        # 진행상황 표시 (10프레임마다)
        if frame_count % 10 == 0:
            print(f"처리된 프레임: {frame_count}")
    
    # 비디오 캡처 해제
    cap.release()
    
    print(f"\n처리 완료!")
    print(f"총 프레임 수: {frame_count}")
    print(f"추출된 객체 수: {object_count}")
    print(f"저장 위치: {output_dir}")

def load_yolo_model(model_path):
    """
    YOLO 모델을 로드하는 함수
    
    Args:
        model_path (str): 모델 파일 경로
        
    Returns:
        YOLO: 로드된 YOLO 모델
    """
    try:
        from ultralytics import YOLO
        model = YOLO(model_path)
        print(f"모델 로드 완료: {model_path}")
        return model
    except ImportError:
        print("오류: ultralytics 라이브러리가 설치되지 않았습니다.")
        print("설치 명령어: pip install ultralytics")
        return None
    except Exception as e:
        print(f"모델 로드 실패: {e}")
        return None

if __name__ == "__main__":
    import sys
    
    # 명령행 인수 확인
    if len(sys.argv) < 4:
        print("사용법:")
        print("  python extract_objects_from_video.py <모델_경로> <비디오_경로> <출력_폴더> [신뢰도_임계값]")
        print("")
        print("매개변수:")
        print("  모델_경로      : YOLO 모델 파일 경로 (.pt 파일)")
        print("  비디오_경로    : 입력 비디오 파일 경로")
        print("  출력_폴더      : 추출된 객체 이미지 저장 폴더")
        print("  신뢰도_임계값  : 객체 탐지 신뢰도 임계값 (기본값: 0.5)")
        print("")
        print("예시:")
        print("  python extract_objects_from_video.py model.pt video.mp4 output/")
        print("  python extract_objects_from_video.py model.pt video.mp4 output/ 0.7")
        sys.exit(1)
    
    # 명령행 인수 추출
    model_path = sys.argv[1]
    video_path = sys.argv[2]
    output_dir = sys.argv[3]
    confidence_threshold = float(sys.argv[4]) if len(sys.argv) > 4 else 0.5
    
    # 입력 파일 존재 확인
    if not os.path.exists(model_path):
        print(f"오류: 모델 파일을 찾을 수 없습니다: {model_path}")
        sys.exit(1)
    
    if not os.path.exists(video_path):
        print(f"오류: 비디오 파일을 찾을 수 없습니다: {video_path}")
        sys.exit(1)
    
    # 모델 로드
    model = load_yolo_model(model_path)
    if model is None:
        print("오류: 모델 로드에 실패했습니다.")
        sys.exit(1)
    
    # 객체 추출 실행
    print(f"모델: {model_path}")
    print(f"비디오: {video_path}")
    print(f"출력 폴더: {output_dir}")
    print(f"신뢰도 임계값: {confidence_threshold}")
    print("-" * 50)
    
    extract_objects_from_video(model, video_path, output_dir, confidence_threshold)
    
    print("-" * 50)
    print("객체 추출 작업이 완료되었습니다.")