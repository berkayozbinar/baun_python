def birimIslem(**birim):
    print("Birimin Tipi :",type(birim))
    print("Birim Adı :",birim["ad"])
    print("Birim Tipi :",birim["tip"])
    print("Birim Yılı :",birim["yil"])

birimIslem(ad="Balıkesir", tip="Üniversite", yil=1992)