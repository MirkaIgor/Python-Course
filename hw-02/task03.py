"""В этой задаче вам необходимо создать объектную модель лыжника, спускающегося с горы. Лыжник может спускаться с горы в произвольном 
направлении. Однако для определенности положим, что он может перемещаться только в 3-х направлениях: Юг, Запад, Восток. При этом, 
если он идет галсами в направлении Запад или Восток, то его скорость составляет 1 м/с, а если катится прямо вниз (Юг), 
то скорость выше, и равна 5 м/с.
Создайте программную модель движения лыжника и определите: 1) какое расстояние он проедет через 17 секунд спуска, если каждую секунду 
он меняет направление движения случайным образом, и 2) в каком направлении он двигался каждую секунду.
Приложение должно состоять из двух классов. Первый класс наполните характеристиками и методами лыжника. Второй класс используйте 
для параметров движения. Управление программой и вывод результатов производите в основной функции main."""

from random import choice

class Moving:
    """
    Class represents moving parameters of Skiman

    --------------------
    Attributes:
        speed
            speed in m/s
        direction
            There are 3 posssible directions: West,South,East
    Methods:
        gen_direction()
            Generates random of possible directions
        toggle_speed()
            Sets the speed by current direction
        random_move()
            Change randomly moving parameters
        stop()
            Stops the Skiman
    """
    def __init__(self) -> None:
        """Initialize Moving object"""
        self.speed=0
        self.direction='S'

    def gen_direction(self):
        """Generates random of possible directions"""
        dirs = ['W','S','E']
        self.direction = choice(dirs)

    def toggle_speed(self):
        """Sets the speed by current direction"""
        speed_data = {'W':1,'S':5,'E':1}
        self.speed = speed_data[self.direction]

    def random_move(self):
        """Change randomly moving parameters"""
        self.gen_direction()
        self.toggle_speed()

    def stop(self):
        """Stops the Skiman"""
        self.speed=0
        self.direction='S'

class Skiman:
    """
    Class represents a Skiman

    -----------------
    Attributes:
        name        str
            Skiman's name
        move        Moving
            Skiman's parameters of moving, such as speed and direction
    Methods:
        start()
            Start moving
        stop()
            Stops moving
    """
    def __init__(self, name: str) -> None:
        """Initialize Skiman object"""
        self.name = name
        self.move = Moving()
    
    def start(self):
        """Start moving"""
        self.move.random_move()

    def stop(self):
        """Stops moving"""
        self.move.stop()

def main():
    """Launch this function to see task result"""
    skiman = Skiman('Steve')
    skiman.start()
    distance = 0
    directions = []
    for _ in range(17):
        distance+=skiman.move.speed
        directions.append(skiman.move.direction)
        skiman.move.random_move()
    skiman.stop()
    print(f"Skiman {skiman.name} passed {distance} meters. Dir changes: {directions}")

if __name__ == '__main__':
    main()

