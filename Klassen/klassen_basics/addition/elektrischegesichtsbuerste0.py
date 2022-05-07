
class elektrischegesichtsbuerste:
    def __init__(self, motor):
        self.motor = motor


elektrobuerste_1 = elektrischegesichtsbuerste("Vibrationsmotor")
elektrobuerste_2 = elektrischegesichtsbuerste("brushless motor")

print(elektrobuerste_1.motor)
print(elektrobuerste_2.motor)
