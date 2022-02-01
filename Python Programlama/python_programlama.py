#SAYILAR VE STRINGLERE GİRİŞ
9
9.2
9+9
9*9

type(9)
type(9.2)
type("Hello AI ERA")

#Stringlere yakından bakalım
"a" + "b"
"a" "b"
"a"*3
"yigit"*5

#String Metodları - Len

gel_yaz = "gelecegi_yazanlar"s

a = 9
b = 10

a*b

len(gel_yaz)

#STRING METODLARI - upper() ve lower()

gel_yaz.upper() #büyük harfle yazar
gel_yaz.lower() #küçük harflerle yazar

gel_yaz.islower()
gel_yaz.isupper()


#Karakter değiştirme - replace()

gel_yaz = "gelecegi_yazanlar"
gel_yaz.replace("e", "a")
gel_yaz.replace("a", "i")

#STRING METODLARI - strip() - Kırpma işlemi
gel_yaz = "*gelecegi_yazanlar*"
gel_yaz.strip("*")

gel_yaz = "?gelecegi_yazanlar?"
gel_yaz.strip("?")

#METODLARA GENEL BAKIŞ
gel_yaz = "gelecegi_yazanlar"

dir(gel_yaz)
gel_yaz.islower()
gel_yaz.isupper()

# İlk harfleri büyütmek için kullanılan bir metod
gel_yaz.capitalize()
#Her kelimenin ilk harfini büyütür
gel_yaz.title()

#SUBSTRINGLER

gel_yaz = "gelecegi_yazanlar"

gel_yaz[0]
gel_yaz[0:3] # 0 dan 3'e kadar =>3.index alınmaz 0,1,2 indekseler alınır
gel_yaz[2:7]


#DEĞİŞKENLER

a = 99999
b = "yigit_uzaya_git"
c = a * 5
print(c)
a/c

type(100)
type(100.2)
type(1+2j)

a = 100.2


#TYPE_DÖNÜŞÜMLERİ
#input() fonksiyonu kullanıcıdan bilgi almak için kullanılır

toplama_bir = input()
toplama_iki = input()
type(toplama_bir)
type(toplama_iki)

toplama_bir + toplama_iki
int(toplama_bir) + int(toplama_iki)
int(11.0) #int'a çevirme
float(12) #floata çevirme
str(9) #string'e çevirme
type(str(9))

#print()
# Argüman = Fonksiyonların genel amaçlarını biçimlendirmek için kullanılan 
#alt görev belirteclerine argüman denir. sep argümandır.

print("Hello AI Era")

print("gelecegi","yazanlar")
print("gelecegi","yazanlar", sep = '_')#_ile birleştirir

?print
"a"+"b"
"10"+2
"_Python".strip("_")
ifade = "Merhaba! "
ifade.strip("")
dir(type)

#VERİ YAPILARI
#Listeler
# --> Değiştirilebilirdir
#--> Kapsayıcıdır (Farklı türdeki verileri tutabilir)
#--> Sıralıdır (İndex işlemleri yapılabilir)
# [] --> liste oluşturma 1.yol
# list() --> liste oluşturma 2.yol

notlar = [90,80,70,50] 
type(notlar)

liste = ["a",19.5,90]
liste_genis = ["a",19.5,90,notlar]

len(liste_genis)

#Liste içi type sorgulama
type(liste[0])
liste[0]
type(liste[1])
type(liste[2])
type(liste_genis[3])

#Liste birlşeştirme
tum_liste = [liste, liste_genis]
tum_liste[0]
tum_liste[1]
#Liste silme 
# del tum_liste

#LİSTELER - ELEMAN İŞLEMLERİ

liste = [10,20,30,40,50]
liste[1]
liste[0:2] #0'dan 2'ye kadar
liste[2:] #2'den sona kadar
liste[:2] #bantan sona kadar

yeni_liste = ["a",10,[20,30,40,50]]
yeni_liste
yeni_liste[2]
#Listenin içindeki listenin elamanına erişmek
yeni_liste[2][1]

#LİSTELER - Eleman Değiştirme

liste = ["ali","veli","berkecan","zeynep"]
liste

