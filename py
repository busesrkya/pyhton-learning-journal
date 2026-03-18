# print('Hell"o world'
# print("h'i")

# #GİRİNTİNİN ÖNEMİ:

# if 7>2:
#  print("Seven greater than two")
#  print("None of your business")

# #variable
# # x=7
# # y="python"

# # print(x)
# # print(y)

# # x=8
# # x="buse"
# # print(x)

# #variable get the type
# x=7
# y="python"

# print(type(x))
# print(type(y))

# #variable single or double quotes


# y="python"
# print(y)
# z='awesome'
# print(z)


# #DEĞİŞKEN İSİM KURALLARI
# #1.
# _name="Buse"
# name="Buse"
# name2="Emre"
# Myname="Eylem"

# print(_name)
# print(name)
# print(name2)
# print(Myname)


#ÇOK KELİMELİ DEĞİŞKEN İSİMLERİ

# kupunToplamHacmi=70
# print(kupunToplamHacmi)

# UcgeninAlanı=90
# print(UcgeninAlanı)

# kupun_toplam_hacmi=95
# print(kupun_toplam_hacmi)



# #FARKLI DEĞİŞKENLERE TEK SATIRDA DEĞER ATAMA

# x,y,z="Banana","Apple","Grape"

# print(x)
# print(y)
# print(z)

# a=b=C="red"
# print(a)


#OUTPUT VERİABLE

# x="Python"
# y="is"
# z="wonderful"

# print(x,y,z)

# x=10
# y=7

# print(x+y)

# x=8
# y="python"
# print(x,y)



# #SAYISAL VERİ TÜRLERİ
# name="Fehmi" #string
# age=34 #integer
# weight=84.15 #float
# complex=2j #complex data type

# #print(name+ str(age)+str( "weight")+str( "complex"))
# #yukarıda yazdıgım seyi anlamadım ve yanlış yazdım

# print("isim:"+name+" yaş:"+str(age)+" kilo:"+str(weight)+" karmasik sayilar:"+str(complex))

# print(type(name))
# print(type(age))
# print(type(weight))



#PROGRAMLAMADA VERİ TÜRÜ

# myList=["Apple","Grape","Cherry","Watermelon","Lemon","Banana"] #list data type
# #myList=["Red","Blue","White","Purple"]
# print(type(myList))
# print(myList)

# myRange=range(9) #range data type
# print(*myRange)


# myDict={"name":"Fehmi","age":34} #dictionary data type
# print(myDict)

# mySet={"Apple","Grape","Cherry","Watermelon","Lemon","Banana"} #set data type

# x=7 #int
# y=19.57 #float
# z=2j #complex

# print("int:",x,"\nfloat:",y,"\ncomplex",z)



#DAİRENİN ALANI VE ÇEVRESİNİ BULAN PROGRAM

#dairenin alanı:pi*r*r
#dairenin çevresi:2*pi*r
#3.14159

# pi=3.14159
# radius_of_circle=float(input("Yarı çap:"))

# area_of_circle=pi*radius_of_circle*radius_of_circle

# circumference_of_circle=2*pi*radius_of_circle

# print("Alan:",area_of_circle)
# print("Çevre:",circumference_of_circle)


#VERİLEN İKİ TAM SAYIYI TOPLAYAN PROGRAM

# number1=int(input("Birinci Sayi:"))
# number2=int(input("İkinci Sayi:"))

# sum=number1+number2

# print("Toplam:",sum)



#PROGRAMLAMADA RANDOM MODÜLÜ
# import random
# print(random.random())


# import random
# random.seed(7)
# print(random.random())
 #tekrarlanabilir sonuçlar elde etmek için





#GETSTATE VE STESTATE METODU
# import random
# print(random.random())

# state=random.getstate()
# print(random.random())
# print(random.random())

# random.setstate(state)
# print(random.random())



# import random
# print(random.getrandbits(8))

# import random
# print(random.randrange(1,10))

# print(random.randrange(1,10,3))

# print(random.randint(1,10))



#CHOCİES METODU

# import random

# myList=["black","white","Purple","pink"]
# print(random.choice(myList))




#STRİNG VERİ TÜRÜ

# print("ıt's alright")
# print("He is called \'big boy\'")

# text="python"
# print(text)

# text=""" This is so good
#  life is good
#  ı'm a veriable
#      """
# print(text)

