#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import time
import sys
import math


cmd_vel_topic = "/turtle1/cmd_vel"
position_topic = "/turtle1/pose"

def move(speed,distance,isforward):
	velocity_msg = Twist()
	global x,y
	x0 = x
	y0 = y

	if isforward:
	   velocity_msg.linear.x = abs(speed)
	else:
	   velocity_msg.linear.x = -abs(speed)

	Distance_traveled = 0
	loop_rate = rospy.Rate(10)
#	velocity_cmd_publisher = rospy.Publisher(cmd_vel_topic,Twist,queue_size=10)
    t0 = rospy.Time.now().to_sec()
	while Distance_traveled < distance:
		rospy.loginfo("Start moving...")
		velocity_cmd_publisher.publish(velocity_msg)
		t1 = rospy.Time.now().to_sec()
		Distance_traveled = (t1-t0)*speed
		print(Distance_traveled)
	rospy.loginfo("reached")
	velocity_msg.linear.x = 0
	velocity_cmd_publisher.publish(velocity_msg)

def rotate(angular_speed_degree,relative_angle_degree,clockwise):
    global yaw
    theta0 = yaw 

    velocity_msg = Twist()
    velocity_msg.linear.x =0
    velocity_msg.linear.y = 0
    velocity_msg.linear.z = 0
    velocity_msg.angular.x = 0
    velocity_msg.angular.y = 0
    velocity_msg.angular.z = 0

    angular_speed_radian = math.radians(abs(angular_speed_degree))

    if clockwise:
    	velocity_msg.angular.z = -abs(angular_speed_radian)
    else:
    	velocity_msg.angular.z = abs(angular_speed_radian)

    current_angle_degree = float("-inf")
    loop_rate = rospy.Rate(10)
 #   velocity_cmd_publisher = rospy.Publisher(cmd_vel_topic,Twist,queue_size=10)

    t0 = rospy.Time.now().to_sec()

    while current_angle_degree <= relative_angle_degree:
    	rospy.loginfo("Start rotating")
    	velocity_cmd_publisher.publish(velocity_msg)
    	t1 = rospy.Time.now().to_sec()
    	current_angle_degree = (t1-t0)*(angular_speed_degree)

    	loop_rate.sleep()
    rospy.loginfo("reached")
    velocity_msg.angular.z = 0
    velocity_cmd_publisher.publish(velocity_msg)

if __name__ == "__main__":
	try:
	  rospy.init_node("turtlesim_cleaner_node",anonymous=True)
	  velocity_cmd_publisher = rospy.Publisher(cmd_vel_topic,Twist,queue_size = 10)
	  time.sleep(2)
	  move(.5,.5,True)
	  rotate(30,90,False)
	except rospy.ROSInterruptException:
	  rospy.loginfo("Node terminate")
