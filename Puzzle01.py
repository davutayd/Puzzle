import random as rnd
import tkinter as Tk 
import sqlite3 as vt

Demet=[]


def degistir(numara):
	global tiklama
	global ilk
	tiklama += 1 
	if tiklama == 2:
		ikinci = numara
		ilksat, ilksut, ikincisat, ikincisut = ilk // sut, ilk % sut, ikinci // sut, ikinci % sut
		if (ilksat - ikincisat)**2 + (ilksut -ikincisut)**2 <= 2:
      
			cumle = "create table if not exists Hareketler (dgmno int, dgmmetni text, dgmrenk text)"
			sql.execute(cumle)
   
			for row in range(8):
				for column in range(8):
						cumle = "insert into Hareketler values (%d,'%s','%s')"%(row*sut+column,dugmeler[row*sut+column]["text"],dugmeler[row*sut+column]["bg"])
						sql.execute(cumle)
      
			
   
			dugmeler[ilk]["text"], dugmeler[ikinci]["text"] = dugmeler[ikinci]["text"], dugmeler[ilk]["text"]
			dugmeler[ilk]["bg"], dugmeler[ikinci]["bg"] = dugmeler[ikinci]["bg"], dugmeler[ilk]["bg"]
			cumle = "update dugmeler set dgmmetni = '%s', dgmrenk = '%s' where dgmno = %d"%(dugmeler[ilk]["text"],dugmeler[ilk]["bg"],ilk)
			sql.execute(cumle)
			cumle = "update dugmeler set dgmmetni = '%s', dgmrenk = '%s' where dgmno = %d"%(dugmeler[ikinci]["text"],dugmeler[ikinci]["bg"],ikinci)
			sql.execute(cumle)

			cumle = "select * from Hareketler"
			sql.execute(cumle)
			Demet.append(sql.fetchall())
			
			
			bag.commit()
		tiklama = 0
	else:
		ilk = numara

uzunluk=len(Demet)

def birhamlegeri(event):
	
	#liste=swap[-64*n:]
	
	print(Demet[uzunluk-1][1][2])
	print(uzunluk)
	dugmeler=[]
	sat, sut = 8,8
	for row in range(sat):
			for column in range(sut):
				dugmeler.append(Tk.Button(text = str(Demet[uzunluk-1][row*sut+column][1]), bg = Demet[uzunluk-1][row*sut+column][2], command = lambda x = row*sut+column : degistir(x) ))
				dugmeler[row*sut+column].place(x = column*gen+20, y=yuk*row+20+100,height = yuk, width = gen)
	
	

def birhamleileri(event):

	print(Demet[uzunluk-1][1][2])
	print(uzunluk)
	dugmeler=[]
	sat, sut = 8,8
	for row in range(sat):
			for column in range(sut):
				dugmeler.append(Tk.Button(text = str(Demet[uzunluk-1][row*sut+column][1]), bg = Demet[uzunluk-1][row*sut+column][2], command = lambda x = row*sut+column : degistir(x) ))
				dugmeler[row*sut+column].place(x = column*gen+20, y=yuk*row+20+100,height = yuk, width = gen)
	uzunluk=uzunluk+1
	return uzunluk

def girilensayikadarhamlegeri(event,a):

	print(Demet[uzunluk-1][1][2])
	print(uzunluk)
	dugmeler=[]
	sat, sut = 8,8
	for row in range(sat):
			for column in range(sut):
				dugmeler.append(Tk.Button(text = str(Demet[uzunluk-1][row*sut+column][1]), bg = Demet[uzunluk-1][row*sut+column][2], command = lambda x = row*sut+column : degistir(x) ))
				dugmeler[row*sut+column].place(x = column*gen+20, y=yuk*row+20+100,height = yuk, width = gen)
	uzunluk=uzunluk-a
	return uzunluk

def girilensayikadarhamleileri(event,a):

	print(Demet[uzunluk-1][1][2])
	print(uzunluk)
	dugmeler=[]
	sat, sut = 8,8
	for row in range(sat):
			for column in range(sut):
				dugmeler.append(Tk.Button(text = str(Demet[uzunluk-1][row*sut+column][1]), bg = Demet[uzunluk-1][row*sut+column][2], command = lambda x = row*sut+column : degistir(x) ))
				dugmeler[row*sut+column].place(x = column*gen+20, y=yuk*row+20+100,height = yuk, width = gen)
	uzunluk=uzunluk+a
	return uzunluk




bag = vt.connect("veriler.db")
sql = bag.cursor()
cumle = "create table if not exists dugmeler (dgmno int, dgmmetni text, dgmrenk text)"
sql.execute(cumle)

cumle = "DELETE FROM Hareketler"
sql.execute(cumle)
bag.commit()

cumle = "delete from dugmeler"
sql.execute(cumle)
bag.commit()

tiklama = 0
renk = ["Yellow", "Red", "Blue", "Green", "Orange", "Brown", "Magenta", "Tomato", "Gray"]

 
sat, sut = 8,8
form = Tk.Tk()
a,b,c,d = 400, 500, (form.winfo_screenwidth()-600)//2, (form.winfo_screenheight()-400)//2
form.title("Puzzle")
form.geometry("%sx%s+%s+%s"%(a,b,c,d))

def hello(a):
	
    print(a) 


GGeri = Tk.Button(text='Girilen Sayı Kadar Hamle Geri <--')
GGeri.pack()
GGeri.bind('<Button-1>', lambda event, a=2: 
                            girilensayikadarhamlegeri(a))

IIleri = Tk.Button(text='Girilen Sayı Kadar Hamle İleri -->')
IIleri.pack()
IIleri.bind('<Button-1>', lambda event, a=2: 
                            girilensayikadarhamleileri(a))

E1 = Tk.Entry(form)
E1.pack()
Girdi = E1.get()

 





Geri = Tk.Button(text='Bir Hamle Geri <-')
Geri.pack()
Geri.bind('<Button-1>', birhamlegeri)

Ileri = Tk.Button(text='Bir Hamle İleri ->')
Ileri.pack()
Ileri.bind('<Button-1>', birhamleileri)

dugmeler = []
secim = len(renk)-1
yuk, gen = 45, 45
liste = rnd.sample(range(1,sat*sut+1), sat*sut)
for row in range(sat):
	for column in range(sut):
		dugmeler.append(Tk.Button(text = str(liste[row*sut+column]), bg = renk[rnd.randint(0,secim)], command = lambda x = row*sut+column : degistir(x) ))
		dugmeler[row*sut+column].place(x = column*gen+20, y=yuk*row+20+100,height = yuk, width = gen)
		cumle = "insert into dugmeler values (%d,'%s','%s')"%(row*sut+column,str(liste[row*sut+column]),dugmeler[row*sut+column]["bg"])
		sql.execute(cumle)
bag.commit()





Tk.mainloop()