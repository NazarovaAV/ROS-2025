#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float32

rospy.init_node('summing_node')

# Храним полученные числа
numbers = [0, 0, 0]
received = [False, False, False]

def callback1(data):
    numbers[0] = data.data
    received[0] = True
    check_and_sum()

def callback2(data):
    numbers[1] = data.data
    received[1] = True
    check_and_sum()

def callback3(data):
    numbers[2] = data.data
    received[2] = True
    check_and_sum()

def check_and_sum():
    if all(received):
        total = sum(numbers)
        result = Float32()
        result.data = total
        pub.publish(result)
        rospy.loginfo(f"Сумма: {numbers[0]} + {numbers[1]} + {numbers[2]} = {total}")
        
        # Сбрасываем для следующего запроса
        received[0] = False
        received[1] = False
        received[2] = False

pub = rospy.Publisher('final_result', Float32, queue_size=10)

# Подписываемся на три топика с результатами
rospy.Subscriber('result1', Float32, callback1)
rospy.Subscriber('result2', Float32, callback2)
rospy.Subscriber('result3', Float32, callback3)

rospy.spin()
