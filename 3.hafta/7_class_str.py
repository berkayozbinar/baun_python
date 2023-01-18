class sinif:
    metin = ""

    def __init__(self, a):
        self.metin = a

    def __str__(self):
        return "Yazdırılan : " + self.metin

nesne = sinif("Metin")
print(nesne)

