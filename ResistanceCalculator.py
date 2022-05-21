minTiefe = 2            # How many recursions to do at least
tolleranzbereich = 1    # Maximum tollerance in %

# Resistors available
widerstande1 = [10000000,4700000,3300000,2700000,1000000,
                680000,560000,470000,390000,330000,270000,
                220000,180000,150000,130000,100000,68000,
                56000,47000,39000,33000,22000,12000,10000,
                8200,6800,5600,4700,3900,3600,3000,2200,
                1800,7.3,47,39,22,10,1,220,150,130,100,
                75,68,1300,1000,680,470,360]

# Common resistors
# widerstande1 = [360,1000,10000,100000,1000000]

# Custom resistors
# widerstande1 = [1000,10000,333000]

def formatiereFloat(wert):
    if int(wert) < 1000:
        return str(wert)
    temp = list(str(wert).split(".")[0])
    temp.reverse()
    outputString = []
    for n,i in enumerate(temp[:-1]):
        outputString += i
        if (n + 1) % 3 == 0:
            outputString += ["'"]
    outputString += [temp[-1]]
    outputString.reverse()
    if "." in str(wert):
        return ("".join(outputString) + "." + str(wert).split(".")[-1]).replace("'000'000.0"," M").replace("'000.0"," K")# + " Ω"
    temp = "".join(outputString)

    return temp.replace("'000'000"," M").replace("'000"," K")# + " Ω"


while True:
    rausgesucht = [] # Dopplearray: [Wert,Beschreibungsstring,Tiefe]
    eingabe = input("Desired resistance (M = 000000, K = 000, e.g. 2K = 2000): ").upper().replace(",",".")
    gesucht = float(eingabe.replace("M","000000").replace("K","000").replace(" ","")) # Welcher Wert gesucht ist
    print("Searching: " + formatiereFloat(gesucht))

    tolleranz = max(gesucht * tolleranzbereich * 0.01,1)

    def kombi(aktuellerWert,kombiString = "",tiefe = 0):
        global rausgesucht

        if tiefe == minTiefe:
            return

        if aktuellerWert > gesucht * 1000 or gesucht > aktuellerWert * 1000:
            return

        if abs(gesucht - aktuellerWert) < tolleranz:
            rausgesucht.append([aktuellerWert,kombiString,tiefe])

        for i in widerstande1:
            if aktuellerWert > 1000 * i or i > 1000 * aktuellerWert:
                continue

            kombi(aktuellerWert + i, kombiString + " + " + str(i), tiefe + 1)
            kombi((aktuellerWert * i) / (aktuellerWert + i), kombiString + " || " + str(i), tiefe + 1)

    while True:
        for n,i in enumerate(widerstande1):
            print(".",end="")
            kombi(i,str(i))

        if len(rausgesucht) > 0:
            break

        print()
        minTiefe += 1

    for i in range(minTiefe):
        print("\n----- Resistor Count: " + str(i + 1) + " -----")
        abschnitt = [k for k in rausgesucht if i == k[2]]
        print("Hits:", len(abschnitt))
        abschnitt.sort(key = lambda x : abs(gesucht - x[0]))
        for k in abschnitt[:10]:
            print(formatiereFloat(round(k[0],2)),"\t-> ",end="")
            for l in k[1].split(" "):
                try:
                    float(l)
                    print(formatiereFloat(l),end="")
                except ValueError:
                    print("\t" + l + "\t",end="")
            print()



