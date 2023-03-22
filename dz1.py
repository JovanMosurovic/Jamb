seed = 191
praveSacuvane = []

def bbs():
    global seed
    p = 619
    q = 373
    M = p * q
    seed += 1
    x = seed
    kockice = []
    for i in range(5):
        x = (x * x) % M
        bit = x % 2
        x //= 2
        if bit == 0:
            kockice.append(int((x % 6) + 1))
        else:
            kockice.append(int((x + q) % 6 + 1))
    return kockice

# TALONI

def ispisPraznogTalona():
    for i in range(11):
        for j in range(3):
            if (j == 0):
                if (i < 6):
                    print("  {:2d}   |".format(i + 1), end="")
                elif (i == 6):
                    print(" KENTA |", end="")
                elif (i == 7):
                    print("  FUL  |", end="")
                elif (i == 8):
                    print(" POKER |", end="")
                elif (i == 9):
                    print(" JAMB  |", end="")
                elif (i == 10):
                    print("   ∑   |", end="")
            print("{:3d}  |".format(0), end="")
        print("\n" + "-" * 26)

def ispisMatrice():
    global matrica
    sumaNaDole = 0
    sumaNaGore = 0
    sumaRucna = 0
    for i in range(10):
        sumaNaDole += matrica[i][0]
        sumaNaGore += matrica[i][1]
        sumaRucna += matrica[i][2]
        for j in range(3):
            if (j == 0):
                if (i < 6):
                    print("  {:2d}   |".format(i + 1), end="")
                elif (i == 6):
                    print(" KENTA |", end="")
                elif (i == 7):
                    print("  FUL  |", end="")
                elif (i == 8):
                    print(" POKER |", end="")
                elif (i == 9):
                    print(" JAMB  |", end="")
                elif (i == 10):
                    print("   ∑   |", end="")
            print("{:3d}  |".format(matrica[i][j]), end="")
        print("\n" + "-" * 26)
    print("   ∑   |", end="")
    matrica[10][0] = sumaNaDole
    matrica[10][1] = sumaNaGore
    matrica[10][2] = sumaRucna
    for k in range(3):
        print("{:3d}  |".format(matrica[10][k]), end="")
    print("")
# KONVERZIJE

# def retkaUPravu2(vektor_R, vektor_V, vektor_C):
#     pravaMatrica = []
#     for i in range(len(vektor_R)):
#         red = []
#         for j in range(len(vektor_C)):
#             if vektor_R[i] == vektor_V[j]:
#                 red.append(vektor_C[j])
#             else:
#                 red.append(0)
#         pravaMatrica.append(red)
#     return pravaMatrica

def retkaUPravu(vektor_R, vektor_V, vektor_C):
    indeksi = {v: i for i, v in enumerate(vektor_V)}
    pravaMatrica = []
    for i in vektor_R:
        red = [0] * len(vektor_V)
        if i in indeksi:
            red[indeksi[i]] = vektor_C[indeksi[i]]
        pravaMatrica.append(red)
    return pravaMatrica


# UPISI

matrica = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0],
           [0, 0, 0],
           [0, 0, 0],
           [0, 0, 0],
           [0, 0, 0],
           [0, 0, 0],
           [0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]
brojacNaDole = 0
brojacNaGore = 9
brojUpisaRucne = 0
brojUpisaBezRucne = 0
brojacZaBacanja = 1

def sumaUpisa(kockice, index):
    global brojacZaBacanja
    suma = 0
    i = 0
    if(index < 6):
        while (i < len(kockice)):
            if (kockice[i] == index + 1):
                suma += (index + 1)
            i += 1
    elif (index == 6 and kenta(kockice)):
        if(brojacZaBacanja == 1): suma = 66
        if(brojacZaBacanja == 2): suma = 56
        if(brojacZaBacanja == 3): suma = 46
    elif(index == 7 and ful(kockice)):
        suma = 30 + sum(kockice)
    elif (index == 8 and poker(kockice)):
        suma = 40 + sum(kockice)
    elif (index == 9 and jamb(kockice)):
        suma = 50 + sum(kockice)
    return suma


def upisNaDole(kockice):
    global brojacNaDole
    if(brojacNaDole <= 10):
        vrednost = sumaUpisa(kockice, brojacNaDole)
        matrica[brojacNaDole][0] = vrednost
        brojacNaDole += 1
        ispisMatrice()
    else: print("Ne mozete vise da upisujete na dole!")
    return vrednost


def upisNaGore(kockice):
    global brojacNaGore
    vrednost = sumaUpisa(kockice, brojacNaGore)
    if(brojacNaGore >= 0):
        matrica[brojacNaGore][1] = vrednost
        brojacNaGore -= 1
        ispisMatrice()
    else:
        print("Ne mozete vise da upisujete na gore!")
    return vrednost


