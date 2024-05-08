from gauss_jordan import gauss_jordanv2, mostrar_matriz
from optimizar import optimizar_resultado


matriz_barcazas = [
      [50, 20, 40, 4500],
      [30, 50, 30, 4400],
      [40, 50, 60, 5800]
        ] 
matriz_5barcazas = [
  [50, 20, 40, 40, 20, 4500],
  [30, 50, 30, 20, 60, 4400],
  [40, 50, 60, 10, 30, 5800]
]

gauss_jordanv2(matriz_barcazas)
mostrar_matriz(matriz_barcazas)
resultado = optimizar_resultado(matriz_barcazas)
print(resultado)
