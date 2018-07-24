def DrawSmilley(diameter):

    import math
    center_x = diameter/2
    center_y = diameter/2
    smilley = ""
   

    for y in range(diameter+1):
        for x in range(diameter):
            distance = math.sqrt((center_x - x )**2 + (center_y - y)**2)
            distance = math.ceil(distance)

            if distance == diameter/2:
                smilley += "*"

            if y == round(diameter/5) and x == round(diameter/3): #linker wenkbrau
                smilley += "___"

            if y == round(diameter/5) and x == round(diameter*0.6): #rechter wenkbrau
                smilley += "___"

            if y == round(diameter/4) and x == round(diameter/3): #linker oog
                smilley += "(O)"

            if y == round(diameter/4) and x == round(diameter*0.6): #rechter oog
                smilley += "(O)"

            if y == round(diameter/2) and x == round(diameter/2): #neus
                smilley += "^^"

            if y == round(diameter * 0.7) and x == round(diameter/4): #linker mondhoek
                    smilley += "("

            if y == round(diameter * 0.7) and x == round(diameter * 0.73): #rechter mondhoek
                   smilley += ")"


            if y == round(diameter*0.7) and round(diameter/4) <= x <= round(diameter * 0.7): #mond
                smilley += "_"

            else: 
                smilley += " "

        smilley += "\n"
 
    return smilley


invoer = int(input("Type in any number to draw a rather ugly smilley face:   "))
print(DrawSmilley(invoer))