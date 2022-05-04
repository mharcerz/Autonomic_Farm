import random
import pygame
from loader import beetroots, obstacles, grass, dry_soil, normal_soil, wet_soil
from constants import SQUARE_SIZE, ROWS, COLS, DRY_SOIL_COST, NORMAL_SOIL_COST, WET_SOIL_COST


class Field(pygame.sprite.Sprite):
    # słownik przechowujący wszystkie pola
    allFieldsDictionary = {}

    # wszystkie możliwe paramerty pola
    cropsTypes = ["", "Burak ćwikłowy", "Burak liściowy", "Burak cukrowy", "Burak zwyczajny"]
    typesOfProtectionMeasures = ["", "pestycydy", "doglebowe", "systemiczne"]
    soilStates = ["", "sucha", "zamokła", "w normie"]
    fertilizerTypes = ["", "organiczny", "wapniowy", "naturalny"]
    obstacleTypes = ["", "skała", "słup", "drzewo", "brak", "brak", "brak", "brak", "brak", "brak", "brak", "brak",
                     "brak", "brak", "brak", "brak", "brak", "brak", "brak", "brak", "brak", "brak"]
    isWatered = ["", "tak", "nie"]
    isCollected = ["", "tak", "nie"]

    # tworzenie objektu pole przez losowanie dostępnych parametrów
    def __init__(self, posX, posY):
        pygame.sprite.Sprite.__init__(self)
        self.posX = posX
        self.posY = posY
        if self.posX == ROWS - 1 and self.posY == COLS - 1:
            self.crop = Field.cropsTypes[0]
            self.protectionMeasure = Field.typesOfProtectionMeasures[0]
            self.soilState = Field.soilStates[0]
            self.fertilizer = Field.fertilizerTypes[0]
            self.obstacle = Field.obstacleTypes[0]
            self.isWatered = Field.isWatered[0]
            self.isCollected = Field.isCollected[0]
            self.czyMoznaTuStanac = "tak"
            self.cost = 0

            self.image = pygame.transform.scale(grass, (SQUARE_SIZE, SQUARE_SIZE))
            self.rect = self.image.get_rect()
            self.rect.topleft = (posY * SQUARE_SIZE, posX * SQUARE_SIZE)
        else:
            self.crop = Field.cropsTypes[random.randint(1, len(Field.cropsTypes) - 1)]
            self.protectionMeasure = Field.typesOfProtectionMeasures[
                random.randint(1, len(Field.typesOfProtectionMeasures) - 1)]
            self.soilState = Field.soilStates[random.randint(1, len(Field.soilStates) - 1)]
            self.fertilizer = Field.fertilizerTypes[random.randint(1, len(Field.fertilizerTypes) - 1)]
            self.obstacle = Field.obstacleTypes[random.randint(1, len(Field.obstacleTypes) - 1)]
            self.isWatered = Field.isWatered[random.randint(1, len(Field.isWatered) - 1)]
            self.isCollected = Field.isCollected[random.randint(1, len(Field.isCollected) - 1)]
            self.czyMoznaTuStanac = "nie" if self.obstacle != "brak" else "tak"

            self.image = pygame.transform.scale(self.selectImage(), (SQUARE_SIZE, SQUARE_SIZE))
            self.rect = self.image.get_rect()
            self.rect.topleft = (posY * SQUARE_SIZE, posX * SQUARE_SIZE)
            self.cost = 0

    # wypisanie parametrów pola
    def fieldParameters(self):
        print("\nParametry pola to:\nWpółrzędne: " + str(self.posX) + " " + str(self.posY) +
              "\nUprawa: " + self.crop +
              "\nŚrodek ochrony: " + self.protectionMeasure +
              "\nStan gleby: " + self.soilState +
              "\nStosowany nawóz: " + self.fertilizer +
              "\nCzy wymaga podlewania: " + self.isWatered +
              "\nCzy wymaga zbiorów: " + self.isCollected +
              "\nCzy na polu znajduje się przeszkoda: " + self.obstacle
              + "\nCzy mozna mozna stanac na tym polu: " + self.czyMoznaTuStanac)

    def can_u_be_here(self):
        if self.czyMoznaTuStanac == "tak":
            return 1
        else:
            return 0

    def set_image(self, img):
        self.image = pygame.transform.scale(img, (SQUARE_SIZE, SQUARE_SIZE))

    # dodawanie pola do słownika
    @staticmethod
    def addFieldToDict(dictionary, key, item):
        if key not in dictionary:
            dictionary[key] = item
            # item.fieldParameters()

    # wypisanie wszystkich pól ze słownika
    def printAllFieldsParameters(self, dictionary):
        for key in dictionary:
            print(key)
            dictionary[key].fieldParameters()

    def reset_field_image(self):
        self.image = pygame.transform.scale(self.selectImage(), (SQUARE_SIZE, SQUARE_SIZE))

    def selectImage(self):
        if self.czyMoznaTuStanac == "tak":
            # if self.crop == "Burak ćwikłowy":
            #     return beetroots[0]
            # elif self.crop == "Burak liściowy":
            #     return beetroots[1]
            # elif self.crop == "Burak cukrowy":
            #     return beetroots[2]
            # elif self.crop == "Burak zwyczajny":
            #     return beetroots[3]
            if self.soilState == "sucha":
                return dry_soil
            elif self.soilState == "w normie":
                return normal_soil
            elif self.soilState == "zamokła":
                return wet_soil
            else:
                return grass
        elif self.czyMoznaTuStanac == "nie":
            if self.obstacle == "slup":
                return obstacles[0]
            elif self.obstacle == "drzewo":
                return obstacles[1]
            elif self.obstacle == "skała":
                return obstacles[2]
            else:
                return obstacles[0]

    def getCost(self):
        if self.soilState == "sucha":
            return DRY_SOIL_COST
        elif self.soilState == "w normie":
            return NORMAL_SOIL_COST
        elif self.soilState == "zamokła":
            return WET_SOIL_COST
        else:
            return 0
