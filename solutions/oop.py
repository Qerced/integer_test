class IEngine:
    def start(self):
        pass

    def stop(self):
        pass

    def accelerate(self):
        pass


class StandardEngine(IEngine):
    def start(self):
        print('Стандартный двигатель запущен')

    def stop(self):
        print('Стандартный двигатель остановлен')

    def accelerate(self):
        print('Стандартный двигатель ускоряется')


class SportEngine(IEngine):
    def start(self):
        print('Спортивный двигатель запущен')

    def stop(self):
        print('Спортивный двигатель остановлен')

    def accelerate(self):
        print('Спортивный двигатель ускоряется быстро!')


class Car:
    def __init__(self, make, model, year, engine: IEngine):
        self.make = make
        self.model = model
        self.year = year
        self.__engine = engine

    def move(self):
        self.__engine.start()
        self.__engine.accelerate()
        print('Автомобиль движется')

    def brake(self):
        self.__engine.stop()
        print('Автомобиль тормозит')


class BMW(Car):
    def __init__(self, make, model, year, color, engine: IEngine):
        super().__init__(make, model, year, engine)
        self.color = color

    def honk(self):
        print('Бибика!')


bmw_with_standard_engine = BMW('BMW', '320i', 2023, 'Синий', StandardEngine())
bmw_with_sport_engine = BMW('BMW', 'M3', 2023, 'Красный', SportEngine())

bmw_with_standard_engine.move()
bmw_with_sport_engine.move()
