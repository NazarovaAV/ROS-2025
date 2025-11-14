#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32, String

def overflow_detector():
    rospy.init_node('overflow_detector')
    
    # Публикуем сообщения о переполнении
    pub_overflow = rospy.Publisher('overflow', String, queue_size=10)
    
    def number_callback(msg):
        # Проверяем, достигли ли мы 100
        if msg.data >= 100:
            overflow_msg = "Overflow detected! Count reached 100, resetting counter"
            pub_overflow.publish(overflow_msg)
            rospy.logwarn(overflow_msg)
    
    # Подписываемся на топик с четными числами
    rospy.Subscriber('even_numbers', Int32, number_callback, queue_size=10)
    
    rospy.loginfo("Overflow detector started")
    rospy.spin()

if __name__ == '__main__':
    try:
        overflow_detector()
    except rospy.ROSInterruptException:
        rospy.loginfo("Overflow detector node terminated")
