import random
import pygame
import glob
import decision_tree
from loader import beetroots, obstacles, grass, dry_soil, normal_soil, wet_soil
from constants import SQUARE_SIZE, ROWS, COLS, DRY_SOIL_COST, NORMAL_SOIL_COST, WET_SOIL_COST


class Field(pygame.sprite.Sprite):
    # słownik przechowujący wszystkie pola
    allFieldsDictionary = {}

    crop_photo = ""
    sianie = ["", "zasiane", "nie_zasiane"]
    czy_rosnie = ["", "rosnie", "wyroslo"]
    suchosc_gleby = [0, 1, 2, 3, 4]
    owady = ["", "potrzebny_srodek_owady", "niepotrzebny_srodek_owady"]
    chwasty = ["", "sa_chwasty", "brak_chwastow"]
    ph_gleby = ["", "kwasowa", "w_normie", "zasadowa"]
    value = ["", "slup", "skala", "drzewo", "Marchewka", "Kalafior", "Ogorek", "Ziemniak", "Pomidor"]

    # tworzenie obiektu pole przez algorytm genetyczny a parametry wciąż losuje
    def __init__(self, posX, posY, value_given):
        pygame.sprite.Sprite.__init__(self)
        self.posX = posX
        self.posY = posY
        if self.posX == ROWS - 1 and self.posY == COLS - 1:
            self.crop = Field.value[0]
            self.sianie = Field.sianie[0]
            self.czy_rosnie = Field.czy_rosnie[0]
            self.suchosc_gleby = Field.suchosc_gleby[0]
            self.owady = Field.owady[0]
            self.chwasty = Field.chwasty[0]
            self.ph_gleby = Field.ph_gleby[0]
            self.obstacle = Field.value[0]

            self.czyMoznaTuStanac = "tak"
            self.cost = 0

            self.image = pygame.transform.scale(grass, (SQUARE_SIZE, SQUARE_SIZE))
            self.rect = self.image.get_rect()
            self.rect.topleft = (posY * SQUARE_SIZE, posX * SQUARE_SIZE)
        else:

            if value_given <= 3:
                self.obstacle = Field.value[value_given]
                self.czyMoznaTuStanac = "nie"
                self.crop = Field.value[0]
            else:
                self.obstacle = "brak"
                self.czyMoznaTuStanac = "tak"
                self.crop = Field.value[value_given]

                if self.crop == 'Ogorek':
                    file_path_type = ["resources/warzywa/Cucumber/*.jpg"]
                    images = glob.glob(random.choice(file_path_type))
                    self.crop_photo = str(random.choice(images))

                elif self.crop == 'Marchewka':
                    file_path_type = ["resources/warzywa/Carrot/*.jpg"]
                    images = glob.glob(random.choice(file_path_type))
                    self.crop_photo = str(random.choice(images))

                elif self.crop == 'Kalafior':
                    file_path_type = ["resources/warzywa/Cauliflower/*.jpg"]
                    images = glob.glob(random.choice(file_path_type))
                    self.crop_photo = str(random.choice(images))

                elif self.crop == 'Ziemniak':
                    file_path_type = ["resources/warzywa/Potato/*.jpg"]
                    images = glob.glob(random.choice(file_path_type))
                    self.crop_photo = str(random.choice(images))

                elif self.crop == 'Pomidor':
                    file_path_type = ["resources/warzywa/Tomato/*.jpg"]
                    images = glob.glob(random.choice(file_path_type))
                    self.crop_photo = str(random.choice(images))


                self.sianie = Field.sianie[
                    random.randint(1, len(Field.sianie) - 1)]
                self.czy_rosnie = Field.czy_rosnie[random.randint(1, len(Field.czy_rosnie) - 1)]
                self.suchosc_gleby = Field.suchosc_gleby[random.randint(0, len(Field.suchosc_gleby) - 1)]

                self.owady = Field.owady[random.randint(1, len(Field.owady) - 1)]
                self.chwasty = Field.chwasty[random.randint(1, len(Field.chwasty) - 1)]
                self.ph_gleby = Field.ph_gleby[random.randint(1, len(Field.ph_gleby) - 1)]



            self.image = pygame.transform.scale(self.selectImage(), (SQUARE_SIZE, SQUARE_SIZE))
            self.rect = self.image.get_rect()
            self.rect.topleft = (posY * SQUARE_SIZE, posX * SQUARE_SIZE)
            self.cost = 0

    # sprawdzenie czy mozna siac na danym polu
    def isVegetable(self):
        if self.czyMoznaTuStanac == "tak":
            return True

    # wypisanie parametrów pola
    def fieldParameters(self):

        if self.czyMoznaTuStanac == "tak":
            print("\nParametry pola to:\nWspółrzędne: " + str(self.posX) + ", " + str(self.posY) +
                  "\nUprawa: " + self.crop +
                  "\nCzy zasiane: " + self.sianie +
                  "\nCzy rosnie: " + self.czy_rosnie +
                  "\nStan gleby: " + str(self.suchosc_gleby) +
                  "\nOwady: " + self.owady +
                  "\nChwasty: " + self.chwasty +
                  "\nPh gleby: " + self.ph_gleby +
                  "\nCzy na polu znajduje się przeszkoda: " + self.obstacle
                  + "\nCzy mozna stanac na tym polu: " + self.czyMoznaTuStanac)
            print("Decyzja: " + decision_tree.make_decision(self))
        else:
            print("\nNie można tu stanąć! Tutaj znajduje się przeszkoda: " + str(self.obstacle))

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

    # wypisanie wszystkich pól ze słownika
    def printAllFieldsParameters(self, dictionary):
        for key in dictionary:
            print(key)
            dictionary[key].fieldParameters()

    def reset_field_image(self):
        self.image = pygame.transform.scale(self.selectImage(), (SQUARE_SIZE, SQUARE_SIZE))

    def return_crop_source(self):
        return self.crop_photo

    def selectImage(self):
        if self.czyMoznaTuStanac == "tak":
            if self.suchosc_gleby == 0 or self.suchosc_gleby == 1:
                return dry_soil
            elif self.suchosc_gleby == 2:
                return normal_soil
            elif self.suchosc_gleby == 3 or self.suchosc_gleby == 4:
                return wet_soil
            else:
                return grass
        elif self.czyMoznaTuStanac == "nie":
            if self.obstacle == "slup":
                return obstacles[0]
            elif self.obstacle == "drzewo":
                return obstacles[1]
            elif self.obstacle == "skala":
                return obstacles[2]
            else:
                return obstacles[0]

    def getCost(self):
        if self.suchosc_gleby == 0 or self.suchosc_gleby == 1:
            return DRY_SOIL_COST
        elif self.suchosc_gleby == 2:
            return NORMAL_SOIL_COST
        elif self.suchosc_gleby == 3 or self.suchosc_gleby == 4:
            return WET_SOIL_COST
        else:
            return 0
