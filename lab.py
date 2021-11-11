
class Cars(object):
    """dockstring"""
    eng = False
    fari = False
    def __init__(self, color, doors, carmark):
        """Construcktor"""
        self.__color = color
        self.doors = doors
        self.tires = 4
        self.carmark = carmark

    def delete(self):
        class_name = self.__class__.__name__
        print('{} удален'.format(class_name))
    def color(self,c):
        if type(c) == 'str':
            self.__color = c
        else:
            raise ValueError
    def brake(self):
        """
        Stop the car
        """
        self.eng = False
        return "%s braking" % self.carmark
    def drive(self):
        """
        Drive the car
        """
        return "Yahoo, I'm driving a %s %s" % (self.color, self.carmark)
    def turn_lights_on(self):
        self.fari = True
        return "Lights on now"

    def turn_off(self):
        self.fari = False
        return "Lights off now"

    def start_engine(self):
        self.eng = True
        return "Brrrr!!! Engine Started. You ready to move"

class Audi(Cars):
    """
    Audi class
    """
    engine = "V8, 4.2L, 420h.p"
    speed = "322 km/h"
class Mercedes(Cars):
    """
    Mersedec class
    """
    engine = "V8, 6.2L, 571h.p"
    speed = "350 km/h"

class Toyota(Cars):
    """
    Toyota class
    """
    engine = "2JZ-GE, 3.0L, 420h.p"
    speed = "250 km/h"

class Bmw(Cars):
    """ BMW class"""
    engine = "V8, 4.4L"
    speed = "305km/h"

auto = []
car_name=[]
a = ""

print("Список комманд:"'\n'"Для создания авто введите 'create auto'"'\n'"Для просмотра существующий авто введите 'list'"'\n'"Для выхода введите 'exit'")
while a != "exit":
    # процесс создания объекта
    a = input("Введите комманду: "'\n')
    if a == "create auto":
        c = input("Выберите марку: Mercedes, audi, bmw:  ")
        car_name.append(input("Введите название авто: "))
        b = input("Выберете цвет: ")
        if c == "Mercedes":
            new_car = Mercedes(b,4,car_name[-1])
        elif c == "audi":
            new_car = Audi(b,4,car_name[-1])
        elif c == "bmw":
            new_car = Bmw(b,4,car_name[-1])
        auto.append(new_car)
        print('\n'"Автомобиль {} создан".format(car_name[-1]),'\n')
    # процесс удаления объектов
    elif a == "delete auto":
        del_name = input('\n'"Введите имя машины, которую нужно удалить: ")
        k = 0
        for i in car_name:
            if i == del_name:
                del auto[k]
                del car_name[k]
            k += 1
        print(del_name, "Удален")
    # вывод списка имеющихся машин
    elif a == "list":
        for i in car_name:
            print(i)
    # включение / выключение фар
    elif a == "lights":
        for i in range(len(car_name)):
            print("{}'s lights: ".format(car_name[i]),auto[i].fari)
    elif a == "choose car":
        name_light = input("Введите имя машины, с которой хотите производитеть действия (вкл/вкл фары, вкл/выкл двигатель: ")
        comm = input("Вы выбрали автомобиль под названием {}'\n'Введите команду для вкл/выкл фар и двигателя: ".format(name_light))
        if comm == "light on":
            for i in range(len(car_name)):
                if car_name[i] == name_light:
                    auto[i].turn_lights_on()
                    print("{}'s lights now:".format(name_light), auto[i].fari)
        elif comm == "light off":    
            for i in range(len(car_name)):
                if car_name[i] == name_light:
                    auto[i].turn_lights_on()
                    print("{}'s lights now:".format(name_light), auto[i].fari)
        elif comm == "engine on":    
            for i in range(len(car_name)):
                if car_name[i] == name_light:
                    auto[i].start_engine()
                    print("{}'s двигатель сейчас:".format(name_light), auto[i].eng)
        elif comm == "engine off":    
            for i in range(len(car_name)):
                if car_name[i] == name_light:
                    auto[i].brake()
                    print("{}'s lights now:".format(name_light), auto[i].eng)
    elif a == "engines":
        for i in range(len(car_name)):
            print("{}'s lights: ".format(car_name[i]),auto[i].eng)