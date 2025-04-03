#Limite: 127
#print(str("123.50".replace(".","").replace(".", "")).isnumeroc()).replace(True, "OK")

print(f"123.50".replace(".","").isnumeric()) #True
print(f"123,50".isnumeric()) #False
print("123.50".isnumeric()) #False

print(str("123.50".replace(".","").isnumeric()).replace("True", "OK")) #OK