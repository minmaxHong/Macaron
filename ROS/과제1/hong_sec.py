#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32

result_sum = 0  # 두 숫자의 합을 저장할 전역 변수
input_flag = None

def callback(data):
    global result_sum
    result_sum += data.data
    print("Received student number:", data.data, "\nCurrent sum:", result_sum)

def multiply_constant_publisher():
    pub = rospy.Publisher('second_input', Int32, queue_size=10)
    rate = rospy.Rate(1)  # 1 Hz, 필요에 따라 조정

    while not rospy.is_shutdown():
        multiply_constant = int(input("곱할 숫자를 입력하세요: "))
        pub.publish(result_sum)
        rate.sleep()
        pub.publish(multiply_constant)
        rate.sleep()

if __name__ == '__main__':
    try:
        rospy.init_node('student_number_subscriber', anonymous=True)
        rospy.Subscriber('first_input', Int32, callback)

        while not rospy.is_shutdown():
            # 두 숫자의 합을 출력하고, 곱할 숫자를 publish
            # print("Current sum:", result_sum)
            if input_flag == None:
                multiply_constant_publisher()
                input_flag = True
            else:
                break
            rospy.sleep(1)  # rospy.sleep를 사용하여 루프를 제어
    except rospy.ROSInterruptException:
        pass