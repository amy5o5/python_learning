import cv2
import os
your_video = "/video.mp4"
cap = cv2.VideoCapture(your_video)
frames = []

while True:
    ret, frame = cap.read()
    if not ret:
        break
    frames.append(frame)

cap.release()
print(f"Total frames extracted: {len(frames)}")
print(os.getcwd())