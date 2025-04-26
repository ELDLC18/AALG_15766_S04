def busqueda_iterativa(lista, dato):
    inicio = 0
    fin = len(lista) - 1
    
    while inicio+1 < fin:
        medio = (inicio + fin) // 2
       
        if lista[medio] == dato:
            return medio
        elif lista[medio] < dato:
            inicio = medio 
        else:
            fin = medio
    if lista[inicio] == dato:
        return inicio 
    if lista[fin] == dato:
        return fin
    return -1

def busqueda_recursiva(lista, inicio, fin, dato):
    if inicio > fin:
        return -1
    medio=(inicio + fin)//2
    if lista[medio]==dato:
        return medio
    elif lista[medio] < dato:
        return busqueda_recursiva(lista, medio + 1, fin, dato)
    else:
        return busqueda_recursiva(lista, inicio, medio - 1, dato)



lista = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]    

for i in range(0,22):
    print(i, busqueda_iterativa(lista,i))
    print(f"\t{i, busqueda_recursiva(lista, 0, len(lista)-1,i)}")