# cars=["BMW","Volvo","Skoda","Nissan"]
# print(cars[0])

# text="Python is easy"
# print(len(text))





#İN KULLANIMI:
# text="The best languages in life are free!"
# print("expensive" in text)

# text="The best languages in life are free!"
# search="best"
# if search in text:
#  print("Yes,'best' is present")




#  #NOT İN KULLANIMI:

# text="The best languages in life are free!"
# search="expensive"

# if search not in text:
#  print("No, 'expensive' is not present")




# #STRİNG DİLİMLEME
# text="python is weird"

# print(text[1:5])
# print(text[:5])
# print(text[-4:-1])




# #STRİNG BİRLEŞTİRME
# text="python"
# text2=" is weird"
# print(text+text2)




#UPPER VE LOWER METODU
# text="Python is so easy"
# print(text.upper())
# print(text.lower())




#STRİP METODU
# text="     Python is so easy    "
#print(text.strip())




#REPLACE METODU
# text="Python is so easy"
# print(text.replace("P","T"))



#SPLİT METODU
# text="Python is so, easy"
# print(text.split(","))



#KAÇIŞ KARAKTERLERİ
# text="Pyhton is doing \\ well"
# print(text)

# text="Python\nis\ndoing\nwell"
# print(text)

# text="Hello\rPyth"
# print(text)

# text="Hello\tPyt"
# print(text)

# text="Hello\bPython"
# print(text)



#STRİNG FORMATLAMA

# age=24
# name="Buse"
# text="my name is {0}, ı am {1}".format(name,age)
# print(text)



# #F STRİNG KULLANIMI
# # age=34
# name="Fehmi Uyar"
# text=f"My name is {name}, I am {age}"
# print(text)

# price=19.45468
# text=f"The price is {price.1f} turkish lira"
# print(text)



#STRİNG METODLARI
#CAPİTALİZE METODU

# text="welcome to my world. How is it going?"
# result=text.capitalize()
# print(result)


#CASEFOLD METODU
# text="HELLO I AM BUSE"
# result=text.capitalize()
# print(result)



#TİTLE METODU
# text="hello ı am buse"
# result=text.title()
# print(result)



# text="hello f7f7f7 and py4th4on"
# result=text.title()
# print(result)



# #SWAPCASE METODU
# text="Hello ı am Buse"
# result=text.swapcase()
# print(result)



# #İSLOWER METODU
# text="which why is it?"
# result=text.islower()
# print(result)



# #ARİTMETİK VE ATAMA OPERATÖRLERİ
# number1=12
# number2=7

# result1=number1+number2
# print(result1)

# result2=number1**number2
# print(result2)

# result3=number1%number2
# print(result3)

# result4=number1//number2
# print(result4)



#KARŞILAŞTIRMA OPERATÖRÜ ÖRNEĞİ
# realPassword="12345"
# myPassword=input("Enter the password:")

# if realPassword == myPassword:
#  print("congratulations its the correct password")

# else:
#  print("sorry that is the wrong password")



#GİRİLEN SAYI TEK Mİ ÇİFT Mİ
# number=int(input("Enter a number:"))

# if number<0:
#  print("The entered number cannot be less than zero")
# elif number %2 ==0:
#  print(f"{number} is an even number")
# else:
#  print (f"{number} is an odd number")



#MANTIKSAL VE KİMLİK OPERATÖRLERİ:
# AND
# score=int(input("Enter the score: "))
# if score<60:
#     print("You failed the exam")
# elif score>=60 and score<80:
#     print("You passed the exam")
# else:
#     print("You are amazing")

#OR
# score=int(input("Enter the score: "))
# if score<10 or score>=90:
#  print("You are amazing")

# elif score>=10 and score<50:
#  print("You failed the exam")

# else:
#  print("You passed the exam")



#NOT MANTIKSAL OPERATÖRÜ
# score=int(input("Enter the score: "))
# if not (score>50):
#     print("You failed the exam")
# else:
#     print("You passed the exam")



#İS KİMLİK OPERATÖRÜ

# x=["strawberry","grape","pineapple"]
# y=["strawberry","grape","pineapple"]
# z=x
# print( x is y)
# print(x is z)
# print(x==y)



#İS NOT KİMLİK OPERATÖRÜ

# x=["starwberry","grape","pineapple"]
# y=["stawberry","grape","pineapple"]
# z=x
# print(x is not z)
# print(x!=y)



