
class Arac():
    def __init__(self,model,marka):
        self.model= model
        self.marka=marka
        
    def hareketEt(self):
        print("Hareket Et !")
        
class araba(Arac):
    pass

class Bot(Arac):
    def hareketEt(self):
        print("Yüzer")
        
class Ucak(Arac):
    def hareketEt(self):
        print("Uçar")
        
    
araba1= araba("GLA", "Mercedes")
bot1= Bot("Touring", "İbiza")
ucak1=Ucak("747", "Boeing")


for x in (araba1,bot1,ucak1):
    print(x.marka)
    print(x.model)
    x.hareketEt()
    print("")        
    
    
    
#Hatalar 

# print (x) #name error
# int("123456as") # Value Error
# print(5/0) #ZeroDivideError
# print ("Ybs",ybs) #Syntax Error 

try:
    print("try içindeyiz ")
    x=int("123asd")
    print(5/0)
except ValueError:
    print("Sadece Sayı Giriniz")
except ZeroDivisionError:
    print("0 a bölünme hatası ")
  
    
except:
    ("Bir hata oluştu")
    
    
    
try:    
    a=int (input("Birinci sayıyı giriniz : "))
    b=int (input("İkinci sayıyı giriniz :"))
    print(a/b)
except ZeroDivisionError:
    if b == 0:
        print(" Zero Division Hatası")
finally:
    ("Tekrar Deneyiniz")

