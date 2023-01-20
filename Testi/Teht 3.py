#Tehtävä 3

Sukupuoli = str.lower(input("Anna henkilön sukupuoli:"))
Hemoglobiini = float(input("Anna henkilön hemoglobiiniarvo:"))

Hemoglobiiniarvot = {
    "mies":range(134,195),
    "nainen":range(117,175)
}

if Hemoglobiiniarvot[Sukupuoli]:
    ArvoPrint = "Henkilön hemoglobiini arvo on"

    if Hemoglobiini in Hemoglobiiniarvot[Sukupuoli]:
        print(ArvoPrint, "normaali.")
    elif Hemoglobiini > max(Hemoglobiiniarvot[Sukupuoli]):
        print(ArvoPrint, "liiaan korkea!")
    elif Hemoglobiini < min(Hemoglobiiniarvot[Sukupuoli]):
        print(ArvoPrint, "liian alhainen!")
else:
    print("Virheellinen sukupuoli!")