#LİSTELERE ERİŞİM
# fruit=["strawberry","apple","pineapple","banana","watermelon"]
# print(fruit[2])
# print(fruit[0:2])
# print(fruit[-1])
# print(fruit[:])
# print(fruit[-4:-1])



#İN KULLANIMI
# if "pineapple" in fruit:
#     print("Yes this fruit is in the fruits list")
# else:
#     print("No this fruit is in the fruits list ")



#LİSTELERDE DEĞİŞTİRME
#fruit=["melon","watermelon","apple","banana","strawberry"]
# fruit[2]="cherry"
# print(fruit)

# fruit[2:4]="kiwi","orange"
# print(fruit)

# fruit[3:4]="pear","peach"
# print(fruit)



#LİSTELERE VERİ EKLEME VE KOPYALAMA
#LİSTE METODLARI



#APPEND() METODU İLE VERİ EKLEME

#fruit=["grape","orange","strawberry","pineapple","melon","watermelon"]
# fruit.append("cherry")
# print(fruit)



#İNSERT() METODU İLE VERİ EKLEME

# fruit.insert(1,"peach")
# print(fruit)



#EXTEND() METODU İLE VERİ EKLEME

# fruit=["grape","orange","strawberry"]
# fruit2=["pineapple","melon","watermelon"]

# fruit.extend(fruit2)
# print(fruit)
# print(len(fruit))



#LİSTE ÖGELERİNİ KALDIRMAK

# fruit=["grape","orange","strawberry","pineapple","melon","watermelon","strawberry","strawberry"]

# fruit.remove("strawberry")
# print(fruit)


#POP METRODU İLE LİSTEDEN VERİ KALDIRMAK

#fruit=["grape","orange","strawberry","pineapple"]
# fruit.pop()
# print(fruit)


#DEL ANAHTAR SÖZCÜĞÜ İLE VERİ KALDIRMAK

# fruit=["grape","orange","strawberry","pineapple"]
# del fruit[3]
# print(fruit)

# del fruit
# print(fruit)



#CLEAR METODU

# fruit=["apple","banana","melon"]
# fruit.clear()
# print(fruit)



#WHİLE DÖNGÜSÜ


#ÖRNEK 1
# i=1
# while(i<=7):
#     print(i,"-python")
#     i+=1
# print("done")



#ÖRNEK2

# i=1
# while(i<=7):
#     print(i,end=" ")
#     i+=1
# print("\ndone")


#BREAK KOMUTU 

# i=1
# while(i<=7):
#     print(i,end=" ")
#     if(i==4):
#        break
#     i+=1
# print("\ndone")



#WHİLE DÖNGÜSÜ VE CONTİNUE KOMUTU

# i=1
# while(i<=7):
#     print(i,end=" ")
#     if(i==4):
#         continue
#     i+=1


# i=!
# while(i<=7):
#     print(i,end=" ")
#     i+=1
# else:
#     print("\n i variable is no longer less than 7")
# print("\n while loop is over")


#LİSTELERLE WHİLE KULLANIMI:

# myNumbers=[70,19,34,23,7]

# i=0
# while(i<len(myNumbers)):
#     print(myNumbers[i],end=" ")
#     i+=1


#WHİLE İLE BELLİ BİR SAYIDAN GERİYE YAZDIRMA

# i=70
# while(i>0):
#     print(i,end=" ")

# i-=5



#GİRİLEN SAYIYI SIRALAYAN PROGRAM

# myNumbers[]
# i=0
# while(i<7):
#     input_number=(int("Enter an integer:"))
#     myNumbers.append(input_number)
#     i+=1
# myNumbers.sort()

# x=0
# while(x<7):
#     print(myNumbers[x],end=" ")
#     x+=1




#GİRİLEN SAYIYA KADAR OLAN TEK VE ÇİFT SAYILARI YAZDIRAN PROGRAM

# start_number=int(input("Enter a number:"))
# end_number=int(input("Enter a number:"))
# while(start_number<end_number):
#     if(start_number %2==0):
#         print(start_number,end=" ")
#     start_number+=1


#FAKTÖRİYEL HESAPLAYAN PROGRAM

# result=1
# i=1
# number=int(input("Enter an integer"))
# while(i<=number):
#     result*=i
#     i+=1
# print(f"{number}!={result}")


#FOR DÖNGÜSÜ

#fruits=["orange","strawberry","apple","watermelon","melon","cherry"]

