aantalStuks = int(input())
eenheidsprijs = float(input())
aantalBenodigdeBarcodes = int(input())
aantalMijlenPerFfc = int(input())

print(f"Phillips spendeerde ${aantalStuks*eenheidsprijs} voor {(aantalStuks//aantalBenodigdeBarcodes) * aantalMijlenPerFfc} frequent flyer mijlen.")