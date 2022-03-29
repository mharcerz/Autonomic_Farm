import random


class Field:
    # słownik przechowujący wszystkie pola
    allFieldsDictionary = {}

    # wszystkie możliwe paramerty pola
    cropsTypes = ["Burak ćwikłowy", "Burak liściowy", "Burak cukrowy", "Burak zwyczajny"]
    typesOfProtectionMeasures = ["pestycydy", "doglebowe", "systemiczne"]
    soilStates = ["sucha", "zamokła", "w normie"]
    fertilizerTypes = ["organiczny", "wapniowy", "naturalny"]
    obstacleTypes = ["skała", "słup", "drzewo", "brak"]
    isWatered = ["tak", "nie"]
    isCollected = ["tak", "nie"]

    # tworzenie objektu pole przez losowanie dostępnych parametrów
    def __init__(self, posX, posY):
        self.posX = posX
        self.posY = posY
        self.crop = random.choice(Field.cropsTypes)
        self.protectionMeasure = random.choice(Field.typesOfProtectionMeasures)
        self.soilState = random.choice(Field.soilStates)
        self.fertilizer = random.choice(Field.fertilizerTypes)
        self.obstacle = random.choice(Field.obstacleTypes)
        self.isWatered = random.choice(Field.isWatered)
        self.isCollected = random.choice(Field.isCollected)

    # wypisanie parametrów pola
    def fieldParameters(self):
        print("\nParametry pola to:\nWpółrzędne: " + str(self.posX) + " " + str(
            self.posY) + "\nUprawa: " + self.crop + "\nŚrodek ochrony: " + self.protectionMeasure + "\nStan gleby: " + self.soilState + "\nStosowany nawóz: " + self.fertilizer + "\nCzy wymaga podlewania: " + self.isWatered + "\nCzy wymaga zbiorów: " + self.isCollected + "\nCzy na polu znajduje się przeszkoda: " + self.obstacle)

    # dodawanie pola do słownika
    def addFieldToDict(dict, key, item):
        if key not in dict:
            dict[key] = item
            item.fieldParameters()

    # wypisanie wszystkich pól ze słownika
    def printAllFieldsParameters(dict):
        for key in dict:
            print(key)
            dict[key].fieldParameters()
