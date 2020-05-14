#!/usr/bin/env python

from ros_basics.srv import AddTwoInts
from ros_basics.srv import AddTwoIntsResponse
from ros_basics.srv import AddTwoIntsRequest
import rospy
import sys

def AddTwoIntsServer(x,y):
	rospy.wait_for_service("AddTwoIntsService")
	try:
		add_two_ints = rospy.ServiceProxy("AddTwoIntsService",AddTwoInts)
		response = add_two_ints(x,y)
		return response.sum
	except rospy.ServiceException as e:
		print("Service call fialed %s"%e)

def usage():
	print("%s [x,y]"%sys.argv[0])



if __name__ == "__main__":
	if len(sys.argv) == 3:
		x = int(sys.argv[1])
		y = int(sys.argv[2])
	else:
		print(usage())
	print("requesting %s + %s" %(x,y))
	print("responsed %s + %s = %s"%(x,y,AddTwoIntsServer(x,y)))

