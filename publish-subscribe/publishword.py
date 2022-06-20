#! /usr/bin/env python



#chmod u+x ~/catkin_ws/src/beginner_tutorials/src/publishword.py

import rospy
from std_msgs.msg import String

rospy.init_node("stringpub")
pub = rospy.Publisher("/words", String, queue_size=10)

msg= "Hellooo"
rate= rospy.Rate(10)


while not rospy.is_shutdown():
	print(msg)
	pub.publish(msg)
	rate.sleep()
