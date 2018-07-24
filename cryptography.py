alfabet = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
invoer = input("Typ een text hier in:  ")
new_invoer = invoer.lower()
getal = int(input("Typ een getal in:  "))
nieuw_woord = ""
lang = len(invoer)
x = 0
if getal <= 26: 
  while x < lang :
       letter = new_invoer[x]
       x += 1
       zoek = alfabet.find(letter)
       zoek += getal
       nieuw_woord = nieuw_woord + alfabet[zoek]

  print(nieuw_woord)
else: 
    print("Het alfabet heeft maar 26 letters, jouw waarde ligt buiten het bereik!!")