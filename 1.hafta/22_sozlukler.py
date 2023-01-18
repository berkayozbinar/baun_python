sozluk = {"marka":"Toyota", "model":"Supra", "yil":1994}

print(sozluk)
print(sozluk["marka"])
print(sozluk["model"])
print(sozluk["yil"])

sozluk["renk"] = "turuncu"
print(sozluk)
print(sozluk["renk"])

print(sozluk.keys())
print(sozluk.values())
print(sozluk.items())

for i in sozluk.keys():
    print(i, ":", sozluk[i])