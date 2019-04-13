import cv2
import time		#access system clock
import sys, getopt
import datetime		#gets date and time and proper format


def take_snapshots(cam_value, file_write_path):
	#choosing which camera to use
	#DEFAULT is external USB camera
	if(cam_value == 'True'):
		print("Thiiscam ",cam_value)
		cam = cv2.VideoCapture(1)
	else:
		print("Thiiscam ",cam_value)
		print("Invalid camera setting.")
		sys.exit()
	#setting default path if no input is given
		if(file_write_path == ''):
			file_write_path = '/tmp/opencv_frame/'
		

	img_counter = 0

	while True:
	    if(img_counter > 10000):       #making sure image numbers don't get out of control
				img_counter = 0
	    ret, frame = cam.read()		#taking image
	    if not ret:						#checking for error collecting image
				break
	    ts = time.time()
	    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
	    cv2.resize(frame, (480, 360))      #decreasing resolution
	    img_name = file_write_path + st + '.jpg'.format(img_counter)	#prepping name of image to be written
	    cv2.imwrite(img_name, frame)			#writing to input path, Note: default is /tmp/opencv_frame/
	    img_counter += 1

	    time.sleep(.2)
			#POSSIBLY SHOULD ADD POLLING KEYBOARD INTERRUPT
			#DOWNSIDE IS IT WILL SLOW DOWN PROGRAM
	cam.release()			#releases camera from use

	cv2.destroyAllWindows()				#releases cv2 resources


def main(argv):
  usb_cam = ''		#defaults
	file_path = ''
  helpMessage = """
<python >= 2.7> snapshots.py --usb_cam <usb_camera>
--usb_cam specifies camera to be used. usb+cam=true will use exterior camera and not the one mounted on Jetson TX2
  """
  
  try:
    opts, args = getopt.getopt(argv, "hi:o:t",{"usb_cam=", "file_path="}) #parses command line call for input parameters
  except getopt.GetoptError:
    print(helpMessage)
    sys.exit(2)
  for opt, arg in opts:
    if opt == '--help':
      print(helpMessage)
      sys.exit(2)
    elif opt in ("-i", "--usb_cam"):
      cam_value = arg
		elif opt in ("-o", "--file_path"):
			path = arg


  take_snapshots(cam_value, path)		#calls function

if __name__ == '__main__':
  main(sys.argv[1:])		#pases all input parameters on stack