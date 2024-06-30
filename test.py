class MushroomsCollector:
    # Проверьте, нет ли здесь ошибки:
    def __init__(self, mushroom=[]):
        self.mushroom = mushroom
    
    def is_poisonous(self, mushroom_name):
        Flag = None
        if mushroom_name == 'Мухомор' or mushroom_name == 'Поганка':
            Flag = True
        else:
            Flag = False
        return Flag

    # Допишите метод.

    def add_mushroom(self, mushroom_name):
        if self.is_poisonous(mushroom_name) is False:
            self.mushroom.append(mushroom_name)
        else:
            print('Нельзя добавить ядовитый гриб')

    def __str__(self):
        return (f"{' '.join(self.mushroom)}")
    # Напишите магический метод __str__,
    # возвращающий перечень грибов из списка mushrooms
    # через запятую.


# Пример запуска для самопроверки
collector_1 = MushroomsCollector()
collector_1.add_mushroom('Мухомор')
collector_1.add_mushroom('Подосиновик')
collector_1.add_mushroom('Белый')
collector_1.add_mushroom('Поганка')
print(collector_1)

collector_2 = MushroomsCollector()
collector_2.add_mushroom('Лисичка')
print(collector_1)
print(collector_2)

