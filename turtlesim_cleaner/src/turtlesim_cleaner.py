#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import time
import sys
import math

x =0
y =0
yaw = 0
cmd_vel_topic = "/turtle1/cmd_vel"
position_topic = "/turtle1/pose"


def PoseCallBack(pose_msg):
	global x,y,yaw
	x,y,yaw = pose_msg.x,pose_msg.y,pose_msg.theta


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

	while Distance_traveled < distance:
		rospy.loginfo("Start moving...")
		velocity_cmd_publisher.publish(velocity_msg)
		Distance_traveled += abs(0.5*(math.sqrt(((x-x0)**2)+((y-y0)**2))))
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

def go_to_goal(x_goal,y_goal):

	global x,y,yaw
	velocity_msg = Twist()
	distance = float("inf")
	while distance > 0.2:
		distance = abs(math.sqrt(((x-x_goal)**2)+((y-y_goal)**2)))
		P = .7
		linear_speed = P*distance

		K_angular = 4.0
		desired_angle_goal = math.atan2(y_goal-y, x_goal-x)
		angular_speed = (desired_angle_goal-yaw)*K_angular

		velocity_msg.linear.x = linear_speed
		velocity_msg.angular.z = angular_speed

		velocity_cmd_publisher.publish(velocity_msg)
		print("x=",x,"y=",y)


if __name__ == "__main__":
	try:
	  rospy.init_node("turtlesim_cleaner_node",anonymous=True)
	  velocity_cmd_publisher = rospy.Publisher(cmd_vel_topic,Twist,queue_size = 10)
	  position_subcriber =  rospy.Subscriber(position_topic,Pose,PoseCallBack)
	  time.sleep(2)
	  move(1.0,5,True)
	  rotate(30,90,False)
	  go_to_goal(1,1)
	except rospy.ROSInterruptException:
	  rospy.loginfo("Node terminate")
