# ==========================================================
# PROGRAMA DE EQUAÇÃO 2D E 3D
# COM RELATÓRIO, GAUSS, DETERMINANTE E MÉTODO DA POTÊNCIA
# ==========================================================

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D


# ==========================================================
# ELIMINAÇÃO DE GAUSS + DETERMINANTE
# ==========================================================

def gauss_solve(A, b):
    n = len(b)

    import copy
    A = copy.deepcopy(A)
    b = copy.deepcopy(b)

    # Matriz aumentada
    for i in range(n):
        A[i].append(b[i])

    det = 1  # Determinante acumulado

    for i in range(n):

        # Pivotamento parcial
        max_row = i
        for k in range(i + 1, n):
            if abs(A[k][i]) > abs(A[max_row][i]):
                max_row = k

        # Troca de linha muda sinal do determinante
        if max_row != i:
            A[i], A[max_row] = A[max_row], A[i]
            det *= -1

        if abs(A[i][i]) < 1e-12:
            return None, 0

        pivot = A[i][i]
        det *= pivot

        # Normaliza linha
        for j in range(i, n + 1):
            A[i][j] /= pivot

        # Zera abaixo
        for k in range(i + 1, n):
            fator = A[k][i]
            for j in range(i, n + 1):
                A[k][j] -= fator * A[i][j]

    # Retrossubstituição
    x = [0] * n
    for i in range(n - 1, -1, -1):
        soma = sum(A[i][j] * x[j] for j in range(i + 1, n))
        x[i] = A[i][n] - soma

    return x, det


# ==========================================================
# MÉTODO DA POTÊNCIA PARA AUTOVALOR E AUTOVETOR
# ==========================================================

def metodo_potencia(A, iteracoes=50): 
    import math
    n = len(A)

    v = [1] * n

    for _ in range(iteracoes):
        w = [0] * n

        # Produto Av
        for i in range(n):
            for j in range(n):
                w[i] += A[i][j] * v[j]

        norma = math.sqrt(sum(w[i] ** 2 for i in range(n)))
        if norma == 0:
            return 0, v

        v = [w[i] / norma for i in range(n)]

    # Autovalor
    Av = [sum(A[i][j] * v[j] for j in range(n)) for i in range(n)]
    lambda_max = sum(v[i] * Av[i] for i in range(n))

    return lambda_max, v


# ==========================================================
# GERAÇÃO DE RELATÓRIO
# ==========================================================
def gerar_relatorio(titulo, A, det, coeficientes, lambda_max):
    with open("relatorio_equacao_da_curva.txt", "w") as arq:
        arq.write("RELATÓRIO DO PROCESSO DE EQUACAO DA CURVA\n")
        arq.write("=====================================\n\n")
        arq.write(f"Título: {titulo}\n\n")

        arq.write("Matriz do sistema (A):\n")
        for linha in A:
            arq.write(str(linha) + "\n")

        arq.write(f"\nDeterminante da matriz A: {det}\n")
        if det == 0:
            arq.write("A matriz é singular — não existe solução única.\n\n")

        arq.write("\nCoeficientes encontrados:\n")
        arq.write(str(coeficientes) + "\n\n")

        arq.write("Maior autovalor da matriz A (método da potência):\n")
        arq.write(str(lambda_max) + "\n\n")

        arq.write("Observações:\n")
        arq.write("• O sistema foi resolvido pelo método de eliminação de Gauss.\n")
        arq.write("• O determinante foi obtido multiplicando os pivôs.\n")
        arq.write("• O método da potência estimou o maior autovalor.\n")
        arq.write("• Aplicação prática em SI: Previsão de tendências em bancos de dados (2D) e calibração de sensores biométricos (3D).\n")

    print("\nRelatório gerado: relatorio_equacao_da_curva.txt\n")


