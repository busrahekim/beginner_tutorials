#! /usr/bin/env python



#Make the node an executable node
#chmod u+x ~/catkin_ws/src/beginner_tutorials1/src/scanenvironment.py

import rospy
import sys
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

#nodeid = str(sys.argv[1])
#nodename = "robot_"+nodeid

vel_msg = Twist()
	
vel_msg.linear.x = 0.5
vel_msg.linear.y = 0.0
vel_msg.linear.z = 0.0
	
vel_msg.angular.x = 0.0
vel_msg.angular.y = 0.0
vel_msg.angular.z = 0.0

def callback(msg):
	print('s[0]: ' + str(msg.ranges[0]))
	print('s[150]: ' + str(msg.ranges[150]))	
	print('s[210]: ' + str(msg.ranges[210]))
	
	if(msg.ranges[20]> 0.5):
		vel_msg.linear.x = 0.5
		vel_msg.linear.y = 0.0
	else:
		vel_msg.linear.x = 0.0
 		vel_msg.linear.y = 0.0

	pub.publish(vel_msg)

rospy.init_node("nodename",anonymous=True)
pub = rospy.Publisher("/cmd_vel", Twist, queue_size=10)
sub = rospy.Subscriber("/scan", LaserScan, callback)

rospy.spin()
