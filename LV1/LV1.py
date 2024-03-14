# zadatak 1
"""
def total_euro(radni_sati, cijena_sata):
    return radni_sati * cijena_sata

def main():
    radni_sati = float(input("Radni sati: "))
    cijena_sata = float(input("eura/h: "))

    ukupno = total_euro(radni_sati, cijena_sata)

    print("Ukupno:", ukupno, "eura")

main()

"""

#Zadatak 2
"""
def main():
    try:
        ocjena = float(input("Unesite ocjenu (između 0.0 i 1.0): "))
        if 0.0 <= ocjena <= 1.0:
            if ocjena >= 0.9:
                print("A")
            elif ocjena >= 0.8:
                print("B")
            elif ocjena >= 0.7:
                print("C")
            elif ocjena >= 0.6:
                print("D")
            elif ocjena < 0.6:
                print("F")
        else:
            print("Uneseni broj je izvan intervala [0.0, 1.0]")
    except ValueError:
        print("Molimo unesite broj!")


main() 

"""


# Zadatak 3

"""
def main():
    brojevi = []
    
    while True:
        unos = input("Unesite broj ('Done' za kraj): ").strip().lower()
        
        if unos == 'done':
            break
        
        try:
            brojevi.append(float(unos))
        except ValueError:
            pass

    if brojevi:
        print("Ukupno unesenih brojeva:", len(brojevi))
        print("Srednja vrijednost:", sum(brojevi) / len(brojevi))
        print("Minimalna vrijednost:", min(brojevi))
        print("Maksimalna vrijednost:", max(brojevi))
        
        brojevi.sort()
        print("Sortirana lista brojeva:", brojevi)
    else:
        print("Niste unijeli nijedan broj.")


main()

"""

#Zadatak 4

"""
def prosjecni_spam():
    file = input("Unesite ime tekstualne datoteke: ")
    ukupna_pouzdanost = 0
    br = 0
    
    try:
        with open(file, 'r') as file:
            for line in file:
                if line.startswith("X-DSPAM-Confidence:"):
                    ukupna_pouzdanost += float(line.split(":")[1])
                    br += 1
            count
            if br > 0:
                print(f"Average X-DSPAM-Confidence: {ukupna_pouzdanost / br}")
    except FileNotFoundError:
        print("Datoteka nije pronađena.")

prosjecni_spam()

"""

#Zadatak 5

def main():
    file = "song.txt" 
    br_rijeci = {}

    try:
        with open(file, 'r') as file:
            for line in file:
                rijecs = line.split()
                for rijec in rijecs:
                    rijec = rijec.lower()
                    br_rijeci[rijec] = br_rijeci.get(rijec, 0) + 1

    except FileNotFoundError:
        print("Datoteka nije pronađena.")

    jedinstvene_rijeci = [rijec for rijec, count in br_rijeci.items() if count == 1]

    print(f"Broj riječi koje se pojavljuju samo jednom u datoteci: {len(jedinstvene_rijeci)}")
    print("Te riječi su:")
    for rijec in jedinstvene_rijeci:
        print(rijec)

if __name__ == "__main__":
    main()


