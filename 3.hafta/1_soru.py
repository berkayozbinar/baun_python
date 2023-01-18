# kendisine gönderilen sayılardan, sadece palindrom olanları toplayan ve diğerlerini de bu toplamdan çıkartıp geri döndüren
# fonksiyonu yazınız. palidrom = ilk sayı ile son sayısı aynı olan

toplam = 0

def fonksiyon(*sayi):
    global toplam
    
    for i in sayi:
        if (str(i) == str(i)[::-1]):
            toplam += i
        else:
            toplam -= i

fonksiyon(55, 9009, 50, 101)

print(toplam)