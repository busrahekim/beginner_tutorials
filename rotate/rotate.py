#Make the node an executable node
#chmod u+x ~/catkin_ws/src/beginner_tutorials1/src/rotate.py

import rospy
import sys
import math
from geometry_msgs.msg import Twist

rospy.init_node("movenode",anonymous=True)
pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)
vel_msg = Twist()

vel_msg.linear.x = 0.0
vel_msg.linear.y = 0.0
vel_msg.linear.z = 0.0	
vel_msg.angular.x = 0.0
vel_msg.angular.y = 0.0
vel_msg.angular.z = 0.0

rate = rospy.Rate(10)

def rotatetask(speed, angle, clockwise, lspeed=0):
	rospy.loginfo("Rotating...")
	angularspeed = speed * (math.pi/180)
	relativeangle = angle * (math.pi/180)
	

	vel_msg.linear.x = lspeed
	vel_msg.angular.z = clockwise * angularspeed
	
	t0 = rospy.Time.now().to_sec()
	current_angle = 0
	
	while(current_angle < relativeangle):
		pub.publish(vel_msg)
		t1 = rospy.Time.now().to_sec()
		current_angle = angularspeed * (t1-t0)
		rate.sleep()
	vel_msg.linear.x = 0.0
	vel_msg.angular.z = 0.0
	pub.publish(vel_msg)

if __name__ == "__main__":
	try:
	   rotatetask(5,90,-1)
	except rospy.ROSInterruptException:
	   pass
