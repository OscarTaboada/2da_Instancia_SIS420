#!/usr/bin/env python
# coding: utf-8

import random

# ================================================
# Implementación clase abstracta algoritmo genético 
# ================================================
# Definir clase abstracta Problema_Genetico 
# Propiedades:
# - genes: lista de genes usados en el genotipo de los estados.
# - longitud_individuos: longitud de los cromosomas
# Métodos:
# - decodifica: función de obtiene el fenotipo a partir del genotipo.
# - fitness: función de valoración.
# - muta: mutación de un cromosoma 
# - cruza: cruce de un par de cromosomas

# En la definición de clase no se especifica si el problema es
# de maximización o de minimización, esto se hace con el
# parámetro en el algoritmo genético que se implemente.

class Problema_Genetico(object):
    # Constructor
    def __init__(self, genes, fun_decodificar, fun_cruzar, fun_mutar, fun_fitness, longitud_individuos):
        self.genes = genes
        self.fun_decodificar = fun_decodificar
        self.fun_cruzar = fun_cruzar
        self.fun_mutar = fun_mutar
        self.fun_fitness = fun_fitness
        self.longitud_individuos = longitud_individuos
    
    def decodificar(self, genotipo):
        #Devuelve el fenotipo a partir del genotipo
        fenotipo = self.fun_decodificar(genotipo)
        return fenotipo
    
    def cruzar(self, cromosoma1, cromosoma2):         
        #Devuelve el cruce de un par de cromosomas
        cruce = self.fun_cruzar(cromosoma1, cromosoma2)
        return cruce 
    
    def mutar(self, cromosoma, prob):
        #Devuelve el cromosoma mutado
        mutante = self.fun_mutar(cromosoma, prob)
        return mutante

    
    # Si se quisiera implementar otro mecanismo de cruza
    #def cruza_loca(self, cromosoma1, cromosoma2, cromosoma3, cromosoma4):
    #    cruce = self.fun_cruza(cromosoma1, cromosoma2, cromosoma3, cromosoma4)
    #    return cruce

    def fitness(self, cromosoma):
        #Función de valoración
        valoracion = self.fun_fitness(cromosoma)
        return valoracion


# Función interpreta lista de 0's y 1's como número natural:  

def binario_a_decimal(x):
    return sum(b * (2 ** i) for (i, b) in enumerate(x)) 

# con cuad_gen, se prueba alguna de las funciones definidas en la
# clase anterior, para esta instancia concreta. Por ejemplo:
# cuad_gen.decodifica([1,0,0,0,1,1,0,0,1,0,1])
# 1329
# cuad_gen.fitness([1,0,0,0,1,1,0,0,1,0,1])
# 1766241
# cuad_gen.muta([1,0,0,0,1,1,0,0,1,0,1],0.1)
# [1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1]
# cuad_gen.muta([1,0,0,0,1,1,0,0,1,0,1],0.1)
# [0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1]
# cuad_gen.cruza([1,0,0,0,1,1,0,0,1,0,1],[0,1,1,0,1,0,0,1,1,1])
# [[1, 0, 0, 0, 1, 0, 0, 1, 1, 1], [0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1]]

def fun_cruzar(cromosoma1, cromosoma2):
    # Cruza los cromosomas por la mitad
    l1 = len(cromosoma1)
    l2 = len(cromosoma2)
    cruce1 = cromosoma1[0:int(l1 / 2)]+cromosoma2[int(l1 / 2):l2]
    cruce2 = cromosoma2[0:int(l2 / 2)]+cromosoma1[int(l2 / 2):l1]
    return [cruce1, cruce2]

def fun_mutar(cromosoma,prob):
    # Elige un elemento al azar del cromosoma y lo modifica con una probabilidad igual a prob
    l = len(cromosoma)
    p = random.randint(0, l - 1)
    if prob <= random.uniform(0, 1):
        cromosoma[p] =  (cromosoma[p] + 1) % 2
        #cromosoma[p] = cromosoma[p]*-1
    return cromosoma

