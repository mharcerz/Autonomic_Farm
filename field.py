import random
class Field:
    #słownik przechowujący wszystkie pola
    allFields={}

    #wszystkie możliwe paramerty pola
    typyUprawy=["Burak ćwikłowy","Burak liściowy","Burak cukrowy","Burak zwyczajny"]
    typySrodkowOchrony=["pestycydy","doglebowe","systemiczne"]
    stanyGleby=["sucha","zamokła","w normie"]
    typyNawozow=["organiczny","wapniowy","naturalny"]
    podlewanie=["tak","nie"]
    zbiory=["tak","nie"]
    typyPrzeszkod=["skała","słup","drzewo","brak"]
    #tworzenie objektu pole przez losowanie dostępnych parametrów 
    def __init__(self,wspolrzednaX,wspolrzednaY):
        self.wspolrzednaX=wspolrzednaX
        self.wspolrzednaY=wspolrzednaY
        self.uprawa=random.choice(Field.typyUprawy)
        self.srodekOchrony=random.choice(Field.typySrodkowOchrony)
        self.stanGleby=random.choice(Field.stanyGleby)
        self.nawoz=random.choice(Field.typyNawozow)
        self.wymagaPodlewania=random.choice(Field.podlewanie)
        self.wymagaZbiorow=random.choice(Field.zbiory)
        self.przeszkoda=random.choice(Field.typyPrzeszkod)

    #wypisanie parametrów pola 
    def fieldParameters(self):
        print("\nParametry pola to:\nWpółrzędne: "+str(self.wspolrzednaX)+" "+str(self.wspolrzednaY)+"\nUprawa: "+ self.uprawa+"\nŚrodek ochrony: "+self.srodekOchrony+"\nStan gleby: "+self.stanGleby+"\nStosowany nawóz: "+self.nawoz+"\nCzy wymaga podlewania: "+self.wymagaPodlewania+"\nCzy wymaga zbiorów: "+self.wymagaZbiorow+"\nCzy na polu znajduje się przeszkoda: "+self.przeszkoda)

    #dodawanie pola do słownika
    def addFieldToDict(dict,key,item):
        if key not in dict:
            dict[key]=item
            item.fieldParameters()
    
    #wypisanie wszystkich pól ze słownika
    def printAllFieldsParameters(dict):
        for key in dict:
            print(key)
            dict[key].fieldParameters()