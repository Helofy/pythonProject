nb=int(input('entrez un nombre entier : '))
if nb == 0:
    print( 'Le nombre est zéro ( et il est pair)')
else:
    if nb %2 == 0 :
        type = 'pair'
    else:
        type = 'impair'
    if nb > 0 :
        genre = 'positif'
    else :
        genre='négatif'

    print(' Le nombre est ',genre,' et ', type)