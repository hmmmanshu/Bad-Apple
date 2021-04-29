# python BadApple.py --video videos/videoplayback.m4v
from imutils.video import FileVideoStream
from imutils.video import FPS
from os import system,name	
import numpy as np
import argparse
import imutils
import time
import cv2

def clear():
    '''
    Clear console
    '''
    _ = system('cls')

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", required=True,
	help="path to input video file")
args = vars(ap.parse_args())

# start the file video stream thread and allow the buffer to
# start to fill
print("[INFO] starting video file thread...")
fvs = FileVideoStream(args["video"]).start()
time.sleep(1.0)

# start the FPS timer
fps = FPS().start()
width = 48
height = 36

# loop over frames from the video file stream
while fvs.more():
	# grab the frame from the threaded video file stream, resize
	# it, and convert it to grayscale (while still retaining 3 channels)
	frame = fvs.read()
	frame = imutils.resize(frame, width=900)
	frame = cv2.resize(frame, (48, 36))
	frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	frame = np.dstack([frame, frame, frame])
	newframe = np.array(frame)
	for i in range(height):
		for j in range(width):
			current_ele = newframe[i][j][0]
			if(current_ele == 0):
				print(' ',end=' ')
			else:
				print('8',end=' ')
		print()
	clear()
	cv2.waitKey(1)
	fps.update()

# stop the timer and display FPS information
fps.stop()
print("[INFO] elasped time: {:.2f}".format(fps.elapsed()))
print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))

# do a bit of cleanup
cv2.destroyAllWindows()
fvs.stop()