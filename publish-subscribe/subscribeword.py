#! /usr/bin/env python



#chmod u+x ~/catkin_ws/src/beginner_tutorials/src/subscribeword.py

import rospy
from std_msgs.msg import String

rospy.init_node("stringsub")

def callbackfunc(msg):
	print(msg)

pub = rospy.Subscriber("/words", String, callbackfunc)

rospy.spin()


