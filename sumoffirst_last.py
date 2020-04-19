user= int(input("please enter four digit no.\n"))
fourth = user%10

first= (user//1000)
result = (fourth+first)
print(result)