def decodificar_x(x):
    # return [binario_a_decimal(x[:4]), binario_a_decimal(x[4:])] 
    return x

# Definir una función poblacion_inicial(problema_genetico, tamaño), para
# definir una población inicial de un tamaño dado, para una instancia dada de
# la clase anterior Problema_Genetico

def poblacion_inicial(problema_genetico, size):
    l = []
    for i in range(size):
        l.append([random.choice(problema_genetico.genes) for i in range(problema_genetico.longitud_individuos)])
        
    # for i in range(size):
    #     m = []
    #     for i in range(problema_genetico.longitud_individuos):
    #         l.append([random.choice(problema_genetico.genes)
    #     l.append(m)
    return l



# Definir una función cruza_padres(problema_genetico, padres), que recibiendo
# una instancia de Problema_Genetico y una población de padres (supondremos
# que hay un número par de padres), obtiene la población resultante de
# cruzarlos de dos en dos (en el orden en que aparecen)

def cruza_padres(problema_genetico, padres):
    l = []
    l1 = len(padres)
    while padres != []:
        l.extend(problema_genetico.cruzar(padres[0], padres[1]))
        padres.pop(0)
        padres.pop(0)
    return l



# Definir una función muta_individuos(problema_genetico, poblacion, prob), que
# recibiendo una instancia de Problema_Genetico, una población y una
# probabilidad de mutación, obtiene la población resultante de aplicar
# operaciones de mutación a cada individuo. 

def muta_individuos(problema_genetico, poblacion, prob):
    return [problema_genetico.mutar(individuo, prob) for individuo in poblacion]


# Definir una función 
# seleccion_por_torneo(problema_genetico,poblacion,n,k,opt)
# que implementa la selección mediante torneo de n individuos de una
# población.  Esta función recibe como entrada una instancia de
# Problema_Genetico, una población, un número natural n (número de individuos
# a seleccionar) un número natural k (número de participantes en el torneo) y
# un valor opt que puede ser o la función max o la función min (dependiendo de
# si el problema es de maximización o de minimización, resp.).

# INDICACIÓN: Usar random.sample 

def seleccion_por_torneo(problema_genetico, poblacion, n, k, opt):
    # Selección por torneo de n individuos de una población. Siendo k el nº de participantes
    # y opt la función max o min.
    seleccionados = []
    for i in range(n):
        participantes = random.sample(poblacion, k)
        seleccionado = opt(participantes, key = problema_genetico.fitness)
        #opt(poblacion, key = problema_genetico.fitness)
        seleccionados.append(seleccionado)
        # poblacion.remove(seleccionado)
    return seleccionados  



def nueva_generacion_t(problema_genetico, k, opt, poblacion, n_padres, n_directos, prob_mutar):
    padres2 = seleccion_por_torneo(problema_genetico, poblacion, n_directos, k, opt) 
    padres1 = seleccion_por_torneo(problema_genetico, poblacion, n_padres , k, opt)
    cruces =  cruza_padres(problema_genetico,padres1)
    generacion = padres2 + cruces
    resultado_mutaciones = muta_individuos(problema_genetico, generacion, prob_mutar)
    return resultado_mutaciones



# La siguiente función algoritmo_genetico_t implementa el primero de los
# algoritmos genéticos (el de selección por torneo)

