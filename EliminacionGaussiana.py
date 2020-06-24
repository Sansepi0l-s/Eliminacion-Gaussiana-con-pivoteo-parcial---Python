## Importing NumPy Library
import numpy as np
# Leer número de incógnitas
n = int(input('Ingrese el número de incógnitas: '))

# Hacer una matriz numpy de tamaño n x n + 1
a = np.zeros((n, n + 1))

# Hacer una matriz numpy de tamaño n
x = np.zeros(n)


# Reading augmented matrix coefficients
print('Ingrese coeficientes de matriz aumentada:')
for i in range(n):
    for j in range(n + 1):
        a[i][j] = float(input('a[' + str(i) + '][' + str(j) + ']='))
print("\n\nMATRIZ:")
for i in range(n):
    for j in range(n+1):
        if (j <= n - 1):
            print(a[i][j], end=" ")
        else:
            print("|", a[i][j])
# Lectura de coeficientes de matriz aumentada
for i in range(n-1):
    for p in range(i,n):
        if a[p][i] != 0.0  and p != i:
            aux=np.copy(a[i,:])
            a[i,:]=np.copy(a[p,:])
            a[p,:]=np.copy(aux)

print("\n\nMATRIZ: despues")
for i in range(n):
    for j in range(n+1):
        if (j <= n - 1):
            print(a[i][j], end=" ")
        else:
            print("|", a[i][j])

NROW = np.zeros(n)
# Paso 1
m = np.zeros((n , n+1))
for i in range(n):
    NROW[i] = i
# Paso 2
p = 0
NROW = NROW.astype(int)
for i in range(n):
    ##Encuentra el maximo de la primera columna
    z = np.max(a[NROW[i]][0])
    while(p < i ):
            ##Compara el valor absoluto
            if abs(a[NROW[p]][i]) == z:
                # Paso 4
                if a[NROW[p]][i] == 0:
                    print("No existe una solución única 1")
                    break

                # Paso 5
                ##Realiza el intercambio
                if NROW[i] != NROW[p]:
                    NCOPY = NROW[i]
                    NROW[i] = NROW[p]
                    NROW[p] = NCOPY
           
                # Paso 6
    p += 1           
                ##Operaciones entre renglones
    for j in range(i + 1, n):
          m[NROW[j]][i] = a[NROW[j]][i]/a[NROW[i]][i]
          a[j,:] =a[NROW[j],:] - m[NROW[j]][i] * a[NROW[i],:] 
            
print("\n\nMATRIZ:")
for i in range(n):
    for j in range(n+1):
        if (j <= n - 1):
            print(a[i][j], end=" ")
        else:
            print("|", a[i][j])
if a[NROW[n-1]][n - 1] == 0:
    print("No existe solucion unica 2")
else:
    x[n-1] = a[NROW[n-1]][n] / a[NROW[n-1]][n-1]
    for i in range(n-2, -1, -1):
        suma = 0
        for j in range(i + 1, n):
            suma += a[NROW[i]][j] * x[j]
            x[i] = a[NROW[i]][n] - suma
        x[i] = x[i] / a[NROW[i]][i]
    print("\nLa solucion requerida es:")
    for i in range(n):
        print('X%d = %0.2f' % (i, x[i]), end='\t')


