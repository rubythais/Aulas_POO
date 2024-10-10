import math
print ("Digite a base e a altura do retângulo")
b = float(input())
h = float(input())
area = b*h
peri = (b*2)+(h*2)
diag = math.sqrt((b**2)+(h**2))
print("Área =", area, " - Perímetro = ", peri, " - Diagonal = ", diag)