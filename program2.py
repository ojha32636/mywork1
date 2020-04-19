distance = int(input("Enter distance in KM from dewas to indore Is:"))
mtr = 1000
feet =3.28
inches = 12
cm= 2.54
print( "in KM is\t"+ str(distance))
meter = (distance*mtr)

print("in MTR is\t"+str( meter))
Df=(meter*feet)

print("in FT is\t"+str(Df))


Dinches = (Df*inches)
print("in INC is\t"+ str(Dinches))

dcm=(Dinches*cm)
print("In CM is\t"+str(dcm))

#print("distance in km is" distance +"\n distance in MTR is" meter +"\n distance in FT is" Df+"\n distance in InC is" Dinches +" istance in CM is" dcm )