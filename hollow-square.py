def teken_vierkant_met_gat(afmeting):

 
 vierkant = ""
 spatie = "  "
 enter = "\n"
 ster = "*"

 for i in range(afmeting): 
     if i == 0 or i == afmeting - 1:
         for i in range(0, afmeting):
             vierkant = vierkant + ster
         vierkant = vierkant + enter
     else:
         vierkant = vierkant + ster
         for i in range(1, round(afmeting/2)):
             vierkant = vierkant + spatie
         vierkant = vierkant + ster
         vierkant = vierkant + enter
 return vierkant


x = int(input("Vul een getal in:  "))
print(teken_vierkant_met_gat(x))  



    
