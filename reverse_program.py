userval= int(input("please enter five digit no.:"))
val= userval%10
rev= val*10
val= (userval//10)%10

rev= (rev+val)*10
print(rev)
val= (userval//100)%10
rev= (rev+val)*10
print(rev)
val= (userval//1000)%10
rev= (rev+val)*10
print(rev)
val= (userval//10000)
rev= (rev+val)
print(rev)