def upis():
    global brojUpisaBezRucne
    global kockice
    global praveSacuvane
    ok = True
    print("Izaberite da li zelite na gore ili na dole da upisete vrednost:")
    print("╭───────────────────────────────────╮")
    print("│               MENI                │")
    print("├───────────────────────────────────┤")
    print("│  1. Na dole                       │")
    print("├───────────────────────────────────┤")
    print("│  2. Na gore                       │")
    print("╰───────────────────────────────────╯")
    opcija = input().split()
    while (ok):
        if (len(opcija) == 1):
            if (opcija[0] == '1'):
                if(brojacNaDole < 10):
                    x = kockice[:]
                    x.extend(praveSacuvane)
                    upisNaDole(x)
                    brojUpisaBezRucne += 1
                    kockice = bbs()
                else:
                    print("Popunili ste kolonu na dole. Probajte nesto drugo.")
                ok = False
            elif (opcija[0] == '2'):
                if(brojacNaGore >= 0):
                    x = kockice[:]
                    x.extend(praveSacuvane)
                    upisNaGore(x)
                    brojUpisaBezRucne += 1
                    kockice = bbs()
                else: print("Popunili ste kolonu na gore. Probajte nesto drugo.")
                ok = False
            else:
                print("Uneli ste nepostojecu opciju. Pokusajte ponovo:")
                opcija = input().split()
        else:
            print("Uneli ste nepostojecu opciju. Pokusajte ponovo:")
            opcija = input().split()


def upisUPoljeRucna(index):
    suma = sumaUpisa(kockice, index)
    for i in range(10):
        if(i == index):
            matrica[i][2] = suma

def rucnaUpis(index):
    global brojUpisaRucne
    if(index >= 1 and index <= 6):
        upisUPoljeRucna(index-1)
    elif(index == 7):
            upisUPoljeRucna(index-1)
    elif (index == 8):
        if (ful(kockice)):
            upisUPoljeRucna(index-1)
    elif (index == 9):
            upisUPoljeRucna(index-1)
    elif (index == 10):
            upisUPoljeRucna(index-1)
    brojUpisaRucne += 1
    ispisMatrice()


# KOCKICE

kockice = bbs()
nove = []
sacuvane = []

def lista_podliste(manjaLista, vecaLista):
    if(len(vecaLista) == 0): return False
    x = vecaLista[:]
    for i in range(len(manjaLista)):
        try:
            x.remove(manjaLista[i])
        except Exception:
            return False
    return True

def ponovnoBacanjeKockica():
    ok = True
    global kockice
    print("Izaberite koje kockice cuvate: ")
    str_sacuvane = input().split()
    sacuvane = []
    for i in range(len(str_sacuvane)):
        sacuvane.append(int(str_sacuvane[i]))
    if(len(praveSacuvane) + len(sacuvane) <= 5):
        while (ok):
            if not lista_podliste(sacuvane, kockice):
                while(True):
                    print("Izabrali ste nepostojece kockice. Pokusajte ponovo:")
                    sacuvane = [int(i) for i in input().split()]
                    if (lista_podliste(sacuvane,kockice)): break
            else:
                ok = False
    else:
        sacuvane = []
        print("Imate previse sacuvanih kockica.")
    nove = []
    for i in range(5 - len(sacuvane) - len(praveSacuvane)):
        nove.append(bbs()[0])
    kockice = nove
    return nove, sacuvane


# DRUGA POLJA

def kenta(kockice):
    kockice1 = sorted(kockice)
    if (kockice1 == [1, 2, 3, 4, 5] or kockice1 == [2, 3, 4, 5, 6]):
        return True
    return False


def ful(kockice):
    kockice1 = sorted(kockice)
    if (kockice1[0] == kockice1[1] == kockice1[2] and kockice1[3] == kockice1[4]):
        return True
    elif (kockice1[0] == kockice1[1] and kockice1[2] == kockice1[3] == kockice1[4]):
        return True
    return False


def poker(kockice):
    kockice1 = sorted(kockice)
    for i in kockice1:
        if (kockice1.count(i) == 4 or kockice1.count(i) == 5):
            return True
    return False


def jamb(kockice):
    i = 0
    while (i < len(kockice) - 1):
        if (kockice[i] != kockice[i + 1]):
            return False
        i += 1
    return True

