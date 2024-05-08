from scipy.optimize import linprog

def optimizar_resultado(matriz):
    """ 
    Optimizar la funcion f = x1 + x2 + ... + xn basado en un sistema
    de ecuaciones con n variables
    Parametros:
        matriz: list[list[float]]: reprecentacion matriacial del sitema Ax = b
    Retorno:
        res.x: list[int]: Aqulla solucion del tipo (x1, x2, ... , xn) que
        mininmiza la suma de las variables
    
    """
    filas = len(matriz)
    cols = len(matriz[0])
    c = [] #coeficientes de la funcion obejetivo
    for _ in range(cols - 1):
        c.append(1)

    A_eq = [] #array bidimensional con los coefientes de las variables
    b_eq = [] #array unidimensional con los terminos independientes, vector b

    for i in range(filas):
        coeficientes_var = []
        terminos_ind = []
        for j in range(cols):
            if j != cols - 1:
                coeficientes_var.append(matriz[i][j])
            else:
                terminos_ind.append(matriz[i][j])

        A_eq.append(coeficientes_var)
        b_eq.append(terminos_ind)
    
    bounds = [(0, None)] #Restriccion para el valor de las variables 
    try:
        res = linprog(c=c, A_eq=A_eq, b_eq=b_eq, bounds=bounds, integrality=1)
        return res.x
    except ValueError:
        print("Error al optimizar")
        return 0



if __name__ == "__main__":
    #estas son solo pruebas, para optimizar resultado importar la funcion de arriba
    c = [1, 1, 1, 1, 1]
    c2 = [-1, -1, -1, -1, -1]

    A_eq = [
        [1, 0, 0, 1.44, 0.83],
        [0, 1, 0, 0.02, 1.47],
        [0, 0, 1, -0.82, -1.28]
    ]

    A_ub = [
        [-1, 0, 0, -1.44, -0.83],
        [0, -1, 0, -0.02, -1.47],
        [0, 0, -1, 0.82, 1.28]
    ]

    b_eq = [
        50,
        40,
        30
    ]

    b_ub = [
        -50,
        -40,
        -30
    ]

    bounds = [(0, None)]

    #res = linprog(c=c ,A_ub=A_ub, b_ub=b_ub, bounds=bounds)
    res = linprog(c=c, A_eq=A_eq, b_eq=b_eq, A_ub=A_ub, b_ub=b_ub,bounds=bounds, integrality=1)
    #res2 = linprog(c=c, A_eq=A_eq, b_eq=b_eq, A_ub=A_ub, b_ub=b_ub,bounds=[(10, None)])
    #res3 = linprog(c=c2, A_eq=A_eq, b_eq=b_eq, bounds=bounds, )
    #res4 = linprog(c=c, A_ub=A_ub, b_ub=b_ub, bounds=[(0,None)], integrality=1)
    #res4 = linprog(c=c, A_ub=A_ub, b_ub=b_ub, bounds=[(0,None)], integrality=1)
    res4 = linprog(c=c, A_ub=A_eq, b_ub=b_eq, bounds=[(0,None)], integrality=1)
    res5 = linprog(c=c2, A_ub=A_eq, b_ub=b_eq, bounds=bounds, integrality=1)
    res6 = linprog(c=c, A_ub=A_ub, b_ub=b_ub, bounds=[(0, None)])
    print(res.x)
    print(res6.x)
