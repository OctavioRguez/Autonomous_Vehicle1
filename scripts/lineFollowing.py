#!/usr/bin/env python
import rospy
import numpy as np
import cv2
import cv_bridge
from sensor_msgs.msg import Image
from std_msgs.msg import Float32

class LineFollowing:
    # Variables
    def __init__(self):
        self._flag = False # Flag to start once the first frame is received
        self.__bridge = cv_bridge.CvBridge() # Bridge to conversion between imgmsg and cv2

	self.__error = 0.0 # Save the error

    # Callback to receive the frames from camera
    def _retrieveImage(self, msg):
	try:
	    # Conversion from imgmsg to cv2
            self.__img = self.__bridge.imgmsg_to_cv2(msg, desired_encoding = 'passthrough')
	except cv_bridge.CvBridgeError as e:
	    rospy.loginfo(e) # Catch an error
	
	# Change flag to start the Image processing
        self._flag = True

    # Crop and binarize the image
    def __preProcessing(self):
	self.__img = self.__img[360: , :]
	grayImage = cv2.cvtColor(self.__img, cv2.COLOR_BGR2GRAY)
        self.__binaryImage = cv2.threshold(grayImage, 100, 255, cv2.THRESH_BINARY)[1]
	#contours = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]

	self.prueba = self.__bridge.cv2_to_imgmsg(self.__img, encoding = 'passthrough')

    def _lineError(self):
	self.__preProcessing()

	#if len(contours) > 0:
	    #largest_contour = max(contours, key = cv2.contourArea)

        # Calculate the line error
        moments = cv2.moments(self.__binaryImage)
        if moments['m00'] > 0:
            cx = int(moments['m10'] / moments['m00'])
            self.__error = cx - self.__img.shape[1] / 2

    def getError(self):
	return self.__error

# Stop Condition
def stop():
    # Stop message
    print("Stopping")

if __name__=='__main__':
    # Initialise and Setup node
    rospy.init_node("Line_Following")
    rospy.on_shutdown(stop)

    hz = 2 # Frequency (Hz)
    rate = rospy.Rate(hz)

    follow = LineFollowing() # LineFollowing class object

    # Publishers and subscribers
    rospy.Subscriber("/video_source/raw", Image, image._retrieveImage) # Get the image from the camera

    prueba_pub = rospy.Publisher("/prueba/raw", Image, queue_size = 2) # Prueba
    error_pub = rospy.PUblisher("/error", Float32, queue_size = 2) # Error

    print("The Line Following is Running")

    # Run the node
    while not rospy.is_shutdown():
        # Code
     	prueba_pub.publish(follow.prueba)
	error_pub.publish(follow.getError())

        rate.sleep()
