Numbers= int(input("Enter five digit number"))
#rem= (Numbers%10)
sum=(Numbers%10)+((Numbers/1000)%10)+((Numbers/100)%10)+((Numbers/10)%10)
print(round(sum))
