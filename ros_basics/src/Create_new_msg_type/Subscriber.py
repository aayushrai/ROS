#!/usr/bin/env python
import rospy
from ros_basics.msg import student_info

def student_details_print_callback(message):
    #get_caller_id(): Get fully resolved name of local node
    rospy.loginfo(rospy.get_caller_id() + "I heard student name is %s and his id is %d ,Coding lang is %s and percent %.2f", message.name,message.id,message.lang,message.percent)
    

rospy.init_node('Student_info_reciever', anonymous=True)

rospy.Subscriber("Student_Details", student_info,student_details_print_callback)

rospy.spin()
