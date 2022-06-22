#Make the node an executable node
#chmod u+x ~/catkin_ws/src/beginner_tutorials1/src/rotate2.py

import rospy
import sys
import math
from geometry_msgs.msg import Twist

nodename = "robot_0"
rospy.init_node("rotatenode",anonymous=True)
pub = rospy.Publisher(nodename+"/cmd_vel", Twist, queue_size=10)
vel_msg = Twist()

vel_msg.linear.x = 0.0
vel_msg.linear.y = 0.0
vel_msg.linear.z = 0.0	
vel_msg.angular.x = 0.0
vel_msg.angular.y = 0.0
vel_msg.angular.z = 0.0

#rate = rospy.Rate(10)

ctrl_c = False

def rotaterobot(speed, angle, clockwise, lspeed=0):
	rospy.loginfo("Lets rotate..!")
	angularspeed = speed * (math.pi/180)
	relativeangle = angle * (math.pi/180)
	rate = rospy.Rate(10)

	vel_msg.linear.x = lspeed
	vel_msg.angular.z = clockwise * abs(angularspeed)
	

	while not ctrl_c:
		connections = pub.get_num_connections()
		if connections > 0:
			pub.publish(vel_msg)
			break
		else:
			rate.sleep()	
	

	t0 = rospy.Time.now().to_sec()
	current_angle = 0

	while(current_angle < relativeangle):
		pub.publish(vel_msg)
		t1 = rospy.Time.now().to_sec()
		current_angle = angularspeed * (t1-t0)
		rate.sleep()
	stop_robot()

def shutdowntask():
	stop_robot()
	ctrl_c= True

def stop_robot():
	rospy.loginfo("shutdown time! stop the robot")
	vel_msg.linear.x = 0.0
	vel_msg.angular.z = 0.0
	pub.publish(vel_msg)

if __name__ == "__main__":
	try:
	   rospy.on_shutdown(shutdowntask)
	   rotaterobot(60.0, 90.0, -1, 0)
	except rospy.ROSInterruptException:
	   pass