liste[1] = "velinin_babasi"
liste
liste[0:3] = "alinin_basi","velinin_babasi","berkcanin_babasi"
liste

liste = liste + ["yigit"]
liste

#Liste içinden eleman silme
del liste[4]
liste

#LİSTELER - Liste Metoldarı

liste = ["ali","veli","isik"]
dir(liste)

#Liste metodal elaman ekleme
liste.append("berkacan")
liste
#Liste isme göre metodla elaman silme
liste.remove("berkacan")
liste

#insert - İndekse göre eleman ekleme 

liste = ["ali","veli","isik"]
liste

liste.insert(0, "zeynep")
liste

liste.insert(2, "abc")
liste

liste.insert(5,"berk")
liste

#listenin sonuna eleman ekle
liste.insert(len(liste), "umut")
liste

#pop - indekse göre elaman silme

liste.pop(6)
liste.pop(2)
liste

#DİĞER LİSTE ELEMANLARI
#count => aranan elemandan kaç tane var
liste = ["ali","veli","isik","ali","veli"]
liste.count("ali")
liste.count("veli")
liste.count("isik")

#copy => elemizdeki mevcut listelemek veya yedeklemek için kullanılır
liste_yedek = liste.copy()

#exten => iki listeyi birleştirmek için kullanılır
#Birleştirmek istediğimiz listenin adını yada yeni bir liste oluşturabiliriz
liste.extend(["a","b",10])
liste

#index => istenilen elemanın kaçıncı index'te olduğunu veririr
liste.index("ali")

#reverse => elemanları terse çevirir
liste.reverse()
liste

#sort => liste içindeki elemanları sıralar
liste_sort = [10,40,5,90]
liste_sort.sort()
liste_sort

#clear => listenin içini temizler
liste_sort.clear()

#VERİ YAPILARI - Tuple (Demet oluşturma)
# -> Kapsayıcıdır (Birbirinden farklı veri tiplerini barındırabilir)
# -> Sıralıdır
# -> Değiştirilemez 

t = ("ali","veli",1,2,3.2, [1,2,3,4])

t = "ali","veli",1,2,3.2, [1,2,3,4]
#tuple

# Tek elemanlı tuple oluşturacığımız zaman sonuna virgül koyulur.
t = ("eleman",)

t[1]
t[0:3]

# Hata verir tuple değişikliğe izin vermez
t[2] = 99

# VERİ YAPILARI - Dictionary ( Sözlük )
# -> Kapsayıcıdır
# -> Sırasızdır
# -> Değiştirilebilir

# Sırasız olduğu için key ile seçme işlemi yapılır indeks ile seçme yapılmaz

sozluk = {"REG" : "Regresyon Modeli", 
          "LOJ"  : "Lojistik Regresyon", 
          "CART" : "Classification and Reg"} 

len(sozluk)

sozluk1 = {"REG" : 10, 
          "LOJ"  : 20, 
          "CART" : 30}

sozluk1

sozluk = {"REG" : ["RMSE",10], 
          "LOJ"  : ["MSE",20], 
          "CART" : ["SSE", 30] }

sozluk["REG"]
sozluk["LOJ"]
sozluk["CART"]


sozluk

sozluk = {"REG" : {"RMSE" : 10, 
                   "MSE" : 20, 
                   "SSE" : 30},
          
          "LOJ"  : {"RMSE" : 10, 
                   "MSE" : 20, 
                   "SSE" : 30}, 
          
          "CART" : {"RMSE" : 10, 
                   "MSE" : 20, 
                   "SSE" : 30} }

sozluk
sozluk["REG"]["SSE"]
sozluk["LOJ"]["MSE"]

#Sozluk Eleman Ekleme & De

sozluk = {"REG" : "Regresyon Modeli", 
          "LOJ"  : "Lojistik Regresyon", 
          "CART" : "Classification and Reg"} 


sozluk["GBM"] = "Gradient Boosting Mac"
sozluk

sozluk["REG"] = "Çoklu Doğrusal Regresyon"
sozluk

sozluk[1] = "Yapay Sinir Ağları"
sozluk

l = [1]

