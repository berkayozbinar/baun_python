"""
1- veri isimli bir klasör oluşturun
2- zip dosyasını veri klasörüne çıkartın
3- zip dosyası içindeki csv dosyalarının tüm içeriğini tek bir csv dosyasında birleştirin  (volume olmasın)
4- bu kayıtların tamamını sqlite veritabanına bir tablo oluşturarak yükleyin
5- kullanıcının belirlediği paritenin
   kullanıcının belirlediği araligin
   kullanıcının belirlediği degerin
   grafiğini çizdirin (verileri sqlite'dan çekiniz)
"""
import os, zipfile, pandas, sqlite3, matplotlib.pyplot as plt

con = sqlite3.connect("veri.db")
cursor = con.cursor()

if not os.path.isdir("veri"):
    os.mkdir("veri")
    with zipfile.ZipFile("pariteler_cikti_1hour_2022_2022.zip", 'r') as zip_ref:
        zip_ref.extractall("veri")

    all_files = os.listdir("veri")
    pandas_csv_list = []

    for csv_file in all_files:
        data = pandas.read_csv("veri/" + csv_file)
        del data["volume"]
        data["parite"] = csv_file.split("_")[0]
        pandas_csv_list.append(data)

    final_csv = pandas.concat(pandas_csv_list)
    final_csv.to_csv("hepsi.csv", index = False)

    cursor.execute("CREATE TABLE IF NOT EXISTS pariteler(id INTEGER PRIMARY KEY AUTOINCREMENT, parite TEXT, otime DATETIME, open FLOAT, high FLOAT, low FLOAT, close FLOAT)")
    con.commit()

    all_data = pandas.read_csv("hepsi.csv")

    for row in all_data.itertuples():
        cursor.execute("INSERT INTO pariteler(parite, otime, open, high, low, close)"
                        + "VALUES("
                        + "'"+row.parite+"',"
                        + "'"+row.otime+"',"
                        + ""+str(row.open)+","
                        + ""+str(row.high)+","
                        + ""+str(row.low)+","
                        + ""+str(row.close)+")")

parite = input("Parite Giriniz :")
start_date = input("Başlangıç Tarihi :")
end_date = input("Bitiş Tarihi :")

cursor.execute("SELECT * FROM pariteler WHERE (otime BETWEEN '"+start_date+"' AND '"+end_date+"') AND parite = '"+parite+"'")
result = cursor.fetchall()

print(result)

listx = []
listy = []
for candle in result:
    listy.append(candle[6])
    listx.append(candle[2])

plt.plot(listx, listy)
plt.show()

con.close()