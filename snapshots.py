import cv2
import time
import datetime

cam = cv2.VideoCapture(0)

#cv2.namedWindow("test")

img_counter = 0

while True:
    if(img_counter > 10000):       #making sure image numbers don't get out of control
        img_counter = 0
    
    ret, frame = cam.read()
    #cv2.imshow("test", frame)  #shows preview of image to be taken
    if not ret:
        break
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    cv2.resize(frame, (480, 360))      #decreasing resolution
    img_name = '/tmp/opencv_frame/' + st + '.jpg'.format(img_counter)
    cv2.imwrite(img_name, frame)
    #print("{} written!".format(img_name))
    img_counter += 1

    time.sleep(.2)

cam.release()

cv2.destroyAllWindows()