# for item in fruits:
#     print(item)

# for item in fruits:
#     print(item,end=" ")   #end= " " parametresi yanyana yazmamı sağlar


# i=0
# for item in fruits:
#     print(i, ".index =", item)
#     i+=1



 #TUPLE İLE FOR KULLANIMI

# myNumber=(70,19,35,40,90)

# for number in myNumber:
#  print(number)



 #STRİNGLERLE FOR KULLANIMI

#  text="Python"
#  for item in text:
#   print(item)



#BREAK STEATMENT İLE FOR KULLANIMI

#fruits=["grape","orange","strawberry","apple"]

# for item in fruits:
#  print(item)
#  if(item=="orange"):
#   break
 

#PRİNTİN YERİNİN ÖNEMİ
# for item in fruits:
#     if item == "orange":
#         break
#     print(item)


#CONTİNUE İLE FOR KULLANIMI


# for item in fruits:
#     if (item=="orange"):
#        continue
#     print(item)


#orange'ı atla bir sonraki adıma geç demek istiyorum


#RANGE METODU İLE FOR KULLANIMI

# for item in range(8):
#     print(item)


# for item in range(9):
#   print(item,end=" ")
          


# for item in range(8,19,4):
#     print(item,end=" ")
          


#FOR DÖNGÜSÜ BİTİMİNDE ELSE KULLANIMI:

# for item in range (1,8):
#    print(item,end=" ") 
# else:
#    print("\nFor loop is over!")        
          
          
#GİRİLEN SAYIYA KADAR OLAN TEK VE ÇİFT SAYILARI BULMA

# number=int(input("Enter an integer:"))
# for item in range(number):
#   if (item %2==1):
#     continue
#   print(item,end=" ")

# else:
#   print("\n For loop is over")
          


#İÇİÇE DÖNGÜ(NESTED LOOP)

# adjectives=["red","big","tasty"]
# fruits=["grape","strawberry","cherry"]

# for outer in adjectives:
#     for inner in fruits:
#         print(outer,inner)
          

#İÇİÇE LİSTELERİN FOR İLE KULLANIMI

# myNumbers=[
#     [70,19],
#     [34,7],
#     [23,41]
# ]

# for item1,item2 in myNumbers:
#     print(f"{item1},{item2}")



#ENUMERATE KOMUTU 
# fruits=["grape","strawberry","cherry","orange"]

# for index,item in enumerate (fruits):
#     print(f"{index}-{item}")
          
# for index,item in enumerate (fruits,3):
#     print(f"{index}-{item}")    
      
           
          
#ZİP KOMUTU          


# names=["Ali","Buse","Zeynep"]
# ages=[20,21,22]

# for names,ages in zip (names,ages):
#     print(names,ages)


          
          
#BASİT SAYI TAHMİNİ OYUNU:

# import random

# sayi=random.randint(1,10)
# hak=5
          
# print("Sayı tahmin etme oyunu")
# print("1 ile 10 arasından bir sayı tuttum!")
# print("5 hakkın var")

#  while hak>0:
#     tahmin=int(input("Tahmin gir:"))

#     if tahmin==sayi:
#         print("Tebrikler bildin")
#         break
    
#     elif tahmin<sayi:
#         hak-=1
#         print("Daha büyük bir sayı dene")

#     else:
#         hak-=1
#         print("Daha kücük bir sayı dene")

#     print(f"kalan hak: {hak}")

#     if hak==0:
#       print(f"kaybettin doğru sayı:{sayi}")





#FOR DÖNGÜSÜ İLE LİST KULLANIMI

# fruits=["grape","orange","strawberry","blackberry"]

# for item in range(len(fruits)):
#     print(item)



#WHİLE DÖNGÜSÜ İLE LİST KULLANIMI

# i=0
# while(i<len(fruits)):
#     print(fruits[i])
#     i+=1



#LİST COMPREHENSİON
#Döngüleri kullanmamızı sağlar

# fruits=["grape","orange","strawberry","blackberry","fig","apricot","kiwi"]

# for item in fruits:
#     print(item)


#tek parça halinde yazmak istersem

# [print(item) for item in fruits]
 
# new_list=[]

# for item in fruits:
#     if("g" in item):
#         new_list.append(item)
# print(new_list)



# new_list=[item for item in fruits if("g" in item)]
# print(new_list)


#kayısı olmayan meyveleri new_list e ekle

