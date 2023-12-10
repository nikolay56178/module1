a= int(input("Введите первое число:"))
b= int(input("Введите второе число:"))
c= int(input("Введите третье число:"))

if (a==b) and (b==c) and (c==a):
	print (3)
elif (a==b) | (b==c) | (c==a):
	print (2)

else:
	print (0)