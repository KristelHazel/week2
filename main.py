""" kirjutame programmi, mis küsib kasutajalt, mis päev homme on (tööpäev või puhkepäev) ja väljastab vastuse põhjal sobiva sona
KAsutaja sisestab ühe sõna:
"tööpäev"
või "puhkepäev" """

""" Kui sisestus on "tööpäev", siis väljastame sõnumi: "Ma lähen magama, head ööd!"
Kui sisestus on "puhkepäev", siis väljastame sõnumi: "Veel üks osa Netflixist
 """
#Alusta programmi.
#Küsi kasutajalt: "Mis päev homme on?" (tööpäev/puhkepäev)
#Salvesta vastus muutujasse day.
#kui day on "tööpäev", siis väljastame sõnumi: "Ma lähen magama, head ööd!"
#kui day on "puhkepäev", siis väljastame sõnumi: "Veel üks osa Netflixist"
#Muidu ( kui sisestus ei olnud õige), siis väljastame sõnumi: "Vale väärtus.
#Lõpeta programm.

""" day=input("Mis päev homme on? (tööpäev/puhkepäev): ")

if day=="tööpäev":
    print("Ma lähen magama, head ööd!")
elif day=="puhkepäev":
    print("Veel üks osa Netflixist")
else:
    print("Vale väärtus.") """


#Finantsnõustaja
""" Sa tahad osta endale uue IPhone 17 pro aga sa oled otsustanud, et krediiti sa ei võta. Selle asemel oled sa palganud range ja vastutustundliku finantsnõustaja programmi kujul.
See programm:
küsib kui palju raha sul on
võrdleb seda IPhone 17 pro hinnaga (näiteks 2500 €)

ja annab sulle täiesti ratsionaalse, emotsionaalse soovituse. """

""" print("Tere tulemast programmi ´Finantsnõustaja´")
print("Sinu isiklik nõustaja ei tee emotsionaalseid oste.")

money = int(input("Kui palju raha sul on? "))

if money < 2500:
    print("Kahjuks sul ei ole piisavalt raha. Ole kannatlik ja kogu edasi!")
elif money == 2500:
    print("Palju õnne, saad osta uue Iphone 17 Pro sularahas!")
else:
    print("Saad osta uue iPhone 17 Pro ja raha jääb ülegi.") """

#Sammulugeja
""" Sul on eesmärk teha iga päev vähemalt 10 000 sammu. Programm küsib kasutajalt, mitu sammu ta on juba teinud, arvutab täitmise protsendi ja annab tagasisidet.
- Kui protsent on < 50: "Alles poolel teel, liigu edasi!"
- Kui protsent on < 75: "Tubli, oled peaaegu kohal!"
- Kui protsent >= 100: "Palju õnne, oled täitnud oma eesmärgi!" """

goal = 10000
steps = int(input("Mitu sammu oled juba täna teinud? "))

percentage = (steps / goal) * 100

print(f"Oled täitnud oma eesmärgi {percentage:.2f}% ulatuses.")

if percentage < 50:
    print("Alles poolel teel, liigu edasi!")
elif percentage < 75:
    print("Tubli, oled peaaegu kohal!")
elif percentage < 100:
    print("Suurepärane, oled peaegu kohal!")    
else:
    print("Palju õnne, oled täitnud oma eesmärgi!") 