# new_list=[item for item in fruits if(item !="apricot")]
# print(new_list)




#new listimize sayı olusturmak istersek
# new_list=[]
# new_list=[item for item in range(10)]
# print(new_list)




#Koşullardan yararlanırsak

# new_list=[]

# new_list=[item for item in range(10) if(item<7)]
# print(new_list)

#meyvelerimi listeden çek ama hepsini büyük harfle yaz

#new_list=[item.upper() for item in fruits]

#meyvelerin yerine dokuz adet python yaz

#new_list=["python" for item in fruits]

#listemdeki kiviyi muz ile değiştirmek istersem

#new_list=[item if item!="kiwi" else "banana" for item in fruits]



#SHORT HAND İF KOŞULLU İFADELER

# a=int(input("Enter an integer:"))
# b=int(input("Enter an another integer:"))

# if(a>b):print(f"{a} is greater than {b}")



# #ELSE İLE KULLANIMI
# print(f"{a}" is greater than {b}") if(a<b) elseprint(f)  devamını yazacağım




#CONDİTİONAL EXPRESSİONS KOŞULLU İFADELER 2

#AND MANTIKSAL OPERATÖR
# a=70
# b=19
# c=123

# if(a>b and c<a):
#     print("Both conditions are true")
  


#OR MANTIKSAL OPERATÖR
# a=70
# b=19
# c=123

# if(a>b or c==a):
#  print("At least one of the conditions is true")



#NOT MANTIKSAL OPERATÖRÜ

# a=70
# b=123

# if(not a>b):
#     print("At least are of the conditions is true")

#BU ŞEKİLDE DE YAZABİLİRİM

# print(f"{a} is not greater than {b}")



#İÇİÇE KOŞULLU İFADELER

# x=int(input("Enter an integer:"))

# if(x>0):
#     print("This is a positive number")
#     if(x>20):
#         print("and also above 20")
#     else:
#         print("but not above 20")

# elif(x==0):
#     print("This number is zero")
# else:
#     print("This is a negative number")




#PASS VEYA ÜÇ NOKTA KOMUTU

# a=10
# b=20

# if(a<b):
#     pass



#KOŞULLU İFADE ÖRNEKLERİ
#GİRİLEN KARAKTER HARF Mİ? HARF İSE KÜÇÜK MÜ? BÜYÜK MÜ? SESLİ Mİ? SESSİZ Mİ?

# myCharacter=input("Enter a character:")

# if(len(myCharacter) !=1):
#      print("Please enter only character")

# else:
#     if(myCharacter.isalpha()):
#       if(myCharacter.isupper()):
#         case="uppercase"

#       else:
#         case="lowercase"


#       vowels="AEIOUaeıou"
#       if(myCharacter in vowels):
#         letter_type="vowel"

#       else:
#         letter_type="consanant"

#       print(f"The character '{myCharacter}' is an {case} {letter_type}")

#     else:
#      print(f"the character '{myCharacter} is not a letter")



#TUPLE VERİ TÜRÜ
# fruits=("strawberry","apple","grape","cherry","melon","pineapple","watermelon")

#print(len(fruits))

# fruits=("strawnerry",)
# print(type(fruits))

#HERHANGİ BİR VERİ TİPİNDE DE OLABİLİR
# myNumbers=(1,7,8,11,23)

# members=(True,False,True,False,True,True)
# print(type(members))

# complex_tuple=("Fehmi",34,True,"Şeyda",36,False)

# fruits1=tuple(("strawberry","apple","pineapple","kiwi","banana"))
# print(fruits1)



#TUPLE ÖĞELERİNE ERİŞİM VE BİRLEŞTİRME
#TUPLE ÖGELERİNE ERİŞİM:

# fruits=("banana","pineapple","kiwi","banana","strawberry","melon","watermelon")
# print(fruits[3:6])

# print(fruits[4])

# print(fruits[2:])

# print(fruits[:5])



#NEGATİF İNDEKSLEME:

# fruits=("grape","orange","apple","melon","cherry","kiwi","watermelon")

# print(fruits[-1])

# print(fruits[-6:-3])

# print(fruits[:-4])

# print(fruits[-5:])



#BELİRLİ BİR ÖGENİN TUPLE DA MEVCUT OLUP OLMADIGINI ANLAMAMIZ İCİN LİSTELERDEKİ GİBİ İN İFADESİNİ KULLANIRIZ

