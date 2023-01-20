#Tehtävä 4

Vuosi = int(input("Anna vuosi:"))

if Vuosi % 4 == 0 and (Vuosi % 100 != 0 or Vuosi % 400 == 0):
    print(Vuosi, "on karkausvuosi!")
else:
    print(Vuosi, "ei ole karkausvuosi!")