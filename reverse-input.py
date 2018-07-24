text = input("text here:  ")
lengte_text = len(text) - 1
new_text = ""
while (lengte_text >= 0):
    new_text = new_text + text[lengte_text]
    lengte_text = lengte_text - 1
   
print(new_text)
 


