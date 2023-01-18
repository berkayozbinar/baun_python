def topla(*toplanacak, fazladan = 0):
    toplam = 0

    for deger in toplanacak:
        toplam += deger + fazladan
    return toplam

print(topla(3, 20, 4, 70, fazladan = 5))