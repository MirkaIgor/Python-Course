"""В этой задаче вам необходимо создать объектную модель лыжника, спускающегося с горы. Лыжник может спускаться с горы в произвольном 
направлении. Однако для определенности положим, что он может перемещаться только в 3-х направлениях: Юг, Запад, Восток. При этом, 
если он идет галсами в направлении Запад или Восток, то его скорость составляет 1 м/с, а если катится прямо вниз (Юг), 
то скорость выше, и равна 5 м/с.
Создайте программную модель движения лыжника и определите: 1) какое расстояние он проедет через 17 секунд спуска, если каждую секунду 
он меняет направление движения случайным образом, и 2) в каком направлении он двигался каждую секунду.
Приложение должно состоять из двух классов. Первый класс наполните характеристиками и методами лыжника. Второй класс используйте 
для параметров движения. Управление программой и вывод результатов производите в основной функции main."""

from math import dist
from random import choice

class Moving:
    def __init__(self) -> None:
        self.speed=0
        self.direction='S'

    def gen_direction(self):
        dirs = ['W','S','E']
        self.direction = choice(dirs)

    def toggle_speed(self):
        speed_data = {'W':1,'S':5,'E':1}
        self.speed = speed_data[self.direction]

    def random_move(self):
        self.gen_direction()
        self.toggle_speed()

    def stop(self):
        self.speed=0
        self.direction='S'

class Skiman:
    def __init__(self, name: str) -> None:
        self.name = name
        self.move = Moving()
    
    def start(self):
        self.move.random_move()

    def stop(self):
        self.move.stop()

def main():
    skiman = Skiman('Steve')
    skiman.start()
    distance = 0
    directions = []
    for time_ in range(17):
        distance+=skiman.move.speed
        directions.append(skiman.move.direction)
        skiman.move.random_move()
    skiman.stop()
    print(f"Skiman {skiman.name} passed {distance} meters. Dir changes: {directions}")

if __name__ == '__main__':
    main()

