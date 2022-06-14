año = int(input("Introduzca un año:"))
k=int(str(año)[-2:][0])
s=int(str(año)[-1:])
if (k%2!=0 and s==2 or s==6) or (k%2==0 and s==0 or s==4 or s==8):
    print(f'{año} es un año bisiesto')
else:
        print(f'Lo siento, {año} no es un año bisiesto')