# Sözlüklerde key değerleri ancak sabit değerlerle oluşturulabilir, listeler
#değiştirilebilir olduğu için onları key olarak atayamayız.
# tupple 'lar değiştirilemez olduğu için bu yüzden tupple kullanabiliriz.
sozluk[l] = "yeni bir sey"

t = ("tuple",)

sozluk[t] = "yeni bir sey"
sozluk


# SET'LER (KÜMELER)
# -> Kapsayıcıdır
# -> Değiştirilebilir
# -> Sırasızdır, yani indeks yok
# -> Değerleri eşsizdir, UNİC

s = set()

liste = [1,"a","ali",123]
s = set(liste)

t = ("a","ali")
s = set(t)
s

ali = "lutfen_ata_bakma_uzaya_git"

s = set(ali)
s


liste = ["ali","lutfen","ata","bakma","uzaya","git","git","ali","git"]
liste
s = set(liste)
s
len(s)

liste[0]
s[0]

# SET' lerde Ekleme & Çıkarma
#Ekleme -> add
#Silme -> remove

l = ["gelecegi","yazanlar"]

s = set(l)
s

dir(s)

s.add("ali")
s
s.add("gelecege_git")
s

s.add("ali") # Var olduğu için eklemez
s

s.remove("ali")
s
s.remove("ali")

s.discard("ali")


# SET' ler Klasik Küme İşlemleri
# =============================================================================
# difference() ile iki kümenin farkını yada "-" ifadesi 
# intersection() iki kümenin kesişimi yada "&" ifadesi
# union() iki kümenin birleşimi 
# symmetric_difference() ikisinde de olmayanlari
# =============================================================================

set1 = set([1,3,5])
set2 = set([1,2,3])

# difference()

# set1'de olup set2 de olmayanları verir
set1.difference(set2)

# set2'de olup set1 de olmayanları verir
set2.difference(set1)

# iki kğmedede olmayanlar
set1.symmetric_difference(set2)

set1 - set2
set2 - set1

# intersection & union

set1 = set([1,3,5])
set2 = set([1,2,3])

set1.intersection(set2)
set2.intersection(set1)

kesisim = set1 & set2
kesisim

# union()
birlesim = set1.union(set2)
birlesim

set1.intersection_update(set2)
set1


# SET Sorgu İşlemleri

set1 = set([7,8,9])
set2 = set([5,6,7,8,9,10])

#İki kümenin kesişiminin  boş olup olmadığını kontrol etme
set1.isdisjoint(set2) #false
set2.isdisjoint(set1)

# Bir kümenin bütün elemanlarının baka bir küme içinde yer alıp almadığı
set1.issubset(set2) #true
set2.issubset(set1) #false

#Bir kümenin diğer kümeyi kapsayıp kapsamadığına bakar
set2.issuperset(set1) #true
set1.issuperset(set2) #false


# FONKSYİONLARA GİRİŞ VE FONKSİYON OKURYAZARLIĞI

print()
print

print()
len("a")

#Matematiksel İşlemler
3**2 #-> üs alma
3**3

# FONKSİYON NASIL YAZILIR

def kare_al(x):
    print(x**2)
    
kare_al(5)
#------------------------------#
#Bilgi notula çıktı üretme
#------------------------------#
def kare_al(x):
    print("Girilen sayının karesi : " + str(x**2))
    #str koymamızın sebebi stringler sadece string ile birleştirilir.
    
kare_al(5)
#------------------------------#

def kare_al(x):
    print("Girirlen sayı : " + str(x) + ", Karesi : " + str(x**2));
    
kare_al(5)

#İki Argümanlı Fonksiyon Tanımlama

def carpma_yap(x, y):
    print(x*y)
    
carpma_yap(20, 5)

# Ön Tanımlı Argümanlar

def carpma_yap(x, y=1):
    print(x*y)
    
carpma_yap(3)

#Argümanların sıralaması
def carpma_yap(x, y=1):
    print(x*y)
    
carpma_yap(y=2, x =6)

   
# Ne zaman Fonksiyon yazılır?
#Tekrar eden olaryları tekrar tekrar yazmak yerine kullanılır
# Sık tekrar eden yada uzun işlemerden kurtulmak için yazılır

