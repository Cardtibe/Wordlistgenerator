import os
print('''
 __    __   ___   ____   ___    ____   ___   __    __    ___  ____  
|  |__|  | /   \ |    \ |   \  |    \ /   \ |  |__|  |  /  _]|    \ 
|  |  |  ||     ||  D  )|    \ |  o  )     ||  |  |  | /  [_ |  D  )
|  |  |  ||  O  ||    / |  D  ||   _/|  O  ||  |  |  ||    _]|    / 
|  `  '  ||     ||    \ |     ||  |  |     ||  `  '  ||   [_ |    \ 
 \      / |     ||  .  \|     ||  |  |     | \      / |     ||  .  \.
  \_/\_/   \___/ |__|\_||_____||__|   \___/   \_/\_/  |_____||__|\__|

CardTibe//                                                           
help for 'help'
''')
cod=input(": ")
if cod=="help":
	print('''
file word1; word2; word3; -s3 -b -n -m -a8

file file    name
word1,2,3... words
-s1,2,3      len(number) include
-b 	     uppercase letter include
-n           "-._" include
-m           frequently used password include
-a           len(password)
''')
	cod=input(": ")
codp=cod.split(" ")
del cod
nl="_-."
filew=""
kelime=[]
params=[]

#inputu kelime params filew ya ayır
for i in codp:
	if i.find(";")!=-1:
		kelime.append(i)
	elif i.find("-")!=-1:
		params.append(i)
	else:
		filew=i

filew=filew.strip()
print(filew)

def kbt(x):
	r=[]
	r.append(x.title())
	r.append(x.upper())
	r.append(x)
	return r
def nek(x):
	r=[]
	for i in range(0,len(nl)):
		r.append(x+nl[i])
	return r

kkelime=[]
ck=""
for i in range(0,len(kelime)):
	for c in kelime[i]:
		if c!=";":
			ck+=c
	kkelime.append(ck)
	ck=""
kelime=kkelime	
del kkelime
b=0
s=0
n=0
m=0
a=0
for i in params:
	if i.find('-b')!=-1:
		b=1
	if i.find('-n')!=-1:
		n=1
	if i.find('-m')!=-1:
		m=1
	for ap in range(5,12):
		if i.find('-a'+str(ap))!=-1:
			a=ap
	for si in range(1,11):
		if i.find('-s'+str(si))!=-1:
			s=si
del params
if m==1:
	bets=open("best.txt","r")
	best=bets.readlines()
	bets.close()
dosya=open(filew,"w")
tkk=[]
enlist=[]
if b==1: 
	for i in kelime:
		enlist+=kbt(i)
else:
	enlist=kelime[:]
del kelime
tkk=enlist[:]
if n==1:
	for i in range(0,len(tkk)):
		enlist+=(nek(tkk[i]))

tkk=enlist[:]
iks=enlist[:]
def sayi(x,p):
	r=[]
	for i in range(0,10**p+1):
		r.append(x+str(i))
	return r
for i in tkk:
	enlist+=(sayi(i,s))
kiks=enlist[:]

del tkk

for i in range(0,len(iks)):
	for si in range(0,len(kiks)):
		suan=iks[i]+kiks[si]
		if len(suan)>=a:
			dosya.write(suan+"\n")
for i in best:
	dosya.write(i)
del iks
del kiks
for i in range(0,len(enlist)):
	if len(enlist[i])>=a:
		dosya.write(enlist[i]+"\n")
print("Words :"+str(len(enlist)))