def algoritmo_genetico_t(problema_genetico, k, opt, ngen, size, prop_cruces, prob_mutar):
    poblacion = poblacion_inicial(problema_genetico, size)
    print("Poblacion Inicial")
    for n, i in enumerate(poblacion):
            print(f"grupo: {n}, {i}")
    # print(poblacion)
    n_padres = round(size * prop_cruces)
    n_padres = int (n_padres if n_padres % 2 == 0 else n_padres - 1)
    n_directos = size - n_padres
    for _ in range(ngen):
        poblacion = nueva_generacion_t(problema_genetico, k, opt, poblacion, n_padres, n_directos, prob_mutar)
        print("Nueva población")
        
        for n, i in enumerate(poblacion):
            print(f"Grupo: {n}, {i}")
        # print(poblacion)

        # for ind in poblacion:
        #     if(problema_genetico.fitness(ind) == 0):
        #         print("La solucion es: ")
        #         print(ind)
        #         break

    mejor_cr = opt(poblacion, key = problema_genetico.fitness)
    mejor = problema_genetico.decodificar(mejor_cr)
    return (mejor, problema_genetico.fitness(mejor_cr)) 

# Argumentos de entrada:
# * problema_genetico: una instancia de la clase Problema_Genetico, con el
#   problema de optimización que se quiere resolver.
# * k: número de participantes en los torneos de selección.
# * opt: max ó min, dependiendo si el problema es de maximización o de
#   minimización. 
# * ngen: número de generaciones (condición de terminación)
# * tamaño (size): número de individuos en cada generación
# * prop_cruces: proporción del total de la población que serán padres. 
# * prob_mutar: probabilidad de realizar una mutación de un gen.

# Se pide definir la única función auxiliar que queda por definir en el
# algoritmo anterior; es decir, la función
# nueva_generacion_t(problema_genetico, opt ,poblacion, n_padres, prob_mutar)
# que a partir de una población dada, calcula la siguiente generación.

# Una vez definida, ejecutar el algoritmo genético anterior, para resolver el
# problema cuad_gen (tanto en minimización como en maximización).

# 
# # ==================================================
# Representación del problema de la ecuacion y = a + bx1 + cx2
# donde se buscan valores para x1 y x2 que cumplan con lo siguiente:
# 3 = 2 -1(x1) + 1(x2)
# y = a + bx1 + cx2
# ===================================================


def fun_fitnnes_ecuacion(cromosoma):

    tiempo = 30
    cancha = random.randint(1, 5)

    x1 = binario_a_decimal(cromosoma[:2])
    x2 = binario_a_decimal(cromosoma[2:4])
    x3 = binario_a_decimal(cromosoma[4:6])
    x4 = binario_a_decimal(cromosoma[6:8])
    x5 = binario_a_decimal(cromosoma[8:10])
    x6 = binario_a_decimal(cromosoma[10:12])
    nro_cancha = cancha
    #
    # x1 = binario_a_decimal(cromosoma[:12])
    if(x1 == 3 ):
        x1 = tiempo
    else:
        x1 = 0
    if(x2 == 3 ):
        x2 = tiempo
    else:
        x2 = 0

    if(x3 == 3 ):
        x3 = tiempo
    else:
        x3 = 0

    if(x4 == 3 ):
        x4 = tiempo
    else:
        x4 = 0

    if(x5 == 3 ):
        x5 = tiempo
    else:
        x5 = 0

    if(x6 == 3 ):
        x6 = tiempo
    else:
        x6 = 0
    fitnnes = (x1+x2+x3+x4+x5+x6)

    # fitnnes = abs(x1 - 2730)
    # print("x1:{0}, x2:{1}, fitnnes:{2}".format(x1, x2, fitnnes))
    print("partido1:{0}, partido2:{1}, partido3:{2}, partido4:{3}, partido5:{4}, partido6:{5}, cancha Nro{6}, tiempo:{7} min".format(x1, x2, x3, x4, x5, x6, nro_cancha, fitnnes))
    # fitnnes = Total_Tiempo
    # print("Dias:{0}".format(fitnnes))
    # print("totalPartidos:{0}, fitnnes:{1}".format(x1, fitnnes))

    return fitnnes



ecua_gen = Problema_Genetico([0, 1], decodificar_x, fun_cruzar, fun_mutar, fun_fitnnes_ecuacion, 12)


algoritmo_genetico_t(ecua_gen, 2, min, 0, 16, 0.5, 0.1)









