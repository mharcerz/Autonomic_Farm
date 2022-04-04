import random

import pygame

from constants import SQUARE_SIZE

from loader import beetroots, obstacles, grass


class Field(pygame.sprite.Sprite):
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
        pygame.sprite.Sprite.__init__(self)
        self.posX = posX
        self.posY = posY
        self.crop = random.choice(Field.cropsTypes)
        self.protectionMeasure = random.choice(Field.typesOfProtectionMeasures)
        self.soilState = random.choice(Field.soilStates)
        self.fertilizer = random.choice(Field.fertilizerTypes)
        self.obstacle = random.choice(Field.obstacleTypes)
        self.isWatered = random.choice(Field.isWatered)
        self.isCollected = random.choice(Field.isCollected)

        self.image = pygame.transform.scale(self.selectImage(), (SQUARE_SIZE, SQUARE_SIZE))
        self.rect = self.image.get_rect()
        self.rect.topleft = (posY * SQUARE_SIZE, posX * SQUARE_SIZE)

    # wypisanie parametrów pola
    def fieldParameters(self):
        print("\nParametry pola to:\nWpółrzędne: " + str(self.posX) + " " + str(self.posY) +
              "\nUprawa: " + self.crop +
              "\nŚrodek ochrony: " + self.protectionMeasure +
              "\nStan gleby: " + self.soilState +
              "\nStosowany nawóz: " + self.fertilizer +
              "\nCzy wymaga podlewania: " + self.isWatered +
              "\nCzy wymaga zbiorów: " + self.isCollected +
              "\nCzy na polu znajduje się przeszkoda: " + self.obstacle)

    # dodawanie pola do słownika
    def addFieldToDict(self, dict, key, item):
        if key not in dict:
            dict[key] = item
            item.fieldParameters()

    # wypisanie wszystkich pól ze słownika
    def printAllFieldsParameters(self, dict):
        for key in dict:
            print(key)
            dict[key].fieldParameters()

    # TO BĘDZIE DO ZMIENIENIA ALE NA RAZIE NIE MAM POMYSLU
    def selectImage(self):
        if self.crop == "Burak ćwikłowy":
            return beetroots[0]
        elif self.crop == "Burak liściowy":
            return beetroots[1]
        elif self.crop == "Burak cukrowy":
            return beetroots[2]
        elif self.crop == "Burak zwyczajny":
            return beetroots[3]