#fruits=("grape","orange","apple","melon","cherry","kiwi","watermelon")

# search="strawberry"
# if search in fruits:
#     print(f"yes,{search} is in the fruits tuple")
# else:
#     print(f"No,{search} isn't the tuple")



#KOŞUL KURMADAN YAZDIRABİLECEĞİMİZ YÖNTEM

# search="orange"
# if search in fruits:
#     print("yes it is in there")




#TUPLELARI BİRLEŞTİRME:

# fruits=("grape","orange","apple","melon","cherry","kiwi","watermelon")
# numbers=(3,5,7,9,1)
# join_tuple=fruits+numbers
# print(join_tuple)



#TUPLE ÖGELERİ COĞALTMAK

# fruits=("grape","orange","apple","melon","cherry","kiwi","watermelon")
# multiply_tuple=fruits*2
# print(multiply_tuple)



#TUPLE VERİ GÜNCELLEME,EKLEME,KALDIRMA,PAKETTEN ÇIKARTMA:

#TUPLE GÜNCELLEME:
# fruits=("grape","orange","apple","melon","cherry","kiwi","watermelon")

# temp_fruits=list(fruits)
# temp_fruits[2]="lemon"
# fruits=tuple(temp_fruits)
# print(fruits)



#VERİ EKLEME:
# fruits=("grape","orange","apple","melon","cherry","kiwi","watermelon")

# temp_fruits=list(fruits)
# temp_fruits.append("lemon")
# fruits=tuple(temp_fruits)
# print(fruits)


#TUPLE'A TUPLE EKLEMEK İÇİN:

# fruits=("grape","orange","strawberry","fig")
# extra_fruits=("blackberry",)
# fruits+=extra_fruits
# print(fruits)


# #TUPLE VERİ KALDIRMAK İÇİN:
# fruits=("grape","orange","strawberry","fig")

# temp_fruits=list(fruits)
# temp_fruits.remove("grape")
# fruits=tuple(temp_fruits)
# print(fruits)



# #TUPLE SİLME:
# fruits=("grape","orange","strawberry","fig")
# del fruits



#PAKETLEME VE PAKETTEN CIKARTMA
#PAKETLEME

# fruits=("grape","orange","strawberry","fig")



#PAKETTEN ÇIKARTMA:

# fruits=("grape","orange","strawberry")

# (x,y,z)=fruits

# print(x)
# print(y)
# print(z)




#VARİABLE SAYISI DEĞER SAYISINDAN AZ İSE * KULLANABİLİRİZ

# fruits=("grape","orange","apple","melon","cherry","kiwi","watermelon")
# (x,*y,z)=fruits
# print(x)
# print(y)
# print(z)




#TUPLE İLE FOR DÖNGÜSÜ KULLANIMI:

# fruits=("grape","orange","apple","melon","cherry","kiwi","watermelon")

# for item in range (len(fruits)):
#     print(fruits[item])





#TUPLE İLE WHİLE DÖNGÜSÜ KULLANIMI:



# fruits=("grape","orange","apple","melon","cherry","kiwi","watermelon")
# i=0
# while(i<len(fruits)):
#     print(fruits[i])
#     i+=1





#COUNT VE İNDEX YERLEŞİK TUPLE METODLARI:

#COUNT
# fruits=("grape","orange","apple","melon","cherry","kiwi","watermelon","fig")
# print(fruits.count("fig"))

#İNDEX
# myNumbers=(7,19,7,8,5,7)
# print(myNumbers.index(7))




#SET KOLEKSİYONU

# fruits={"grape","banana","cherry"}
# print(fruits)



#SET İÇİNEKİ ELEMAN TÜRLERİ

# fruits={"grape","orange","apple","melon","cherry","kiwi","watermelon","fig"}

# setNumber={1,2,9,5}

# setBoolean={True,False,False,True}
# print(setBoolean)



#TEK BİR SET FARKLI VERİ TİPLERİNİ İÇEREBİLİR

# set_complex={"Fehmi",34,True,"Şeyda"}
# print(set_complex)

# print(type(set_complex))




#SETLERİ BİRLEŞTİRME:

#UNİON METODU İLE BİRLEŞTİRME:

# fruits1={"grape","orange","fig"}

# fruits2={"cherry","apricot"}

# result=fruits1.union(fruits2)
# print(result)




