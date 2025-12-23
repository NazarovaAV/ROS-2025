#!/usr/bin/env python3
import rospy
import tf
from tf.transformations import quaternion_from_euler
from turtlesim.msg import Pose

# Инициализируем узел
rospy.init_node('tf_turtle')

# Получаем приватный параметр (будем передавать из launch-файла)
turtlename = rospy.get_param('~turtle_tf_name')

def handle_turtle_pose(msg):
    # Создаем объект для публикации TF
    br = tf.TransformBroadcaster()
    
    # Публикуем преобразование:
    # 1. Линейное смещение: (x, y, 0) - из сообщения, Z = 0
    # 2. Вращение: только вокруг оси Z (theta)
    # 3. Время: сейчас
    # 4. Имя дочерней системы координат: turtlename (например, "turtle1")
    # 5. Имя родительской системы координат: "world"
    br.sendTransform((msg.x, msg.y, 0),
                     quaternion_from_euler(0, 0, msg.theta),
                     rospy.Time.now(),
                     turtlename,
                     "world")

# Подписываемся на топик input_pose (будем мапить в launch-файле)
rospy.Subscriber('input_pose', Pose, handle_turtle_pose)

# Бесконечный цикл обработки сообщений
rospy.spin()
