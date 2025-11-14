#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def overflow_callback(msg):
    rospy.loginfo("🚨 OVERFLOW EVENT: %s", msg.data)

def overflow_listener():
    rospy.init_node('overflow_listener')
    rospy.Subscriber('overflow', String, overflow_callback, queue_size=10)
    
    rospy.loginfo("Overflow listener started, waiting for overflow events...")
    rospy.spin()

if __name__ == '__main__':
    overflow_listener()
