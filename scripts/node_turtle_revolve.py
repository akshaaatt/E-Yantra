#!/usr/bin/env python

import rospy

from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

pi = 3.141592653589793238
        
def move_turtle(lin_vel,radius):

    ang_vel = lin_vel/radius
    rospy.init_node('move_turtle', anonymous=True)
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(10)
    vel = Twist()
    t0=rospy.Time.now().to_sec()
    angle=360
    radian_angle=2.1*pi
    current_angle=0

    vel.linear.x = lin_vel
    vel.linear.y = 0
    vel.linear.z = 0

    vel.angular.x = 0
    vel.angular.y = 0
    vel.angular.z = ang_vel

    while (current_angle<radian_angle):

		pub.publish(vel)
                t1 = rospy.Time.now().to_sec()
                current_angle = ang_vel*(t1-t0)
             
		rospy.loginfo("Moving in a circle")
                rospy.loginfo(t1-t0)
                rate.sleep()               
    rospy.loginfo("Goal Reached")
    vel.angular.z = abs(lin_vel)
    vel.linear.x = 0
    pub.publish(vel)
    
    rospy.spin()

if __name__ == '__main__':
    try:
        move_turtle(3.0,2.1)
    except rospy.ROSInterruptException:
        pass
