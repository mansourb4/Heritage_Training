# Simulateur de ville
# Créer 3 classes : Immeuble, Supermarché et Banque
# Superclass Batiment
# Créer 4 immeubles, 2 supermarché et 1 banque

class Batiment :
    def __init__(self, address, floor):
        self.address = address
        self.floor = floor

    def get_address(self):
        return self.address

    def get_floor(self):
        return self.floor

class Immeuble(Batiment) :
    def __init__(self, address, floor, window):
        super().__init__(address, floor)
        self.window = window
        print("\nBienvenue à la résidence Fatim-Zahra se trouvant au", address, "et qui compte plus de", floor, "étages ainsi que", window, "fenêtres !")

    def get_window(self):
        return self.window

fatim_zahra = Immeuble("276 boulevard Ziraoui", 7, 30)

class Supermarché(Batiment) :
    def __init__(self, address, floor, shelf):
        super().__init__(address, floor)
        self.shelf = shelf
        print("\nBienvenue au supermarché MarketPlace se trouvant au", address, "et qui compte plus de", floor,"étages ainsi que", shelf, "rayons !")

    def get_shelf(self):
        return self.shelf

marketplace = Supermarché("5 boulevard Abderrahim Bouabid", 2, 10)

class Banque(Batiment) :
    def __init__(self, address, floor, safe_box):
        super().__init__(address, floor)
        self.safe_box = safe_box
        print("\nBienvenue à la banque Bank of Africa se trouvant au", address, "et qui compte plus de", floor,"étages ainsi que", safe_box, "coffres forts !")

    def get_safe_box(self):
        return self.safe_box

bank_of_africa = Banque("9 allée des Hespérides", 1, 8)