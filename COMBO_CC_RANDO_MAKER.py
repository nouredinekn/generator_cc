#THIS FOR MAKING COMBO CC   #BY NOUREDINE KAOINE 
#FOR  install pip
import os
try:
    from random import *
except:
    os.systeam("pip install random ")
try:
    import pyfiglet
except:
    os.system("pip install pyfiglet")
os.system("clear")
import random
import pyfiglet
#var
G = '\033[1;34;40m'
Z = '\x1b[2;31m'
NKCPTM= pyfiglet.figlet_format('NOUREDINE_KN')
print(G+NKCPTM)
x='0987654321'
H=int(input("entre how much u need to combo: "+Z))
a77='\033[1;32;40m'
hhh3=str(input("name in the txt to save combo: "))
i=1
H2=H+1
H3=(H2*3-H2)
z66=["01","02","03","04","05","06","07","08","09","10","11","12"]
z1="23456"
os.system("clear")
########bin info######INPUT#######
print("""=====4----BIN        NOT   AMERICA ======= """)
BIN1=input("1-ENTRE BIN 6 NUMBER NOT AMERICA: ")
BIN2=input("2-ENTRE BIN 6 NUMBER BUT NOT AMERICA: ")
BIN3=input("3-ENTRE BIN 6 NUMBER BUT NOT AMERICA: ")
BIN4=input("4-ENTRE BIN 6 NUMBER BUT NOT AMERICA: ")
print("""========2---BIN   AMERICA ======= """)

BIN5=input("1-ENTRE AMERICA BIN 6 NUMBER : ")
BIN6=input("2-ENTRE AMERICA BIN 6 NUMBER : ")
BIN7=input("3-ENTRE AMERICA BIN 6 NUMBER : ")
print("""==≈==== ENTRE BIN 12 NUMBER NOT AMERICA   """)
BIN8=input("1-ENTRE BIN 12 NUMBER NOT AMERICA : ")
BIN9=input("1-ENTRE BIN 12 NUMBER NOT AMERICA : ")


# 6 number without america

PPP2=[BIN1,BIN2,BIN3,BIN4]
###### bin info#####6 but AMERICA
PPP3=[BIN5,BIN6,BIN7]
#### bin info 12 NUM####
PPP4= [BIN8,BIN9]
####################
os.system("clear")
print("""  -------------------------------------------------
------------------>  1- DATE RANDOM
------------------>  2- DATE  NOT RANDOM  
-------------------------------------------------         nouredine_kn""")
DATE=int(input("ENTRE 1 OR 2: "))

if DATE==2 :
	print(""" example 2024 .....""")
	DATE2=str(input("enter your years: "))
else:
	pass
zz=open(hhh3+"[NOUREDINE_KAOINE]"+".txt","w")	

while i<H3 :
	GN1=str("".join(random.choice(PPP2)for i in range(1))) 
	GN2=str("".join(random.choice(PPP3)for i in range(1))) 
	GN3=str("".join(random.choice(PPP4)for i in range(1))) 
	zzz=str("".join(random.choice(x)for i in range(10))) 
	zz2=str("".join(random.choice(z1)for i in range(1))) 
	zz4=str("".join(random.choice(z66)for i in range(1))) 
	z88=str("".join(random.choice(x)for i in range(3))) 
	z99=str("".join(random.choice(x)for i in range(4))) 
	y= GN1+zzz
	y2=GN2+zzz
	y3=GN3+z99
	zz3="202"+z1
	if DATE==2:
	    	wh=y+"|"+zz4+"|"+DATE2+"|"+z88
	    	wh2=y2+"|"+zz4+"|"+DATE2+"|"+z99
	    	wh3=y3+"|"+zz4+"|"+DATE2+"|"+z88
	else:
		wh=y+"|"+zz4+"|"+zz3+"|"+z88
		wh2=y2+"|"+zz4+"|"+zz3+"|"+z99
		wh3=y3+"|"+zz4+"|"+zz3+"|"+z88
	zz.write(wh+"\n"+wh2+"\n"+wh3+"\n")
	print(a77+wh)
	print(a77+wh2)
	print(a77+wh3)
	i +=1
	
