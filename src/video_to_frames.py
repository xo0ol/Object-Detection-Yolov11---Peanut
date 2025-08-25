import cv2
import os

def video_to_frames(video_path, output_folder, save_interval=1):
    """
    동영상을 프레임 단위로 분할하여 이미지로 저장하는 함수
    
    Args:
        video_path (str): 동영상 파일 경로
        output_folder (str): 이미지 저장 폴더 경로
        save_interval (int): 몇 초마다 한 장씩 저장할지 설정 (기본값: 1초)
    """
    # 1. 입력 경로 검증
    if not os.path.exists(video_path):
        print(f"오류: 동영상 파일을 찾을 수 없습니다: {video_path}")
        return False
    
    # 2. 저장 폴더 생성
    try:
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
    except Exception as e:
        print(f"오류: 저장 폴더 생성 실패: {e}")
        return False
    
    # 3. 동영상 파일 열기
    cap = cv2.VideoCapture(video_path)
    
    if not cap.isOpened():
        print(f"오류: 동영상 파일을 열 수 없습니다: {video_path}")
        return False
    
    try:
        # 4. 동영상 정보 가져오기
        fps = cap.get(cv2.CAP_PROP_FPS)
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        frame_interval = int(fps * save_interval)  # 저장 간격에 따른 프레임 계산
        
        # 영상 길이 계산 (초 단위)
        video_duration = total_frames / fps
        
        print(f"동영상 정보:")
        print(f"  - FPS: {fps:.2f}")
        print(f"  - 총 프레임 수: {total_frames}")
        print(f"  - 영상 길이: {video_duration:.2f}초 ({video_duration/60:.2f}분)")
        print(f"  - 저장 간격: {save_interval}초마다 ({frame_interval}프레임마다)")
        
        saved_count = 0
        frame_count = 0
        
        # 5. 프레임 단위로 읽고 저장
        while True:
            ret, frame = cap.read()
            
            if not ret:
                break
            
            if frame_count % frame_interval == 0:
                image_filename = f"frame_{frame_count:05d}.jpg"
                output_path = os.path.join(output_folder, image_filename)
                
                # 이미지 저장
                if cv2.imwrite(output_path, frame):
                    saved_count += 1
                    
                    # 진행 상황 표시 (10개마다)
                    if saved_count % 10 == 0:
                        progress = (frame_count / total_frames) * 100
                        print(f"저장 중... {saved_count}개 완료 ({progress:.1f}%)")
                else:
                    print(f"경고: 프레임 {frame_count} 저장 실패")
            
            frame_count += 1
        
        # 6. 결과 출력
        print(f"\n완료! 총 {saved_count}개의 프레임이 {output_folder}에 저장되었습니다.")
        return True
        
    except Exception as e:
        print(f"오류 발생: {e}")
        return False
    
    finally:
        # 7. 자원 해제
        cap.release()


if __name__ == "__main__":
    import argparse
    import sys
    
    parser = argparse.ArgumentParser(description='비디오를 프레임으로 변환')
    parser.add_argument('video_path', help='입력 비디오 파일 경로')
    parser.add_argument('output_folder', help='출력 폴더 경로')
    parser.add_argument('--interval', '-i', type=int, default=1, 
                       help='저장 간격 (초, 기본값: 1)')
    parser.add_argument('--verbose', '-v', action='store_true', 
                       help='상세 출력')
    
    args = parser.parse_args()
    
    if args.verbose:
        print(f"입력 비디오: {args.video_path}")
        print(f"출력 폴더: {args.output_folder}")
        print(f"저장 간격: {args.interval}초")
    
    success = video_to_frames(args.video_path, args.output_folder, args.interval)
    
    if not success:
        print("변환에 실패했습니다.")
        sys.exit(1)
    else:
        print("변환 완료!")