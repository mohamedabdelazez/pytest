import math
from colored import fg
color = fg('red')
color2 = fg('white')
color3 = fg('green')
#print (color + 'Hello World !!!')
pi = math.pi

vf = 1 
while vf == 1 :
	print ("""\n\t[+]====>interpolition {i}\n\n\t[+]====>logmenTemp {l}\n\n\t
	\t[+]====>heat Q=m*cp*dt {q}\n\n\t[+]====>correction factor [P and R ]{p}\n\n\t[+]====>heat Q=U*A*DTlm {q2}\n\n\t
	\t[+]====>mass flow rate m = density*A*V {m1}\n\n\t
	\t[+]====>mass flow rate m = Q\cp*dt {m2}\n\n\t """)
	print(color3+"if you wnt to close tybe  ",color+"exit")
	print(color2)
	I = str(input("[+]what do you need to Do ? : "))
	if I == "exit":
		break 
	if I == "i" :
		def interpolition() : #this function is used to do interpolition 
			a = float (input("enter the small value : "))
			b = float (input("enter the mid value : "))
			c = float(input("enter the large value : "))
			d = float(input("enter the first value : "))
			print ("this should be the unknown value")
			f = float(input("enter the last value : "))
			x = (((f-d)*(b-a))/(c-a))+(d)
			print(color3 + "The value is : ",x)
			print(color2)
		interpolition()
	elif I == "l":
		def logmenTemp() : #this function is used to calcolate logmenTemp
			t1 = float (input("enter the tube  t1 : "))
			t2 = float (input("enter the shell  T1 : "))
			T1 = float (input("enter the tube  t2 : "))
			T2 = float (input("enter the shell T2 : "))
			DT1 = t1-t2
			DT2 = T1-T2
			logmenTemp = (DT2-DT1)/math.log(DT2/DT1)
			print (color3 + "log mean Temperature = ",logmenTemp)
			print(color2)
		logmenTemp()
	elif I == "q" :
		def Q1() : #this function is used to calcolate the ammount of heat 
			print(color + "[+++++]before you start if you put the CP kj\kg.c the Q will in KW[++++]  ")
			print(color2)
			m = float (input("enter the m <kg\s> : "))
			cp = float (input("enter the cp <j\kg.c> : "))
			DTx = float (input("enter the DT : "))
			Q = m*cp*DTx
			if cp > 1000 :
				print(color3 + "Q = ",Q,"W")
				print(color2)
			elif cp < 1000 :
				print(color3 + "Q = ",Q,"KW")
				print(color2)
		Q1()
	elif I == "p" :
		def PR ():
			print("this function used to calculate correction factor [P and R ]")
			t1=float(input("enter temperature tube in : "))
			t2=float(input("enter temperature tube out : "))
			T1=float(input("enter temperature shell in : "))
			T2=float(input("enter temperature shell out : "))
			p = ((t2-t1)/(T1-t1))
			print (color3 + "P = ",p)
			print(color2)
			r = ((T1-T2)/(t2-t1))
			print(color3 + "R = ",r)
			print(color2)
		PR()
	elif I == "q2" :
		def Q2() :
			U = float (input("enter the U <w\m2.c> : "))
			A = float (input("enter the A <m2> : "))
			DTm = float (input("enter the DTlm : "))
			Q2 = U*A*DTm
			print(color3 + "Q = ",Q2)
			print(color3 + "Q = ",(Q2/1000),"KW")
			print(color2)
		Q2()
	elif I == "m1" :
		def mass_flow () :
			denisty = float (input("enter the denisty <kg\m3> : "))
			A = float (input("enter the A <m2> : "))
			V = float (input("enter the velocity <m\s> : "))
			mass_flow_rate = (denisty*A*V)
			print(color3 + "mass flow rate is : ",mass_flow_rate)
			print(color2)
		mass_flow()
	elif I == "m2":
		def mass_flow2 ():
			print("[+++++]before you start if you put the Q in KW put CP kj\kg.c[++++]")
			Q = float (input("enter the Q < w > : "))
			cp = float (input("enter the cp <j\kg.c> : "))
			DTx = float (input("enter the DT : "))
			mass_flow_rates = ((Q)/(cp*DTx))
			print (color3 + "the mass_flow_rate is : ",mass_flow_rates,"kg\s")
			print(color2)
		mass_flow2 ()
	else :
		print("[-]what do you want ???")


