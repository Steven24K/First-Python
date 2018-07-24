def DrawCircle(diameter):
 import math

 center_x = diameter/2
 center_y = diameter/2
 circle = ""

 for y in range(int(diameter+1)):
       for x in range(int(diameter+1)):
               distance = math.sqrt((center_x - x )**2 + (center_y - y)**2)
               distance = math.ceil(distance)

               if distance <= diameter/2:
                      circle += "*"
               else: 
                    circle += "#"
       circle += "\n"


 return circle

x = int(input("Grote van de cirkel:  "))

print(DrawCircle(x))




    
        