# ==========================================================
# EQUAÇÃO DA CURVA 2D
# ==========================================================
def equacao_2d():
    print("\n=== EQUAÇÃO DA CURVA 2D ===")
    n = int(input("Quantos pontos? "))

    # Inserção dos pontos
    pontos = []
    for i in range(n):
        print(f"Ponto {i+1}:")
        x = float(input("x: "))
        y = float(input("y: "))
        pontos.append((x, y))
        print()

    # Monta A e b
    A = []
    b = []
    for (x, y) in pontos:
        linha = [x ** k for k in range(n)]
        A.append(linha)
        b.append(y)

    coef, det = gauss_solve(A, b)
    if coef is None:
        print("Sistema sem solução única.")
        return

    print("\nCoeficientes:")
    print(coef)

    equacao_str = "y = "
    for i in range(n-1, -1, -1):
        c = coef[i]
        if c == 0: continue
        sinal = "+" if c >= 0 and i != n-1 else ""
        grau = f"x^{i}" if i > 1 else ("x" if i == 1 else "")
        equacao_str += f" {sinal} {c:.4f}{grau}"
    print("Equação da curva: " + equacao_str)
    
    # GRÁFICO
    xs = [p[0] for p in pontos]
    ys = [p[1] for p in pontos]

    plot_x = np.linspace(min(xs), max(xs), 500)
    plot_y = [sum(coef[i] * (x ** i) for i in range(n)) for x in plot_x]

    plt.scatter(xs, ys, color="red")
    plt.plot(plot_x, plot_y)
    plt.title("Equação da Curva 2D")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid()
    plt.show()

    lambda_max, _ = metodo_potencia(A)
    gerar_relatorio("Equação da Curva 2D", A, det, coef, lambda_max)


# ==========================================================
# EQUAÇÃO DA CURVA 3D (6 pontos)
# ==========================================================

def equacao_3d():
    print("\n=== EQUAÇÃO DA CURVA 3D ===")
    print("Serão necessários 6 pontos para determinar a superfície.")

    #Inserção dos pontos
    pontos = []
    for i in range(6):
        print(f"Ponto {i+1}:")
        x = float(input("x: "))
        y = float(input("y: "))
        z = float(input("z: "))
        pontos.append((x, y, z))
        print()

    # Montagem do sistema
    A = []
    b = []
    for (x, y, z) in pontos:
        A.append([x*x, y*y, x*y, x, y, 1])
        b.append(z)

    coef, det = gauss_solve(A, b)
    if coef is None:
        print("Sistema degenerado — não existe superfície única.")
        return

    a, b2, c, d, e, f = coef

    print("\nCoeficientes:")
    print(f"a={a:.2f}, b={b2:.2f}, c={c:.2f}, d={d:.2f}, e={e:.2f}, f={f:.2f}")
    
    # Formata para mascara z = ax^2 + by^2 + ...
    geo_str = f"z = {a:.4f}x^2 + {b2:.4f}y^2 + {c:.4f}xy + {d:.4f}x + {e:.4f}y + {f:.4f}"
    # Remover sinais de +- 
    print(f"\nFomula: {geo_str}")

    # GRÁFICO 3D
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")

    xs = np.linspace(-2, 2, 50)
    ys = np.linspace(-2, 2, 50)
    X, Y = np.meshgrid(xs, ys)
    Z = a*X*X + b2*Y*Y + c*X*Y + d*X + e*Y + f

    ax.plot_surface(X, Y, Z, alpha=0.5)
    ax.scatter([p[0] for p in pontos],
               [p[1] for p in pontos],
               [p[2] for p in pontos],
               color="red")

    ax.set_title("Superfície Quadrática")
    plt.show()

    # Relátório sobre a Equação da Curva 3D
    lambda_max, _ = metodo_potencia(A)
    gerar_relatorio("Equação da Curva 3D", A, det, coef, lambda_max)


# ==========================================================
# MENU PRINCIPAL
# ==========================================================

while True:
    print("==========================================================")
    print("=============== PROGRAMA DE EQUAÇÃO 2D E 3D ==============")
    print("======== GAUSS + DETERMINANTE + MÉTODO DA POTÊNCIA =======")
    print("==========================================================")
    print("\n\n=== MENU ==============")
    print("1 - Equação da Curva 2D")
    print("2 - Equação da Curva 3D")
    print("0 - Sair")

    op = input("Escolha: ")

    if op == "1":
        equacao_2d()
    elif op == "2":
        equacao_3d()
    elif op == "0":
        break
    else:
        print("Opção inválida!")

