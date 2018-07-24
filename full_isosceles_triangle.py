hoogte = int(input("Type any number here, you can do it:  "))
piramide = ""
x = 0

while (x < hoogte):
    spatie = hoogte - x
    x = x + 1

    y = 0
    while (y < spatie):
        piramide = piramide + " "
        y = y + 1

    aantal = 2 * x - 1
    while (aantal > 0):
        piramide = piramide + "*"
        aantal = aantal - 1
    piramide = piramide + "\n"
    
print(piramide)

    
    
    
