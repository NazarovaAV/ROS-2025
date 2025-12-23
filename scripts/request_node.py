#!/usr/bin/env python3
import rospy
import sys
from std_msgs.msg import Float32

# Глобальная переменная для хранения результата
received_result = None
result_received = False

def result_callback(msg):
    """Callback для получения финального результата"""
    global received_result, result_received
    received_result = msg.data
    result_received = True
    rospy.loginfo(f"Получил результат в callback: {received_result}")

def main():
    global received_result, result_received
    
    rospy.init_node('request_node')
    
    # Проверяем аргументы
    if len(sys.argv) != 4:
        rospy.logerr("Нужно 3 числа!")
        rospy.loginfo("Пример: rosrun nazarova_alina_study_pkg request_node.py 2 4 5")
        print("Ожидается 3 числа, например: 2 4 5")
        sys.exit(1)
    
    # Преобразуем в числа
    try:
        num1 = float(sys.argv[1])
        num2 = float(sys.argv[2])
        num3 = float(sys.argv[3])
    except ValueError:
        rospy.logerr("Аргументы должны быть числами!")
        sys.exit(1)
    
    # ПОДПИСЫВАЕМСЯ на топик с результатом ПЕРЕД отправкой запроса
    rospy.Subscriber('final_result', Float32, result_callback)
    
    # Публикаторы для трех чисел
    pub1 = rospy.Publisher('input1', Float32, queue_size=10)
    pub2 = rospy.Publisher('input2', Float32, queue_size=10)
    pub3 = rospy.Publisher('input3', Float32, queue_size=10)
    
    # Ждем подключения подписчиков
    rospy.sleep(1)
    
    # Сбрасываем флаги перед новым запросом
    received_result = None
    result_received = False
    
    # Публикуем числа
    msg1 = Float32()
    msg1.data = num1
    pub1.publish(msg1)
    rospy.loginfo(f"Отправил первое число: {num1} (будет возведено в 3-ю степень)")
    
    rospy.sleep(0.3)
    
    msg2 = Float32()
    msg2.data = num2
    pub2.publish(msg2)
    rospy.loginfo(f"Отправил второе число: {num2} (будет возведено во 2-ю степень)")
    
    rospy.sleep(0.3)
    
    msg3 = Float32()
    msg3.data = num3
    pub3.publish(msg3)
    rospy.loginfo(f"Отправил третье число: {num3} (будет возведено в 1-ю степень)")
    
    # Ждем результат с таймаутом
    rospy.loginfo("Ожидаю результат...")
    timeout = 5  # секунд
    rate = rospy.Rate(10)  # 10 Hz
    
    start_time = rospy.get_time()
    while not rospy.is_shutdown() and (rospy.get_time() - start_time) < timeout:
        if result_received:
            # Выводим результат
            print(f"Результат: {received_result}")
            
            # Проверяем расчет для отладки
            expected = (num1 ** 3) + (num2 ** 2) + (num3 ** 1)
            rospy.loginfo(f"Ожидаемый результат: {expected}")
            rospy.loginfo(f"Фактический результат: {received_result}")
            
            return
        rate.sleep()
    
    if not result_received:
        rospy.logerr("Не получили ответ вовремя")
        print("Ошибка: не получили результат")

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
