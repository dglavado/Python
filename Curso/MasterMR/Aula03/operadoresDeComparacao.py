num1 = 5
num2 = "5"

print(num1 == int(num2)) #true
print(str(num1) == num2) #true
print(num1 == float(num2)) #true

print(num1 == num2) #False - tipos diferentes - Não faz nenhuma conversão automática
print(num1 != num2) #True

#Não é possível comparar com tipos diferentes
#print(num1 > num2) 
#print(num1 >= num2)
#print(num1 < num2)
#print(num1 <= num2)

num2 = int(num2)
print(num1 == num2) #True - convertido para mesmo tipo
print(num1 != num2) #False

print(num1 > num2) #False
print(num1 >= num2) #True
print(num1 < num2) #False
print(num1 <= num2) #True


num1 = str(num1)
num2 = str(num2)

print(num1 > num2) #False - Mesmo sendo string, é possível comparar numericamente
print(num1 >= num2) #True

print("6" > "5") #True




