# 4.Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
class Car:
    speed: int
    color: str
    name: str
    is_police: bool

    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"Машина {self.name} поехала")

    def stop(self):
        print(f"Машина {self.name} остановилась")

    def turn_right(self):
        print(f"Машина {self.name} повернула направо")

    def turn_left(self):
        print(f"Машина {self.name} повернула налево")

    def show_speed(self):
        print(f"Текущая скорость автомобиля {self.name} равна {self.speed}")


class TownCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            print(
                f"Текущая скорость автомобиля {self.name} - {self.speed} км/ч\nПревышена допустимая скорость 60 км/ч.")
        else:
            print(f"Текущая скорость автомобиля {self.name} равна {self.speed} км/ч")


class SportCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            print(
                f"Текущая скорость автомобиля {self.name} - {self.speed} км/ч\nПревышена допустимая скорость 60 км/ч.")
        else:
            print(f"Текущая скорость автомобиля {self.name} равна {self.speed}")


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)


Kia = TownCar(80, "red", "KIA")
Ford = WorkCar(95, "white", "Ford")

Kia.go()
Kia.show_speed()

# Ford.turn_left()
# Ford.show_speed()