#isi, nem, sarj
(40 + 25) / 90

def direk_hesapla(isi, nem, sarj):
    print((isi + nem) / sarj)
    
direk_hesapla(30, 40, 70)


# Çıktıyı Giridi Olarak Kullanma

def direk_hesap(isi, nem, sarj):
    return (isi + nem) / sarj
    
cikti = direk_hesap(25, 40, 70)
cikti
print(cikti)

direk_hesap(25, 40, 70) * 9


#Local ve Global Değişkenler

#Global
x = 10
y = 10

#isi, nem, sarj LOCAL değişken
def direk_hesap(isi, nem, sarj):
    return (isi + nem) / sarj

#Local Etki Alanından Global Etki Alanına Değiştirmek

x = []

def eleman_ekle(y):
    x.append(y)
    print(str(y) + " ifadesi eklenedi")
    
eleman_ekle("yigit")
eleman_ekle(10.5)    
eleman_ekle(100)
x.pop(1)
x


# KARAR & KONTROL YAPILARI

sinir = 5000

sinir == 4000
sinir == 5000
5 == 4
5 == 5


#if

sinir = 50000
gelir = 40000

if gelir < sinir:
    print("Gelir sınır dan küçük")
elif gelir == sinir:
    print("Gelir sınıra eşit")
else:
    print("Gelir sınır dan büyük")
    
    ########
    
sinir = 50000
gelir1 = 60000
gelir2 = 50000
gelir3 = 35000

if gelir2 > sinir:
    print("Tebrikler, hediye kazandınız.")
    
elif gelir2 < sinir:
    print("Uyarı!")
    
else:
    print("Gelir sınıra eşit")


#mini uygulama

sinir = 50000
magaza_adi = input("Mağaza adı nedir? ")    
gelir = int(input("Gelirinizi Giriniz : "))

if gelir > sinir:
    print("Tebrikler, " + magaza_adi + " promosyon kazandınız.")
    
elif gelir < sinir:
    print("Uyarı! Çok düşük gelir : " + str(gelir))
    
else:
    print("Takibe devam")


#DONGÜLER - for

ogrenci = ["ali","veli","isik","berk"]

for i in ogrenci:
    print(i)
    
#for - devam

maaslar = [1000,2000,3000,4000,5000]

for maas in maaslar:
    print(maas)
    
# Programlama dilleri, insanların düşündüklerini,
# bilgisayarlara yaptıması
    

#döngü ve fonksiyonları birlikte kullanalım

def kare_al(x):
    print(x**2)
    
kare_al(2)

maaslar = [1000,2000,3000,4000,5000]
for i in maaslar:
    print(i)
    

#maaslara %20 zam yapılacak, gerekli kodları yazınız

maaslar[0] * 20 / 100 + maaslar[0]

#dongu yazılacak
#fonksiyon yaz

def yeni_maas(x):
    print(x*20/100 + x)
    
yeni_maas(1000)

for i in maaslar:
    yeni_maas(i)
    
#mini uygulama 
#if, for ve fonksiyonların birlikte kullanımı
# maası 3000'den az ise %20, fazla ise %10 zam

maaslar = [1000,2000,3000,4000,5000]

# =============================================================================
# def zam_yap(x):
#     if x < 3000:
#         print(x*20/100 + x)
#     else:
#         print(x*10/100 + x)
#         
# for i in maaslar:
#     zam_yap(i)
# =============================================================================

def maas_ust(x):
    print(x*10/100 + x)

def maas_alt(x):
    print(x*20/100 + x)
    
for i in maaslar:
    if i >= 3000:
        maas_ust(i)
    else:
        maas_alt(i)
        

#break & continue

maaslar = [8000,5000,2000,1000,3000,7000,1000]

dir(maaslar)
maaslar.sort()
maaslar    

for i in maaslar:
    if i == 3000:
        print("kesildi")
        break
    print(i)
    
for i in maaslar:
    if i == 3000:
        print("contione -> 3000 atla")
        continue
    print(i)


#while

sayi = 1

while sayi < 10:
    print(sayi)
    sayi+=1
    
def harf_say(x):
    return len(x)
    
