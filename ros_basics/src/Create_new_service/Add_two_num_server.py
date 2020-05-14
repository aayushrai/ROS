#!/usr/bin/env python

from ros_basics.srv import AddTwoInts
from ros_basics.srv import AddTwoIntsResponse
from ros_basics.srv import AddTwoIntsRequest
import rospy

def AddTwoIntsHandler(req):
	sm = req.a + req.b
	print("Returning %s + %s = %s"%(req.a,req.b,sm))
	return AddTwoIntsResponse(sm)

def AddTwoIntsServer():
	rospy.init_node("AddTwoIntsNode")
	s = rospy.Service("AddTwoIntsService",AddTwoInts,AddTwoIntsHandler)
	print("Waiting for request")
	rospy.spin()

if __name__ == "__main__":
	AddTwoIntsServer()
