locationd= int(input('Donnez l’heure de début de la location (un entier) :'))
locationf= int(input('Donnez l’heure de début de la location (un entier) :'))
locat =locationf - locationd
temp1 = 0
temp2= 0
prix=0
for i in range (locat):
    if  0<=locationd+i<= 7  or  17<=locationd+i <=24:
        prix+= 1
        temp1 += 1
    else :
        temp2 += 1
        prix +=2
if temp1 == 0 :
    print('Vous avez loué votre vélo pendant :')
    print(temp2, "heure(s) au tarif horaire de 2.0 euro(s)")
    print('Le montant total à payer est de', prix, ' euro(s).')
elif temp2 == 0 :
    print('Vous avez loué votre vélo pendant :')
    print(temp1, "heure(s) au tarif horaire de 1.0 euro(s)")
    print('Le montant total à payer est de', prix, ' euro(s).')
else:
    print('Vous avez loué votre vélo pendant :')
    print(temp1, "heure(s) au tarif horaire de 1.0 euro(s)")
    print(temp2, "heure(s) au tarif horaire de 2.0 euro(s)")
    print('Le montant total à payer est de',prix ,' euro(s).')