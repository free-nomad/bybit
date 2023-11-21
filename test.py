from pybit.unified_trading import WebSocket
from time import sleep

# 파일을 읽기 모드로 열기
with open("C:\\Users\\lee\\Desktop\\bybit\\api.txt", "r") as file:
    f = []
    # 파일의 각 줄에 대해 반복
    for line in file:
        # 각 줄 출력
        f.append(line.strip())  # strip()은 줄 바꿈 문자(\n) 등을 제거하여 출력합니다.