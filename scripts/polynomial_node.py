#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float32

rospy.init_node('polynomial_node')

# Публикаторы для результатов (уже возведенных в степень)
pub1 = rospy.Publisher('result1', Float32, queue_size=10)
pub2 = rospy.Publisher('result2', Float32, queue_size=10)
pub3 = rospy.Publisher('result3', Float32, queue_size=10)

def callback1(data):
    # Первое число: в 3 степень
    result = data.data ** 3
    pub1.publish(result)
    rospy.loginfo(f"Число {data.data} -> {data.data}³ = {result}")

def callback2(data):
    # Второе число: в 2 степень
    result = data.data ** 2
    pub2.publish(result)
    rospy.loginfo(f"Число {data.data} -> {data.data}² = {result}")

def callback3(data):
    # Третье число: в 1 степень (оставляем как есть)
    result = data.data ** 1  # или просто data.data
    pub3.publish(result)
    rospy.loginfo(f"Число {data.data} -> {data.data}¹ = {result}")

# Подписываемся на три входящих топика
rospy.Subscriber('input1', Float32, callback1)
rospy.Subscriber('input2', Float32, callback2)
rospy.Subscriber('input3', Float32, callback3)

rospy.spin()
