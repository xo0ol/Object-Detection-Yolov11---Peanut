import os
import random
import matplotlib.pyplot as plt
import cv2

def display_images_from_folder(
    folder_path: str,
    num_images: int = 8,
    rows: int = 4,
    cols: int = 2,
    figsize: tuple = (10, 20)
):
    """
    지정된 폴더에서 이미지를 무작위로 선택하여 그래프로 시각화합니다.

    Args:
        folder_path (str): 이미지가 있는 폴더 경로.
        num_images (int, optional): 시각화할 이미지의 총 개수. 기본값은 8.
        rows (int, optional): 그래프의 행 수. 기본값은 4.
        cols (int, optional): 그래프의 열 수. 기본값은 2.
        figsize (tuple, optional): 그래프의 크기 (가로, 세로). 기본값은 (10, 20).
    """
    if not os.path.exists(folder_path):
        print(f"Error: 폴더를 찾을 수 없습니다. 경로를 다시 확인해주세요: {folder_path}")
        return

    # 폴더 내 모든 파일 목록 가져오기
    all_files = os.listdir(folder_path)
    
    # 이미지 파일만 필터링 (간단한 확장자 체크)
    image_files = [
        f for f in all_files 
        if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))
    ]

    if not image_files:
        print("Error: 폴더에 이미지가 없습니다.")
        return

    # 시각화할 이미지 무작위 선택
    selected_images = random.sample(image_files, min(num_images, len(image_files)))

    # 그래프 생성 및 이미지 표시
    fig, axes = plt.subplots(rows, cols, figsize=figsize)
    axes = axes.flatten()

    for i, image_name in enumerate(selected_images):
        image_path = os.path.join(folder_path, image_name)
        img = cv2.imread(image_path)
        
        if img is None:
            print(f"Warning: 이미지를 읽을 수 없습니다: {image_name}")
            continue

        # OpenCV는 BGR 순서로 읽으므로, Matplotlib을 위해 RGB로 변환
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        
        ax = axes[i]
        ax.imshow(img)
        ax.set_title(image_name, fontsize=8)
        ax.axis('off')  # 축 정보 숨기기

    # 남은 빈 서브플롯 숨기기
    for i in range(len(selected_images), len(axes)):
        axes[i].axis('off')

    plt.tight_layout()
    plt.show()

# --- 함수 사용 예시 (Colab 환경 기준) ---
if __name__ == '__main__':

    import sys
    
    # 명령행 인수 확인
    if len(sys.argv) < 5:
        print("사용법:")
        print("  python display_images_from_folder.py <folder_path : str> <num_images : int> <rows : int> <cols : int> <figsize: tuple>")
        print("")
        print("매개변수:")
        print("  folder_path      : 이미지가 포함된 폴더 경로")
        print("  num_images    : 그래프에 띄우기를 원하는 이미지의 개수")
        print("  rows      : 그래프의 행 지정")
        print("  cols  : 그래프의 열 지정")
        print("  figsize  : 그래프 크기 설정(tuple)")

        sys.exit(1)
    
    # 명령행 인수 추출
    folder_path = sys.argv[1]
    num_images = sys.argv[2]
    rows = sys.argv[3]
    cols = sys.argv[4]
    figsize = sys.argv[4]
    
    # 입력 파일 존재 확인
    if not os.path.exists(folder_path):
        print(f"오류: 폴더를 찾을 수 없습니다.: {folder_path}")
        sys.exit(1)
    
    # 객체 추출 실행
    print(f"이미지 폴더: {folder_path}")
    print(f"이미지 개수: {num_images}")
    print(f"그래프: {rows}*{cols}")
    print(f"그래프 사이즈: {figsize}")
    print("-" * 50)
    
    display_images_from_folder(folder_path, num_images, rows, cols, figsize)
