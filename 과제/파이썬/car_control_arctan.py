"""
Pygame 라이브러리를 다운받아야 한다.

차량은 steering이 가능하며, 제자리 회전이 불가능하다.
steering 의 범위는 -30도 ~ +30도로 설정할 수 있다. 입력으로 40도가 들어가더라도 최대 각도인 30도로 보정된다.
ex) input 27: -> output: 27 ,  input 35: -> output: -> 30 ,  input: -56 -> output: -30

set_motor_value 함수 만을 작성하여 차량을 움직일 수 있다.
차량의 현재 위치는 self.x, self.y로, 차량이 바라보는 방향은 self.heading으로 활용할 수 있다.
heading은 x축을 기준으로 반시계 방향이 +방향이며, radian 단위를 가진다.

활용하고 싶은 인스턴스 변수(class 내의 함수)가 있다면 init 함수 내의 주석 안에 작성하여 활용할 수 있다.
추가적인 라이브러리는 자유롭게 활용이 가능하다.

display(World)는 Width 500, Height 500의 크기를 가진다.
display의 좌측 하단이 (0, 0)이며 우측 방향이 x+, 위쪽 방향이 y+ 이다.
첫 번째 목표 (300, 300)에 도달하여 1초 간 정지 후,
두 번째 목표 (425, 425)에 도달하여 1초 간 정지 후,
출발점 (75, 75)로 복귀하여 정지하도록 코드를 작성한다.

정지의 기준은 차 면적의 절반 이상이 목표점 안에 들어와야 한다.
목표 좌표를 스스로 바꿔가며 코드를 점검한다.
"""

import pygame
from math import *
from pygame.locals import *
import numpy as np
import time
import math
import sys

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

pygame.init()
# 화면의 범위는 가로 500, 세로 500
WIDTH = 500
HEIGHT = 500

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
rate = 100

# 목표 좌표
GOAL = [[250, 370], # 첫번째 목표
        [110, 325], # 두번째 목표
        [75, 75]]   # 마지막 목표는 출발점

def norm_steer(steer):
    while steer > 180:
        steer -= 2.0 * 180
    
    while steer < -180:
        steer += 2.0 * 180
    
    return steer
        
# 벡터 정규화
def norm_vector(vector):
    magnitude = np.sqrt(vector[0] ** 2 + vector[1] ** 2)
    
    if magnitude != 0:
        normalized_vector = vector / magnitude
        return normalized_vector
    
    else:
        return vector    

# 두 벡터 사잇각 구하기
def vector_angle(goal_vector, heading_vector):
    a = goal_vector[0] - heading_vector[0]
    b = goal_vector[1] - heading_vector[1]
    
    theta = np.arctan2(a, b)
    theta = np.degrees(theta)
    
    return theta
    

