#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32

result_mul = 1

def callback(data):
    global result_mul
    result_mul *= data.data
    print("Received student number:", data.data, "\nCurrent sum:", result_mul)

if __name__ == '__main__':
    try:
        rospy.init_node('student_number_subscriber', anonymous=True)
        rospy.Subscriber('second_input', Int32, callback)

        while not rospy.is_shutdown():
            # 두 숫자의 합을 출력하고, 곱할 숫자를 publish
            rospy.sleep(1)  # rospy.sleep를 사용하여 루프를 제어
    except rospy.ROSInterruptException:
        pass