def pomocPrijatelja():
    global kockice
    if(brojacZaBacanja == 1):
        ok = True
        x = 5
        while not(0 <= x <= 2):
            x = bbs()[0]
        while(ok):
            if(x == 1 and brojacNaGore >= 0):
                z = upisNaGore(kockice)
                print("\nUpisano je", z, "na gore")
                ok = False
            elif(x == 0 and brojacNaDole < 10):
                y = upisNaDole(kockice)
                print("\nUpisano je", y, "na dole")
                ok = False
            else:
                z = bbs()[1]+bbs()[2]
                while(z > 0 and z < 11):
                    if(matrica[z-1][2] == 0):
                        rucnaUpis(z)
                        ok = False
                        print("\nUpisana rucna u red", z)
                        break
                    z = bbs()[3]+bbs()[4]
            x = 5
            while not (0 <= x <= 2):
                x = bbs()[0]
        kockice = bbs()
    else: print("Pomoc prijatelja radi samo ceo potez")


def zavrsetakIgre():
    if((brojUpisaRucne == 10 and brojacNaGore == -1 and brojacNaDole == 10)):
        print("╭─────────────────────────────────╮")
        print("│  Cestitamo! Zavrsili ste igru!  │")
        print("╰─────────────────────────────────╯")
        izlazakIzIgre()

def izlazakIzIgre():
    print("╭───────────────────────────────╮")
    print("│     Zavrsili ste partiju.     │")
    print("╰───────────────────────────────╯")
    quit()


def pocetniMeni():
    global kockice
    global praveSacuvane
    global nove
    global sacuvane
    global brojacZaBacanja
    global brojUpisaRucne
    bool = True
    kockice = bbs()

    print("╭───────────────────────────────────╮")
    print("│               MENI                │")
    print("├───────────────────────────────────┤")
    print("│  0. Izadji                        │")
    print("├───────────────────────────────────┤")
    print("│  1. Stvaranje praznog talona za   │")
    print("│     partiju i bacanje kockica     │")
    print("╰───────────────────────────────────╯")

    redni_br = input()

    if redni_br == "0":
        izlazakIzIgre()
    elif redni_br == "1":
        ispisPraznogTalona()

        while bool:
            zavrsetakIgre()
            print("╭───────────────────────────────╮")
            print("│              MENI             │")
            print("├───────────────────────────────┤")
            print("│  0. Izadji                    │")
            print("├───────────────────────────────┤")
            print("│  1. Izaberi koje kockice cuvas│")
            print("│     i ponovo baci kockice     │")
            print("├───────────────────────────────┤")
            print("│  2. Upisivanje                │")
            print("├───────────────────────────────┤")
            print("│  3. Upisivanje u kolonu rucna │")
            print("├───────────────────────────────┤")
            print("│  4. Odabir opcije pomoc       │")
            print("│    prijatelja za odigravanje  │")
            print("│    sledećeg poteza            │")
            print("╰───────────────────────────────╯")
            if(brojacZaBacanja == 1):
                print("Kockice:", *kockice)
            redni_br = input()

            if redni_br == "0":
                izlazakIzIgre()
                bool = False

            elif redni_br == "1":
                if (brojacZaBacanja <= 3):
                    nove, sacuvane = ponovnoBacanjeKockica()
                    praveSacuvane.extend(sacuvane)
                    x = nove[:]
                    x.extend(praveSacuvane)
                    if(len(nove) == 0):
                        print("Nemate vise novih kockica")
                    print("Nove kockice:", *nove)
                    print("Sacuvane kockice:", *praveSacuvane)
                    if (brojacZaBacanja == 1):
                        print("Imate jos {} preostala bacanja".format(3 - brojacZaBacanja))
                    elif (brojacZaBacanja == 2):
                        print("Imate jos 1 preostalo bacanje")
                    else:
                        print("Nemate vise preostalih bacanja")
                    brojacZaBacanja += 1
                else:
                    print("Ne mozete vise da bacate kockice, probajte drugu opciju")
                nove = []
                sacuvane = []
            elif redni_br == "2":
                if (brojUpisaBezRucne < 20):
                    upis()
                    brojacZaBacanja = 1
                    praveSacuvane = []
                    if(brojacNaDole < 10 and brojacNaGore >= 0):
                        kockice = bbs()
                else:
                    print("Ne mozete vise da unosite brojeve u ovu kolonu")
                    continue
            elif redni_br == "3":
                print("Unesite na koji index zelite da unesete vrednost:")
                index = int(input())
                if(index > 0 and index < 11):
                    if(brojUpisaRucne < 10 and matrica[index-1][2] == 0 and brojacZaBacanja == 1):
                        rucnaUpis(index)
                        kockice = bbs()
                        brojacZaBacanja = 1
                    else: print("Ne mozete upisivati u ovo polje.")
                else: print("Uneli ste nepostojeci index. Pokusajte ponovo")
            elif redni_br == "4":
                pomocPrijatelja()
            else:
                print("Ova opcija ne postoji u meniju. Pokusajte ponovo")

# ispisPraznogTalona()
pocetniMeni()
