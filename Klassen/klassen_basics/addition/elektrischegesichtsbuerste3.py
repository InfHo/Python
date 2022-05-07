class elektrischegesichtsbuerste:
    def __init__(self, name, motor, farbe, borsten):
        self.name = name
        self.motor = motor
        self.farbe = farbe
        self.borsten = borsten

    def __add__(self, other):
        return f'{self.name} + {other.name} haben zusammen {self.borsten+other.borsten} Borsten'

    def __str__(self):
        return f'Die elektrische Gesichtsbürste {self.name} ist {self.farbe} und hat einen {self.motor}\
und {self.borsten} Borsten'

elektrobuerste_1 = elektrischegesichtsbuerste("Bürste2000", "Vibrationsmotor", "schwarz", 3000)
elektrobuerste_2 = elektrischegesichtsbuerste("Bürste1000", "brushless motor", "weiss", 2200)

print(elektrobuerste_1)
print(elektrobuerste_2)

print(elektrobuerste_1+elektrobuerste_2)

