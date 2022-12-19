
repetir = int(input())
while (repetir >100 or repetir < 1):
    repetir = int(input())
n = 1

array = [repetir]
for i in range(0,repetir):
    array.append([])

for i in range(0,repetir):
    palabra = input()
    array[i] = palabra

for i in range (0,repetir):
    valor = len(array[i])
    cadena = str(len(array[i])-2)
    if(valor > 10):
        print(array[i][:n]+cadena+array[i][-n:])
    else:
        print(array[i])