#BİRDEN FAZLA VERİ TİPİNİ UNİON İLE BİRLEŞTİRME

# fruits1={"grape","orange","fig"}

# fruits2={"cherry","apricot"}

# setNumber1={1,3,8,80}
# setNumber2={9,6,3,45,2}

# result=fruits1.union(setNumber1,fruits2)
# print(result)




# | OPERATÖRÜ İLE BİRLEŞTİRME İŞLEMİ

# fruits1={"grape","orange","fig"}
# setNumber2={9,6,3,45,2}
# result=fruits1|setNumber2
# print(result)


#UPDATE METODU

# setNumber1={1,7,19,22,4}
# setNumber2={5,12,2}

# setNumber1.update(setNumber2)
# print(setNumber1)

#İNTERSECTİON METODU

# setNumber1={1,7,19,22,4}
# setNumber2={5,12,22}

# result=setNumber1.intersection(setNumber2)
# print(result)






# & OPERATÖRÜYLE İNTERSECTİON

#result=setNumber1 & setNumber2




#İNTERSECİTON_UPDATE METODU


# number1={9,13,50,60}
# number2={6,9,3,50}
# number3={8,9,50,7,2}

# number1.intersection_update(number2,number3)
# print(number1)






#İNTERSECTİON_UPDATE KISAYOLU
#&= 

# number1 &= number2 &number3
# print(number1)




#SET METODLARI

#DİFFERENCE

# setNumber1={1,7,19,23,4}
# setNumber2={5,12,34,19,23}

# result=setNumber1.difference(setNumber2)
# print(result)



#DİFFERENCE KISAYOLU
# - OPERATÖRÜYLE GERÇEKLEŞTİRİLİR

# result=setNumber1 - setNumber2
# print(result)




#DİFFERENCE_UPDATE METODU

# setNumber1={1,7,19,23,4}
# setNumber2={5,12,34,19,23}
# setNumber3={8,6,19}

# setNumber1.difference_update(setNumber2,setNumber3)
# print(setNumber1)




#DİFFERENCE_UPDATE KISAYOLU 
# -=

# setNumber1={1,7,19,23,4}
# setNumber2={5,12,34,19,23}
# setNumber3={8,6,19}

# setNumber1 -= setNumber2 | setNumber3
# print(setNumber1)



#SYMMETRİC_DİFFERENCE METODU
 
# setNumber1={1,7,19,23,4}
# setNumber2={5,12,34,19,23}
# setNumber3={8,6,19}

# result=setNumber1.symmetric_difference(setNumber2)
# print(result)



#SYMMETRİC_DİFFERENCE KISAYOLU 
# ^ OPERATÖRÜ


# setNumber1={1,7,19,23,4}
# setNumber2={5,12,34,19,23}
# setNumber3={8,6,19}

# result=setNumber1 ^ setNumber2 ^ setNumber3
# print(result)




#SYMMETRİC_DİFFERENCE_UPDATE METODU

# setNumber1={1,7,19,23,4}
# setNumber2={5,12,34,19,23}

# setNumber1.symmetric_difference_update(setNumber2)
# print(setNumber1)




#SYMMETRİC_DİFFERENCE_UPDATE METODU KISAYOLU

#  ^=  OPERATÖRÜ

# setNumber1={1,7,19,23,4}
# setNumber2={5,12,34,19,23}


# setNumber1 ^=setNumber2
# print(setNumber1)




#COPY METODU

# fruits={"grape","orange","strawberry","blackberry"}

# result=fruits.copy()
# print(result)



#İSDİSJOİNT METODU

# setNumber1={1,7,19,23,4}
# setNumber2={5,12,34,19,23}

# result=setNumber1.isdisjoint(setNumber2)
# print(result)



#İSSUBSET METODU

# setNumber1={7,19}
# setNumber2={5,12,34,19,4}

# result=setNumber1.issubset(setNumber2)
# print(result)



#İSSUBSET METODU KISAYOLU
# <=

# setNumber1={7,19}
# setNumber2={5,12,34,19,4}

# result=setNumber1 <=setNumber2
# print(result)


#İSSUPERSET METODU KISAYOLU

# setNumber1={7,19,12,34,2,123,87,54}
# setNumber2={5,12,34,19,7}

# result=setNumber1.issuperset(setNumber2)
# print(result)


#İSSUPERSET METODU KISAYOLUy
# >= 

# result=setNumber1 >=setNumber2

