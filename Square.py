afmeting = int(input("Voer een willekeurig getal hier in:  "))
vierkant = ""
x = 0
y = 0
while (x < afmeting):
    y = 0
    while (y < afmeting):
        vierkant += "*"
        y += 1
    vierkant += "\n"
    x += 1
  

print(vierkant)  
    

