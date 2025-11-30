### Resumo

Este projeto consiste em uma ferramenta computacional desenvolvida em Python para realizar a interpolação exata de pontos em espaços bidimensionais (2D) e tridimensionais (3D). O software calcula a equação matemática precisa (polinomial para 2D ou quadrática para 3D) que conecta um conjunto de coordenadas fornecidas. Além do cálculo algébrico via resolução de sistemas lineares, o sistema realiza verificações de consistência (invertibilidade da matriz) para detectar pontos degenerados, gera visualizações gráficas das curvas ou superfícies resultantes e exporta um relatório técnico detalhando o processo.

-----

# Interpolador de Curvas e Superfícies via Sistemas Lineares

## Descrição do Projeto

Este repositório armazena uma solução algorítmica para problemas de interpolação em Geometria Analítica e Álgebra Linear Computacional. O programa é capaz de receber um conjunto arbitrário de coordenadas e determinar a função matemática exata que descreve a curva ou superfície que passa por todos os pontos especificados.

O sistema opera diferenciando automaticamente a modelagem baseada na dimensionalidade dos dados de entrada:

  * Caso 2D: Ajuste de um polinômio de grau $n$ (onde $n$ é derivado do número de pontos menos 1).
  * Caso 3D: Ajuste de uma superfície baseada em um modelo quadrático geral (cônicas/quádricas).

## Funcionalidades

O software foi estruturado para cumprir rigorosamente as seguintes etapas de processamento:

1.  Entrada de Dados: Interface para inserção de coordenadas de pontos no plano cartesiano $(x, y)$ ou no espaço euclidiano $(x, y, z)$.
2.  Modelagem Matemática: Construção dinâmica das equações baseada nos modelos predeterminados.
3.  Validação de Solvabilidade: Verificação da invertibilidade da matriz de coeficientes. O sistema alerta sobre "pontos degenerados" caso o determinante da matriz seja nulo ou a matriz seja singular, indicando que não há solução única para o conjunto de pontos dado.
4.  Visualização Gráfica: Geração de gráficos interativos utilizando matplotlib, plotando simultaneamente os pontos originais (discretos) e a curva/superfície calculada (contínua).
5.  Relatório Técnico: Geração automática de um arquivo de texto explicando o processo, exibindo a matriz montada e a equação final.

## Fundamentação Teórica

O núcleo do projeto baseia-se na resolução de um sistema de equações lineares da forma $A \cdot x = B$, onde $A$ é a matriz construída a partir das coordenadas dos pontos (variáveis independentes) e $x$ é o vetor de coeficientes da equação alvo.

### Modelo 2D (Polinomial)

Para $n+1$ pontos, buscamos um polinômio de grau $n$:
$$P(x) = a_0 + a_1x + a_2x^2 + \dots + a_nx^n$$

Isso resulta em um sistema linear onde a matriz $A$ assume a forma de uma Matriz de Vandermonde.

### Modelo 3D (Superfície Quadrática)

Para pontos no espaço, o modelo geral de segunda ordem utilizado é:
$$z = Ax^2 + By^2 + Cxy + Dx + Ey + F$$
Necessitando de um mínimo de 6 pontos para determinar unicamente os 6 coeficientes, assumindo não haver degeneração (como pontos coplanares em configurações específicas).

## Pré-requisitos e Instalação

Para executar este projeto, é necessário ter o Python 3 instalado, juntamente com as bibliotecas de computação numérica e visualização.

1.  Clone o repositório:

    bash
     git clone https://github.com/KethelynAlves/-Projeto-Curvas-e-Superficies-por-Pontos-Especificados
    

2.  Instale as dependências:

    bash
    pip install numpy matplotlib
    

## Como Usar

Execute o arquivo principal do projeto:

bash
python SPOMVAL-MAISCOMPLEXO.py


Siga as instruções no terminal para escolher a dimensão (2 ou 3) e inserir a quantidade e as coordenadas dos pontos.

### Exemplo de Entrada (2D)

Para gerar uma parábola simples $y = x^2$:

  * Ponto 1: (-1, 1)
  * Ponto 2: (0, 0)
  * Ponto 3: (1, 1)

### Exemplo de Entrada (3D)

Para gerar um paraboloide circular $z = x^2 + y^2$:

  * Ponto 1: (0,0,0)
  * Ponto 2: (1,0,1)
  * Ponto 3: (-1,0,1)
  * Ponto 4: (0,1,1)
  * Ponto 5: (0,-1,1)
  * Ponto 6: (1,1,2)

## Tecnologias Utilizadas

  * Python 3: Linguagem base.
  * NumPy: Para manipulação de arrays multidimensionais e resolução de sistemas lineares (numpy.linalg.solve).
  * Matplotlib: Para plotagem de gráficos 2D e renderização de superfícies 3D (mpl_toolkits.mplot3d).

## Autores

Desenvolvido por:

Kethelyn Alves dos Santos

Vinícius Tiago de Santana

Rafael Teixeira Paulino
