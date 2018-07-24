x = True
while x == True: 
    f = input("Put your temperature in degrees Fahrenheit here, please:  ")
    c = (float(f)-32.00)/1.80
    print("The temperature in degrees Celcius is: ")
    print(round(c, ndigits = 2))
    
