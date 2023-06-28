import os

listaCodigos = [1001,1002,1003]
listaNombres = ['NERON','GRAN ESPANTAPAJAROS','MIU']
listaEspecies = ['PERRO','PERRO','GATO']
listaEdades = [3,6,1]

menu = '''
        MENU
    1. Ingresar Mascotas
    2. Mostrar lista completa
    3. Buscar x especie
    0. Salir
    Digite opcion: '''

def agregarMascota():
    print("Ingresando datos de la mascota:")
    # validacion codigo > 0
    while True:
        try:
            codigo = int(input("codigo: "))
            if codigo > 0: #condicion de termino
                listaCodigos.append(codigo)
                break
            else:
                print("error, codigo debe ser mayor que cero")
        except:
            print("excepcion de codigo")
    #end while codigo    
    # validacion nombre mínimo 2 caracteres
    while True:
        try:
            nombre = input("nombre: ")
            if len(nombre) >= 2:
                listaNombres.append(nombre)
                break
            else:
                print("Error, nombre debe tener a lo menos 2 characteres")
        except:
            print("excepcion de nombre")
    #endwhile nombre
    while True:
        try:
            especie = input("especie: ")
            if len(especie) >= 2:
                listaEspecies.append(especie)
                break
            else:
                print("Error, nombre debe tener a lo menos 2 characteres")
        except:
            print("excepcion de nombre")
    #endwhile nombre
    while True:
        try:
            edad = int(input("edad: "))
            if edad > 0: #condicion de termino
                listaEdades.append(edad)
                break
            else:
                print("error, codigo debe ser mayor que cero")
        except:
            print("excepcion de codigo")
    #end while codigo    

def listarMascotas():
    print("opcion 2")
    print(" LISTADO GENERAL DE MASCOTAS \n")
    print("N°| CODiGO | NOMBRE               | ESPECIE    |EDAD| VACUNARSE")
    print("--+--------+----------------------+------------+----+----------")
    contVacunas = 0
    for i in range(len(listaCodigos)):
        if listaEdades[i] >= 3:
            vacuna = "SI"
            contVacunas += 1
        else:
            vacuna = "NO"
        print(f"{i+1} | {listaCodigos[i]:6d} | {listaNombres[i]:20s} | {listaEspecies[i]:10s} | {listaEdades[i]:2d} | {vacuna}")
        print("--+--------+----------------------+------------+----+----------")
    print(f"TOTAL DE MASCOTAS: {i+1}")
    print(f"CANTIDAD DE MASCOTAS QUE DEBEN VACUNARSE: {contVacunas}")

def buscarEspecie():
    print("opcion 3")
    especie = input("especie a mostrar: ")
    print(f" LISTADO ESPECIE: {especie} \n")
    print("N°| CODiGO | NOMBRE               | ESPECIE    |EDAD| ")
    print("--+--------+----------------------+------------+----+-")
    for i in range(len(listaCodigos)):
        if especie.lower() == listaEspecies[i].lower():
            print(f"{i+1} | {listaCodigos[i]:6d} | {listaNombres[i]:20s} | {listaEspecies[i]:10s} | {listaEdades[i]:2d} |")
            print("--+--------+----------------------+------------+----+----------")

#programa principal o main
while True:
    try:
        opc = int(input(menu))
        if opc == 0:
            break
        elif opc == 1:
            agregarMascota()
        elif opc == 2:
            listarMascotas()
        elif opc == 3:
            buscarEspecie()
        else:
            print("opcion incorrecta")
    except:
        print("Excepcion de menu")
# endwhile

