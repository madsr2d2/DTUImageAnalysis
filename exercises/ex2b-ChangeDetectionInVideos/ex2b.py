import cv2
import numpy as np
import time

# Open a video capture (0 for the default camera)
camPath = '/home/madsr2d2/VID_20240206_161421.mp4'
cap = cv2.VideoCapture(camPath, cv2.CAP_FFMPEG)

while True:
    start = time.time()
    # Read a frame from the video capture
    ret, frame = cap.read()
    if not ret:
        print('Error reading frame')
        break

    grayImg = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Convert the image to float
    grayImgAsFloat = grayImg.astype(np.float32)

    # conert image to uint8
    grayImgUint8 = grayImgAsFloat.astype(np.uint8)

    stop = time.time()

    fps = 1/(stop-start)
    cv2.putText(grayImgUint8, f'FPS: {fps:.2f}', (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

    # Display the frame
    cv2.imshow('Frame', grayImgUint8)

    # Wait for 1 millisecond for a key event
    if cv2.waitKey(1) & 0xFF == ord('q'):
        # Break the loop if 'q' is pressed
        break

# Release the video capture and close all windows
cap.release()
cv2.destroyAllWindows()