harf_say("Merhaba!")



#NESNE YÖNELİMLİ PROGRAMLAMA

class VeriBilimci():
    print("Bu bir sınıftır")
    

#Sınıf Özellikleri (Class Attributes)

class VeriBilimci():
    bolum = ''
    sql = 'Evet'
    deneyim_yili = 0
    bildigi_diller = []
    

#Sınıfların özelliklerine erişmek
VeriBilimci.bolum
VeriBilimci.sql    

#Sınıfların özzelliklerini değiştirmek
#VeriBilimci.sql yapmak gerek VeriBilimci().sql dersek olmuyor
VeriBilimci.sql = 'hayir'
VeriBilimci.sql

VeriBilimci.sql = 'evet'
VeriBilimci.sql


#Sınıf Örneklendirmesi - (instantiation)

ali = VeriBilimci()

ali.sql
ali.deneyim_yili
ali.bolum
ali.bildigi_diller.append("Python")

ali.bildigi_diller


veli = VeriBilimci()
veli.sql
veli.bildigi_diller


#Örnek Özellikleri

class VeriBilimci():
    bildigi_diller = ["R","Python"]
    bolum = ''
    sql = ''
    deneyim_yili = 0
    def __init__(self):
        self.bildigi_diller = []
        self.bolum = ''
        
        
ali = VeriBilimci()
ali.bildigi_diller

veli = VeriBilimci()
veli.bildigi_diller

ali.bildigi_diller.append("Python")
ali.bildigi_diller
veli.bildigi_diller


veli.bildigi_diller.append("R")
veli.bildigi_diller
ali.bildigi_diller

VeriBilimci.bildigi_diller

ali.bolum
veli.bolum

VeriBilimci.bolum
ali.bolum = 'İstatistik'
ali.bolum
VeriBilimci.bolum
veli.bolum
veli.bolum = 'End_muh'
veli.bolum
ali.bolum
VeriBilimci.bolum

#Örnek Metodları

class VeriBilimci():
    calisanlar = []
    def __init__(self):
        self.bildigi_diller = []
        self.bolum = ''
    
    def dil_ekle(self, yeni_dil):
        self.bildigi_diller.append(yeni_dil)
        
        
ali= VeriBilimci()
ali.bildigi_diller 
ali.bolum

veli = VeriBilimci()
veli.bildigi_diller 
veli.bolum

dir(VeriBilimci)

VeriBilimci.dil_ekle("Python")

ali.dil_ekle("R")
ali.bildigi_diller
veli.dil_ekle("Python")
veli.bildigi_diller


#Miras Yapıları - (inheritance)

class Employees():
    def __init__(self):
        self.FirstName = ""
        self.LastName = ""
        self.Address = ""
        
        
class DataScience(Employees):
    def __init__(self):
        self.Programming = []
        
veriBilimci1 = DataScience()
veriBilimci1        
        
class Marketing(Employees):
    def __init__(self):
        self.StoryTelling = ""


mar1 = Marketing()
mar1


class Employees_yeni():
    def __init__(self,FirstName, LastName, Address):
        self.FirstName = FirstName
        self.LastName = LastName
        self.Address = Address
        
ali = Employees_yeni("a","b","c")
ali.FirstName
ali.LastName
ali.Address


#Python'da Fonksiyonel Programlamaya Giriş

# =============================================================================
# ->Fonksiyonlar dilin baştacıdır.
# ->(Birinci sınıf nesnelerdir.)
# ->Yan etkisiz fonksiyonlar(stateless, girdi - çıktı)
# ->Yüksek seviyeli fonksiyonlar.
# ->Vektörel opresyonlar
# =============================================================================

#Yan Etkisiz Fonksiyonlar (Pure Function)
#Örnek1: Yan Etki - Bağımsızlık

A = 9

def impure_sum(b):
    return b + A

def pure_sum(a,b):
    return a + b

impure_sum(6)
pure_sum(3, 4)


#Örnek 2 : Olumcul Yan Etkiler
#OOP

class LineCounter():
    def __init__(self,filename):
        self.file = open(filename, 'r')
        self.lines = []
        
    def read(self):
        self.lines = [line for line in self.file]
        
    def count(self):
        return len(self.lines)
    
