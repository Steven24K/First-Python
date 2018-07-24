for i in range(100):
     k = input("Put your temperature in Kelvin here, please:  ")
     c = float(k) - 273.15
     if float(k) < 0:
         print("The Kelvin scale does not go below zero")
     else:
          print("The temperature in degrees Celcius is: ")
          print(round(c, ndigits = 2))