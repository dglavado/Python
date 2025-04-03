print("Hello, World!")

def pow(n, p):
  ret = 1
  for i in range(p):
    ret = ret*n
  return ret
  
print(f"2^0 = {pow(2,0)}")
print(f"2^1 = {pow(2,1)}")
print(f"2^2 = {pow(2,2)}")
print(f"2^3 = {pow(2,3)}")
print(f"2^4 = {pow(2,4)}")
