class Building:
    total = 0

    def __init__(self, name):
        self.name = name

while Building.total < 40:
    Building.total += 1
    home = Building(f'Комплекс {Building.total}')
    print(home.name)


