Base = 4
fromage = 800.00
eau = 2
ail= 2
pain = 400.00
NbCon= int(input("entrez le nombre de convives : "))

nfromage = fromage * NbCon / Base
neau= eau *NbCon / Base
nail= ail*NbCon / Base
npain= pain * NbCon / Base
print( 'Pour',NbCon, " convives il vous faudras : ")
print ('-', nfromage,' g de fromage')
print('-', neau , " dl d'eau ")
print ('-', nail," gousse(s) d'ail")
print('-',npain, ' g de pain' )