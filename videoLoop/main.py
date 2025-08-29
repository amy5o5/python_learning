import cv2
import numpy as np

cap = cv2.VideoCapture("/home/amy/Videos/video.mp4")
fps = cap.get(cv2.CAP_PROP_FPS)
frame_count = 0

def average_two_frame(f1, f2):
    return cv2.addWeighted(f1, 0.5, f2, 0.5, 0)

def frames_diff(f1, f2):
    return cv2.absdiff(f1, f2)

frames = []

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frames.append(gray)
    frame_count += 1

    if len(frames) == 4:
        avg1 = average_two_frame(frames[0], frames[1])
        avg2 = average_two_frame(frames[2], frames[3])

        diff = frames_diff(avg1, avg2)
        mean_diff = np.mean(diff)

        # زمان تقریبی فریم وسط این 4 فریم
        second = (frame_count - 2) / fps
        print(f"time {second:.2f} diff: {mean_diff:.2f}")

        frames = []  # reset

cap.release()
