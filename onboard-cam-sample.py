import cv2
print(cv2.__version__)

cap = cv2.VideoCapture('nvcamerasrc ! video/x-raw(memory:NVMM), width=(int)640, height=(int)480,format=(string)I420, framerate=(fraction)30/1 ! nvvidconv ! video/x-raw, format=(string)BGRx ! videoconvert ! video/x-raw, format=(string)BGR ! appsink')

while(True):
  ret, frame = cap.read();
  cv2.imshow('MyFrame', frame)
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

# External cam
# https://devtalk.nvidia.com/default/topic/1027250/jetson-tx2/how-to-use-usb-webcam-in-jetson-tx2-with-python-and-opencv-/