class Car:
    def __init__(self, initial_location):
        
        # == 현재 위치 (x,y)
        self.x, self.y = initial_location

        self.length = 15
        self.width = 10
        self.tread = 10
        self.wheel_radius = 1
        
        # == 차가 바라보는 방향 == 
        self.heading = 0

        self.speed = 0
        self.steer = 0
        self.predict_time = 0.01

        # ↓ ↓ ↓ ↓ ↓ ↓ init 에서 활용하고 싶은 인스턴스 변수가 있을 시 이곳에 작성 ↓ ↓ ↓ ↓ ↓ ↓
        self.step = 0
        # ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑

    # noinspection PyMethodMayBeStatic
    def convert_coordinate_l2g(self, d_x, d_y, d_theta):                    # local -> global 좌표 변환
        trans_matrix = np.array([[cos(d_theta), -sin(d_theta), 0],          # 변환 행렬
                                 [sin(d_theta), cos(d_theta), 0],
                                 [0, 0, 1]])
        return np.dot(trans_matrix, np.transpose([d_x, d_y, d_theta]))

    def generate_predict_pose(self):
        self.steer = min(max(self.steer, -30), 30)
        tan_dis = self.speed * self.predict_time  # 접선 이동 거리 (= 호의 길이)
        R = self.length / tan(radians(-self.steer)) if self.steer != 0 else float('inf')  # 곡률 반경
        d_theta = tan_dis / R

        predict_pose = [tan_dis, 0.0, 0.0] if R == float('inf') else [R * sin(d_theta), R * (1 - cos(d_theta)), d_theta]
        d_x, d_y, heading = np.transpose(self.convert_coordinate_l2g(predict_pose[0], predict_pose[1], d_theta + self.heading))
        return self.x + d_x, self.y + d_y, heading

    def move(self):
        self.x, self.y, self.heading = self.generate_predict_pose()

    def GUI_display(self):
        pygame.draw.circle(screen, GREEN, [GOAL[2][0], 500 - GOAL[2][1]], 10)
        pygame.draw.circle(screen, BLUE, [GOAL[0][0], 500 - GOAL[0][1]], 10)
        pygame.draw.circle(screen, BLUE, [GOAL[1][0], 500 - GOAL[1][1]], 10)

        a = atan2(self.width, self.length)
        b = sqrt(self.length ** 2 + self.width ** 2) / 2
        corner1 = [self.x + cos(self.heading - a) * b, 500 - (self.y + sin(self.heading - a) * b)]
        corner2 = [self.x + cos(self.heading + a) * b, 500 - (self.y + sin(self.heading + a) * b)]
        corner3 = [self.x + cos(self.heading + pi - a) * b, 500 - (self.y + sin(self.heading + pi - a) * b)]
        corner4 = [self.x + cos(self.heading + pi + a) * b, 500 - (self.y + sin(self.heading + pi + a) * b)]
        pygame.draw.polygon(screen, RED, [corner1, corner2, corner3, corner4])

    # set_motor_value 함수 내에서 자유롭게 작성
    
    def set_motor_value(self, count):
        self.speed = 150
        
        # 현재 위치 값
        loc = np.array([self.x, self.y])
        loc_int = loc.astype(int)
        
        # heading값
        heading_x = cos(self.heading)
        heading_y = sin(self.heading)
        heading_vector = np.array([heading_x, heading_y])
        
        norm_heading_vector = norm_vector(heading_vector)
        
        # 첫번째 목표 vector
        fr_x = GOAL[0][0] - self.x
        fr_y = GOAL[0][1] - self.y
        fr_vector = np.array([fr_x, fr_y])
        
        norm_fr_vector = norm_vector(fr_vector)
        
        fr_steer = vector_angle(norm_fr_vector, norm_heading_vector)     
        if self.step == 0:
            self.steer = norm_steer(fr_steer)
            if np.allclose(loc_int, GOAL[0], atol=1) == True:
                time.sleep(1)
                self.step = 1
        
        # 두번쟤 목표 vector
        sec_x = GOAL[1][0] - self.x
        sec_y = GOAL[1][1] - self.y
        sec_vector = np.array([sec_x, sec_y])
        
        norm_sec_vector = norm_vector(sec_vector)
        sec_steer = vector_angle(norm_sec_vector, norm_heading_vector)
        
        if self.step == 1:
            self.steer = norm_steer(sec_steer)
            if np.allclose(loc_int, GOAL[1], atol=1) == True:
                time.sleep(1)
                self.step = 2
        
        # 마지막 목표 vector
        thr_x = GOAL[2][0] - self.x
        thr_y = GOAL[2][1] - self.y
        thr_vector = np.array([thr_x, thr_y])
        
        norm_thr_vector = norm_vector(thr_vector)
        thr_steer = vector_angle(norm_thr_vector, norm_heading_vector)
        
        if self.step == 2:
            self.steer = norm_steer(-thr_steer)
            if np.allclose(loc_int, GOAL[2], atol=1) == True:
                time.sleep(1)
                sys.exit()

def main():
    car = Car([GOAL[2][0], GOAL[2][1]])
    count = 0
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return 0

        car.set_motor_value(count)
        car.move()

        screen.fill(WHITE)
        car.GUI_display()

        pygame.display.flip()
        clock.tick(rate)
        count += 1


if __name__ == '__main__':
    main()