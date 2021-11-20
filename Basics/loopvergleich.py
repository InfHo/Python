

einkaufsliste = ["Apfel", "Klopapier", "Bananen", "Brot", "Butter", "Marmelade"]

print(einkaufsliste)

for k in einkaufsliste:
    print(einkaufsliste.index(k)+100,k)


print(20*" - ")

for m in range(len(einkaufsliste)):
    print(m, einkaufsliste[m])

print(20*" - ")


for n,o in list(enumerate(einkaufsliste, start=100)):
    print(n,o)
