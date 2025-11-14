#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32

def even_publisher():
    rospy.init_node('even_publisher')
    pub = rospy.Publisher('even_numbers', Int32, queue_size=10)
    rate = rospy.Rate(10)  # 10 Hz
    count = 0
    
    rospy.loginfo("Starting even number publisher at 10 Hz")
    
    while not rospy.is_shutdown():
        # Публикуем четное число
        pub.publish(count)
        rospy.loginfo("Published even number: %d", count)
        count += 2
        
        # Проверяем достижение 100 и сбрасываем
        if count > 100:
            rospy.loginfo("Counter reset from %d to 0", count)
            count = 0
            
        rate.sleep()

if __name__ == '__main__':
    try:
        even_publisher()
    except rospy.ROSInterruptException:
        rospy.loginfo("Even publisher node terminated")
