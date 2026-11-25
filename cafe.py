print("welcome to Gorden coffee ")
drenk= input("what wude you want to drenk ( coffee or tea ) ??? ")

if drenk=="coffe" :
    sugar=input ( "do you want sugar or black ??? ")
   
    if sugar == "black":
       print ("  it will be ther after a few minutes ")
   
    elif sugar == 'sugar':
      print ("nice it will be ther after a few minutes ")

    else:
       print ('sorry can you tray agan')

elif drenk == "tea":
   tayp_tee = (input ('DO you wnt red tee or gren tea ?? '))

   if tayp_tee == 'red tea':
       print ("ok  it will be ther after a few minutes")

   elif tayp_tee == 'gren tea':
        print ("good choice it will be ther after a few minutes ")

   else:
      print (" sorry we can help you ")

else:
   print (" sorry we can help you ")