class TrafficLight:
    def __init__(self):
        self.__color = "Красный"

    def running(self):
        import time

        while True:
            print(f"\033[31m{self.__color}")
            time.sleep(7)

            print(f"\033[33mЖелтый")
            time.sleep(2)

            print(f"\033[32mЗеленый")
            time.sleep(5)

            if self.__color != "Красный":
                print("Ошибка: Порядок нарушен!")
                break

            self.__color = "Желтый"
            self.__color = "Зеленый"
            self.__color = "Красный"


traffic_light = TrafficLight()
traffic_light.running()