lc = LineCounter("deneme.txt")

print(lc.lines)
print(lc.count()) 

lc.read()

print(lc.lines)
print(lc.count()) 

#FP -> Fonksşyonle programlama

def read(filename):
    with open(filename, 'r') as f:
        return [line for line in f]
    
def count(lines):
    return len(lines)

example_lines = read('deneme.txt')
lines_count = count(example_lines)
lines_count


#İsimsiz Fonksiyonlar (Anonymous Function)

def old_sum(a,b):
    return a + b

old_sum(4, 5)

new_sum = lambda a,b : a + b
new_sum(4, 5)
sirasiz_liste = [('b',3),('a',8),('d',12),('c',1)]
sirasiz_liste
type(sirasiz_liste[0])

sorted(sirasiz_liste, key = lambda x : x[1])


#Vektörel Operasyonlar (Vectorel Operations)
# Her bir elemanı bir bir ile çarpıcaz 
#OOP

a = [1,2,3,4]
b = [2,3,4,5]

#Çarpma sonucunu saklayabilmek için global alanda bir liste
#tanımladık
ab = []

for i in range(0, len(a)):
    ab.append(a[i] * b[i])
    
ab

#FP

import numpy as np

a = np.array([1,2,3,4])
b = np.array([2,3,4,5])

a*b


#map, filter & reduce
#map -> verilen bir vektörün içersinde belirli bir fonksiyonu 
#çalıştırma imkanı veriri


liste = [1,2,3,4,5]

for i in liste:
    print(i + 10)
    

list(map(lambda x: x + 10, liste))

#filter -> Benzer şekilde bir fonksiyon ve itereatif bir 
#nesne alarak çalışır, bu nesne üzerinden başka bir iteratif
#nesne oluşturulur ve iterarif nesne içerisinde aradığı
#şartın sağlandığı tüm elemanlar filtrelenir

liste = [1,2,3,4,5,6,7,8,9,10]

list(filter(lambda x: x % 2 == 0, liste))


#reduce -> map ve filter'e benzerdir fakat indirgeme işlemi yapar

from functools import reduce

liste = [1,2,3,4]

reduce(lambda a,b : a + b, liste)

#map, filter, reduce fonk. gördük, bunlar lambda yani isimsiz 
#fonksiyon yapısı ile birlikte kullanılabilen ve bize vektorel
#işlemler yapma imkanı sağlayabilen fonksiyonlardır.



#Modul Oluşturmak
#-> Bazen modul, bazen kütüphane, bazende paket denirlir
#Modelüller belirli amaçları yerine getirmek için bir arada 
#bulunan fonksiyonlar topluluğudur.
#Örneğin metin madenciliği işlemleri için geliştirilen bir 
#bir modül,kütüphane olduğunu düşünelim bu durumda metin 
#madenciliği etrafında kullanılan fonksiyonlar bir
#araya getirlmiş demektir bu.



# Hatalar / İstisnalar  (exception)
# Hatalar genel olarak 3'e ayrılır
#1- Programcını hataları
#2- Program hataları
#3- Exception, istisnalar


#ZeroDivisionError Hatası
a = 10
b = 0 

a/b

try:
    print(a/b)
except ZeroDivisionError:
    print("Payda da sıfır olmaz")


#Tip hatası

a = 10
b = "2"

try:
    print(a/b)
except TypeError:
    print("Sayı ve string problemi")


a = 10
b = 2

a/b

try:
    print(a/b)
except TypeError:
    print("Payda da sıfır olmaz")


######################################
try:
    print(a/b)
except ZeroDivisionError:
    print("Payda da sıfır olmaz")
except TypeError:
    print("Sayı ve string hatası")
######################################
# =============================================================================
# programcılı ve veri bilimcilik alanında zamanımızın çok çok
# büyük bir bölümü hata ayıklamakla, karşılaştığımız problemleri
# çözmekle geçicek, bundan dolayı try except yapısının dışında 
# bir problemel karşılaştığınımızda mutlaka ve mutlaka google'da 
# araştırın.
# =============================================================================









