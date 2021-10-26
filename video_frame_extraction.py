import os
import cv2
import numpy as np
import sys
from tqdm import tqdm

# 영상을 추출하는 프로그램
# -- 사용법
#1) 1. 파일경로 및 이름설정을 맞게 수정
#2) 2. 목표시간을 지정함. 분과 초를 변경 # 5:53 > 5*minute + 53
#3) cmd 창에서 py 실행

### 1. 파일경로 및 이름설정
video_path = 'C:/Users/KMS/Documents/Coding/video/video_extraction/'
# video1 = video_path + 'record_2021_08_02_15_07_05_373.mp4'
video1 = 'C:/Users/KMS/Downloads/현대0813영상/현대0813영상/로보영상1_4/lvds_cam_1/lvds_cam_1.yuv'

# height = 1280
# width = 944
# yuv_type = 'UYVY'

### 2. 목표 시간 지정
# 분 * 60 + 초 = 초 단위 시간
minute = 60
start = 5 * minute + 53
start = 0
last = 6 * minute + 14
last = 0
cap1 = cv2.VideoCapture(video1)

if not cap1.isOpened():
    print("Not open video!")
    sys.exit()
else:
    print("Video open")
    
#각 영상 프레임 수
frame_cnt1 = round(cap1.get(cv2.CAP_PROP_FRAME_COUNT))
fps = cap1.get(cv2.CAP_PROP_FPS)
delay = int(1000/fps)
print(frame_cnt1, type(frame_cnt1))
print("fps, delay = ", fps, delay)
print("frame1, fps = ",frame_cnt1, fps)

#영상 가로 세로 설정
w1 = round(cap1.get(cv2.CAP_PROP_FRAME_WIDTH))
h1 = round(cap1.get(cv2.CAP_PROP_FRAME_HEIGHT))
print("w1, h1 = ", w1,h1)

#비디오 코덱 설정
fourcc = cv2.VideoWriter_fourcc(*'DIVX')

print("save frame : ", fps * start," ~ ", fps*last)
print("save time(sec) : ", start," ~ ", last)
print()
#1번 영상 열기
for i in tqdm(range(frame_cnt1)):
    ret1, frame1 = cap1.read()
    if not ret1 :
        break
    
    if i < fps * start :
        pass
    
    #시작 프레임이 되면 첫화면 저장 및 동영상 녹화 시작
    if i == fps * start :
        #print(len(framex), len(framex[0]), type(frame1))
        cv2.imwrite(video_path + 'frame1.jpg', frame1)
        out = cv2.VideoWriter(video_path+ 'output1.avi', fourcc, fps, (w1,h1))
        pass
    #시작프레임 이후는 녹화
    if i > fps*start :
        out.write(frame1)

    if last != 0 :
        #마지막 프레임이지나면 자동종료        
        if i > fps * last :
            out.release()
            break
    else :
        pass
    # cv2.imshow('frame', frame1)
    # cv2.waitKey(delay)
#마지막 프레임이 없다면 영상 끝나고 종료.
out.release()

    