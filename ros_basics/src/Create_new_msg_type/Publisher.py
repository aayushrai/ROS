#!/usr/bin/env python
# license removed for brevity
import rospy
from ros_basics.msg import student_info

def Sender():
    #create a new publisher. we specify the topic name, then type of message then the queue size
    pub = rospy.Publisher('Student_Details', student_info, queue_size=10)
    #we need to initialize the node
    # In ROS, nodes are uniquely named. If two nodes with the same
    # node are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'talker' node 
    rospy.init_node('Student_info_sender', anonymous=True)
    #set the loop rate
    rate = rospy.Rate(1) # 1hz
    #keep publishing until a Ctrl-C is pressed
    i = 0
    while not rospy.is_shutdown():
        student = student_info()
        student.name = input("Enter your name :")
        student.id = int(input("Enter your id :"))
        student.lang = input("Enter your programming lang :")
        student.percent = float(input("Enter your percentage :"))
        rospy.loginfo("Sending:")
        rospy.loginfo(student)
        pub.publish(student)
        rate.sleep()
        i=i+1

if __name__ == '__main__':
    try:
        Sender()
    except rospy.ROSInterruptException:
        pass
