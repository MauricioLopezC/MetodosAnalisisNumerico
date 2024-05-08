def gauss_jordanv2(matriz: list[list[float]]) -> None:
    filas = len(matriz)
    columnas = len(matriz[0])
    for e in range(filas):
        divisor = matriz[e][e]

        if divisor == 0 and e != filas - 1:
            aux = matriz[e]
            matriz[e] = matriz[e+1]
            matriz[e+1] = aux
            divisor = matriz[e][e] #actualizamos al nuevo divisor
        elif divisor == 0 and e == filas - 1:
            if matriz[e][filas] == 0:
                print("sistema con infinitas soluciones")
                break
            if matriz[e][filas] != 0:
                print("Sistema incosistente, conjunto solucion vacio")
                break


        for j in range(e, columnas):
            if (divisor != 0):
                matriz[e][j] = matriz[e][j] / divisor #normalizamos fila e
            else:
                print("valio madre")

        #reducimos las otras columnas en la posicion e
        for i in range(filas):
            multiplo = matriz[i][e]
            for j in range(e, columnas):
                if (i != e):
                    matriz[i][j] = matriz[i][j] - multiplo * matriz[e][j] 
                    #elemento - multiplo * elemento fila e 


def mostrar_matriz(matriz: list[list[float]]):
    for fila in matriz:
        print(fila)

def obtener_col(matriz:list[list[float]]):
    columna = []
    filas = len(matriz)
    for i in range(filas):
        columna.append(matriz[i][filas])
    return columna 

if __name__ == "__main__":
    # ejemplo con una solucion (x,y,z)
    matriz = [
            [0, 3, 6, 1],
            [2, 5, 2, 10],
            [1, 4, 2, 6]
            ]
    #ejemplo de infinitas soluciones (x,y,z)
    matriz2 = [ 
            [1, 2, 3, 9],
            [4, 5 ,6 ,24],
            [2, 7, 12, 30]
            ]

    #ejempo sin solucion
    matriz3 = [
            [0, 2, 3, 4],
            [2, -6, 7, 15],
            [1, -2, 5, 10]
            ]

    matriz4 = [
      [50, 20, 40, 40, 20, 4500],
      [30, 50, 30, 20, 60, 4400],
      [40, 50, 60, 10, 30, 5800]
    ]

    gauss_jordanv2(matriz)
    mostrar_matriz(matriz)
    print()
