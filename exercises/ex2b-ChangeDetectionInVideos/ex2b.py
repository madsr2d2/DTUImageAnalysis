import cv2

# Open a video capture (0 for the default camera)
camPath = '/home/madsr2d2/VID_20240206_161421.mp4'
cap = cv2.VideoCapture(camPath, cv2.CAP_FFMPEG)

while True:
    # Read a frame from the video capture
    ret, frame = cap.read()
    if not ret:
        print('Error reading frame')
        break

    # Display the frame
    cv2.imshow('Frame', frame)

    # Wait for 1 millisecond for a key event
    if cv2.waitKey(1) & 0xFF == ord('q'):
        # Break the loop if 'q' is pressed
        break

# Release the video capture and close all windows
cap.release()
cv2.destroyAllWindows()
