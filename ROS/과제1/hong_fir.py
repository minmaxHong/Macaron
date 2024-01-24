#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32

def publisher():
    rospy.init_node('student_number_publisher', anonymous=True)
    pub = rospy.Publisher('first_input', Int32, queue_size=10)
    rate = rospy.Rate(1)  # 1 Hz, 필요에 따라 조정

    while not rospy.is_shutdown():
        # 2개의 정수를 입력 받음
        input_num_1 = int(input("첫 번째 숫자를 입력하세요: "))
        input_num_2 = int(input("두 번째 숫자를 입력하세요: "))

        # 두 숫자를 각각 퍼블리시
        pub.publish(input_num_1)
        rate.sleep()  # rate.sleep()를 사용하여 간격을 두고 메시지를 전송
        pub.publish(input_num_2)
        rate.sleep()

if __name__ == '__main__': # 일단 파이썬에서 메인함수를 만들때 __붙이는 양식 확인
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass