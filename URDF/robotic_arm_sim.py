#!/usr/bin/env python

import rospy
from std_msgs.msg import Float64

def talker():
    pub = rospy.Publisher('/mrm/joint3_position_controller/command', Float64, queue_size=10)
    rospy.init_node('publisher', anonymous=False)
    rate = rospy.Rate(1) # 1hz

    while not rospy.is_shutdown():
        angle = 1.0
        rospy.loginfo(angle)
        pub.publish(angle)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass