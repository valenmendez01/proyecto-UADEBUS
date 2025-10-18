"""Sistema de Venta de Pasajes
Implementar un sistema que gestione las ventas de pasajes de micro a distintos
destinos y en diferentes fechas, utilizando matrices, listas y diccionarios para man-
tener la información. Esta debe almacenarse en archivos para permitir su posterior
recuperación. Aplicar GIT para control de versiones y recursividad para realizar las búsquedas."""

import time, random, json, colorama
from colorama import Fore

# Inicializar colorama
# autoreset=True Significa que después de imprimir un texto con un color, el formato de color se
# restablecerá automáticamente al valor predeterminado
colorama.init(autoreset=True)

# Funciones

def leerTarjeta(codigo, lastname):
    try:
        arch = open("reservas.txt", "rt")
        encontrada = False
        reservas_encontradas=[]
        for registro in arch:
            tarjeta = registro.strip().split(";")
            if tarjeta[0] == codigo and tarjeta[1] == lastname:
                encontrada = True
                reservas_encontradas.append(tarjeta)
                
        if encontrada == False:
            print(f"\n{Fore.RED}❌ {Fore.WHITE}Reserva no encontrada o datos incorrectos.")
            print("."*27)
            return ""
        else:
            return reservas_encontradas

    except FileNotFoundError:
        print(f"\n{Fore.RED}❌ {Fore.WHITE}Archivo no encontrado")
        print("."*27)
    except OSError:
        print(f"\n{Fore.RED}❌ {Fore.WHITE}Error al abrir el archivo")
        print("."*27)
    finally:
        try:
            arch.close()
        except NameError:
            pass

def imprimirTarjeta(tarj):
    for i in range (len(tarj)):
        fecha = tarj[i][6].split("-")
        print()
        print("="*40)
        print("Tarjeta de embarque".center(40).upper())
        print("="*40)
        print("Nombre".ljust(20, '.') + str(tarj[i][2]).rjust(20, '.'))
        print("Apellido".ljust(20, '.') + str(tarj[i][1]).rjust(20, '.'))
        print("Código de reserva".ljust(20, '.') + str(tarj[i][0]).rjust(20, '.'))
        print("DNI".ljust(20, '.') + str(tarj[i][3]).rjust(20, '.'))
        print("Fecha".ljust(20, '.') + f"{fecha[2]} de {fecha[1]} de {fecha[0]}".rjust(20, '.'))
        print("Horario".ljust(20, '.') + str(tarj[i][7]).rjust(20, '.'))
        print("Origen".ljust(20, '.') + str(tarj[i][9]).rjust(20, '.'))
        print("Destino".ljust(20, '.') + str(tarj[i][10]).rjust(20, '.'))
        print("Asiento".ljust(20, '.')+ str(tarj[i][11]).rjust(20, '.'))
        print("="*40)

def eliminar_registro(codigo, apell, registro): #
    try:
        arch = open("reservas.txt", "rt")
        temp_arch = open("reservas_temp.txt", "wt")

        while True:
            linea = arch.readline()
            if not linea:
                break
            campos = linea.strip().split(";")
            if not (campos[0] == codigo and campos[1] == apell and campos[9] == registro[9] and campos[10] == registro[10]):
               temp_arch.write(linea)

        arch.close()
        temp_arch.close()

        arch = open("reservas.txt", "wt")
        temp_arch = open("reservas_temp.txt", "rt")
        for linea in temp_arch:
            arch.write(linea)
        
    except FileNotFoundError:
        print(f"\n{Fore.RED}❌ {Fore.WHITE}Archivo no encontrado")
        print("." * 27)
    except OSError:
        print(f"\n{Fore.RED}❌ {Fore.WHITE}Error al abrir el archivo")
        print("." * 27)
    finally:
        try:
            arch.close()
        except NameError:
            pass
        try:
            temp_arch.close()
        except NameError:
            pass

def elegirOrigenYDestino(provs, direc, prov_origen="", num_origen=""): #
    print(f"\n{direc} disponibles:")
    for i, prov in enumerate(provs, 1):
        if prov != prov_origen:
            print(f"{i}- {prov}")

    while True:
        try:
            prov_selec = int(input("Elija la opción que corresponda: ")) -1
        
            if not 0 <= prov_selec < len(provs):
                print(f"\n{Fore.RED}❌ {Fore.WHITE}Opción inválida. Intente nuevamente.")
                print("."*27)
            elif prov_selec == num_origen:
                    print(f"\n{Fore.RED}❌ {Fore.WHITE}El destino no puede ser igual al origen. Por favor, seleccione otro destino.")
                    print("."*27)
            else:
                break

        except ValueError:
            print(f"\n{Fore.RED}❌ {Fore.WHITE}Opción inválida. Intente nuevamente.")
            print("."*27)
    
    return prov_selec

def ingresarFecha():
    fecha_actual = time.localtime()
    while True:
        try:
            mes_anio = input("Ingrese mes y año que desea viajar en formato mm/aaaa: ")
            lista_ma = mes_anio.split("/")
            mes, anio = lista_ma
            
            if "/" not in mes_anio or len(lista_ma) != 2:
                print(f"\n{Fore.RED}❌ {Fore.WHITE}Formato inválido. Use el formato mm/aaaa.")
                print("."*27)
                continue
            
            if not (1 <= int(mes) <= 12):
                print(f"\n{Fore.RED}❌ {Fore.WHITE}Mes inválido. Debe ser un número entre 01 y 12.")
                print("."*27)
                continue
            
            if not (fecha_actual.tm_year <= int(anio) <= 2025):
                print(f"\n{Fore.RED}❌ {Fore.WHITE}Año inválido. Debe estar entre {fecha_actual.tm_year} y 2025.")
                print("."*27)
                continue
            
            if int(anio) == 2025 and int(mes) > 5:
                print(f"\n{Fore.RED}❌ {Fore.WHITE}Fecha inválida. Solo se permite ingresar una fecha hasta Mayo del 2025.")
                print("."*27)
                continue
            
            if int(anio) == fecha_actual.tm_year and int(mes) < fecha_actual.tm_mon:
                print(f"\n{Fore.RED}❌ {Fore.WHITE}Fecha inválida. Debe ser posterior a la fecha actual.")
                print("."*27)
                continue
            
            break
            
        except ValueError:
            print(f"\n{Fore.RED}❌ {Fore.WHITE}Formato inválido. Ingrese la fecha nuevamente")
            print("."*27)
    
    return int(mes), int(anio)

def diadelasemana(dia,mes,año):
    """Averigua el día de la semana para una fecha determinada, 0 para domingo"""
    if mes < 3:
        mes = mes + 10
        año = año - 1
    else:
        mes = mes - 2
    siglo = año // 100
    año2 = año % 100
    diasem = (((26*mes-2)//10)+dia+año2+(año2//4)+(siglo//4)-(2*siglo))%7
    if diasem < 0:
        diasem = diasem + 7
    return diasem

def imprimirFechas(m, a):
    lista_estados = []
    meses = {
        1: ("Enero", 31),
        2: ("Febrero", 29),
        3: ("Marzo", 31),
        4: ("Abril", 30),
        5: ("Mayo", 31),
        6: ("Junio", 30),
        7: ("Julio", 31),
        8: ("Agosto", 31),
        9: ("Septiembre", 30),
        10: ("Octubre", 31),
        11: ("Noviembre", 30),
        12: ("Diciembre", 31)
    }
    
    if a % 4 == 0 and (a % 100 != 0 or a % 400 == 0):
        meses[2] = ("Febrero", 29)

    mes, d = meses[m]

    calc_linea = diadelasemana(1,m,a)

    print("\n", mes.center(50).upper())
    print ("Dom", "Lun", "Mar", "Mié", "Jue", "Vie", "Sáb", sep="\t")

    print("\t" * (diadelasemana(1,m,a)), end="")
    
    try:
        arch = open("dias_disponibles.txt", "rt")
        for i in range(1, d +1):
            for registro in arch:
                if registro == f"{a}-{m:02}-{i:02}: true\n":
                    print(Fore.GREEN + f"{i}\t", end="")
                    lista_estados.append(True)
                    break
                elif registro == f"{a}-{m:02}-{i:02}: false\n":
                    print(Fore.RED + f"{i}\t", end="")
                    lista_estados.append(False)
                    break
            
            calc_linea += 1
            if calc_linea == 7:
                print("\n", end="")
                calc_linea = 0
            
            arch.seek(0)
            
    except FileNotFoundError:
        print(f"\n{Fore.RED}❌ {Fore.WHITE}Archivo no encontrado")
        print("."*27)
    except OSError:
        print(f"\n{Fore.RED}❌ {Fore.WHITE}Error al abrir el archivo")
        print("."*27)
    finally:
        try:
            arch.close()
        except NameError:
            pass
    print()
    return mes, lista_estados

def IngresarDia(e_fecha, d_selec_ida = 0, m_selec_ida = 0, a_selec_ida = 0, m_vuelt = 0, a_vuelt = 0): #
    while True:
        try:
            d_selec = int(input("• Seleccione un dia disponible: "))
            
            # Verificar si el día seleccionado está disponible
            if not (1 <= d_selec <= len(e_fecha)) or e_fecha[d_selec - 1] == False:
                print(f"\n{Fore.RED}❌ {Fore.WHITE}El día seleccionado no se encuentra disponible o está fuera de rango.")
                print("."*27)
                salir = input("\n• ¿Desea intentar con otro mes y año? (s/n): ").lower()
                if salir == 's':
                    d_selec = 0
                    break
                else:
                    continue

            # Verificar si es día de vuelta
            if d_selec_ida != 0 and m_selec_ida != 0:
                # Se evaluan los años, meses (si años son =), dias (si años y meses son =)
                if (a_vuelt < a_selec_ida) or (a_vuelt == a_selec_ida and m_vuelt < m_selec_ida) or (a_vuelt == a_selec_ida and m_vuelt == m_selec_ida and d_selec <= d_selec_ida):
                    print(f"\n{Fore.RED}❌ {Fore.WHITE}El día de vuelta debe ser posterior al día de ida.")
                    print("."*27)
                    salir = input("\n• ¿Desea intentar con otro mes y año? (s/n): ").lower()
                    if salir == 's':
                        d_selec = 0
                        break
                    else:
                        continue
                
            print(f"{Fore.GREEN}✔ {Fore.WHITE}Día asignado con éxito!")
            break
        
        except ValueError:
            print(f"\n{Fore.RED}❌ {Fore.WHITE}Debe ingresar un número")
            print("."*27)
        except IndexError:
            print(f"\n{Fore.RED}❌ {Fore.WHITE}Día fuera del rango, ingrese un día válido dentro del mes")
            print("."*27)
    
    return d_selec

def obtenerHorariosYPrecios(dest, orig, date): #
    # Diccionario con los destinos como claves y una lista de horarios como valores
    try:
        arch = open("horarios_precios.json", "rt")
        horarios_precios = json.load(arch)
    
        print(f"• Horarios y precios de {orig} a {dest} para el dia {date[1]} de {date[0]} del {date[2]}:")
        horarios = list(horarios_precios[orig][dest].items())
        for i, (horario, precio) in enumerate(horarios, 1):
                print(f"{i}: Horario: {horario} - Precio: {precio} pesos")
        
        seleccion = -1
        while seleccion < 0 or seleccion >= len(horarios):
            try:
                seleccion = int(input("Selecciona un horario (1, 2 o 3): ")) -1
                if 0 <= seleccion < len(horarios):
                    horario_seleccionado, precio_seleccionado = horarios[seleccion]
                    print(f"\n{Fore.GREEN}✔ {Fore.WHITE}Has seleccionado el horario: {horario_seleccionado} - Precio: {precio_seleccionado} pesos")
                else:
                    print(f"\n{Fore.RED}❌ {Fore.WHITE}Selección inválida. Por favor, intenta nuevamente.")
                    print("."*27)
            except ValueError:
                print(f"\n{Fore.RED}❌ {Fore.WHITE}Debe seleccionar un número")
                print("."*27)
        
        hp = (horario_seleccionado, precio_seleccionado)
        
    except FileNotFoundError:
        print(f"\n{Fore.RED}❌ {Fore.WHITE}Archivo no encontrado")
        print("."*27)
    except OSError:
        print(f"\n{Fore.RED}❌ {Fore.WHITE}Error al abrir el archivo")
        print("."*27)
    except ValueError:
        print(f"\n{Fore.RED}❌ {Fore.WHITE}Debe seleccionar un número")
        print("."*27)
    finally:
        try:
            arch.close()
        except NameError:
            pass   
    return hp

def completar_datos_pasajeros(total_pasajeros):
    datos_pasajeros = []
    for i in range(total_pasajeros):
        print(f"\n--- Datos del pasajero {i+1} ---")
        while True:
            nombre = input("• Ingrese el nombre: ").capitalize()
            if nombre.isalpha():
                break
            else:
                print(f"\n{Fore.RED}❌ {Fore.WHITE}Error: El nombre solo debe contener letras.")
                print("."*27)
        while True:
            apellido = input("• Ingrese el apellido: ").capitalize()
            if apellido.isalpha():
                break
            else:
                print(f"\n{Fore.RED}❌ {Fore.WHITE}Error: El apellido solo debe contener letras.")
                print("."*27)
        while True:
            dni = input("• Ingrese el DNI: ")
            if dni.isdigit() and 7 <= len(dni) <= 8:
                break
            else:
                print(f"\n{Fore.RED}❌ {Fore.WHITE}Error: El DNI debe ser numérico y tener entre 7 y 8 dígitos.")
                print("."*27)
        while True:
            try:
                edad = int(input("• Ingrese la edad: "))
                assert 0 < edad < 120
                break
            except ValueError:
                print(f"\n{Fore.RED}❌ {Fore.WHITE}Debe ingresar un número")
                print("."*27)
            except AssertionError:
                print(f"\n{Fore.RED}❌ {Fore.WHITE}Edad inválida. Debe ser un número positivo entre 0 y 120.")
                print("."*27)
        while True: 
            email = input("• Ingrese el correo electrónico: ")
            if verificarcorreo(email):
                break
            else:
                print(f"\n{Fore.RED}❌ {Fore.WHITE}Error: El correo electrónico no tiene un formato válido.")
                print("."*27)
                
        datos_pasajero = [nombre, apellido, dni, edad, email]
        datos_pasajeros.append(datos_pasajero)
        
    return datos_pasajeros

def verificarcorreo(correo):
    valido = True
    
    if correo.count("@") != 1:
        print(f"\n{Fore.RED}❌ {Fore.WHITE}Solamente es válido un @")
        print("."*27)
        return False
    
    usuario = correo[:correo.find("@")]
    if not usuario.isalnum():
        print(f"\n{Fore.RED}❌ {Fore.WHITE}Usuario erróneo")
        print("."*27)
        return False
    
    dominio = correo[correo.find("@") +1:correo.find(".")]
    if len(dominio) == 0:
        print(f"\n{Fore.RED}❌ {Fore.WHITE}Dominio debe tener al menos un carácter")
        print("."*27)
        return False
    
    resto = correo[correo.find('.'):]
    if resto != ".com" and resto != ".com.ar":
        print(f"\n{Fore.RED}❌ {Fore.WHITE}El correo debe finalizar con .com o .com.ar")
        print("."*27)
        return False
    
    return True

def seleccionarAsientos(lista_p, date, dest, orig, hp): #
    while True:
        try:
            """IMPRESIÓN DE ASIENTOS"""

            asientos_t = [[f"{i:02}{letra}" for letra in "ABCD"] for i in range(1, 12)] # Matriz, LISTA DE TODOS LOS ASIENTOS

            lista_seleccionados = [] # LISTA DE LOS ASIENTOS SELECCIONADOS POR LOS PASAJEROS

            asientos_ocupads = asientosOcupados(hp[0], orig, dest)

            for i in range(len(lista_p)): # POR C/ PASAJERO SE IMPRIME y SELECCIONA UN ASIENTO
                print(f"\nSeleccione un asiento disponible para {lista_p[i][0]}".center(40).upper())
                print(f"(Correspondiente al dia {date[1]} de {date[0]} del {date[2]})\n".center(40))
                
                # IMPRESIÓN DE ASIENTOS
                print("Frente".center(40))
                print("___------____________------___".center(40))
                print("/                              \\".center(40))
                imprimirAsientos(asientos_t, asientos_ocupads, lista_seleccionados)
                print("\\______________________________/".center(40))
                print("Fondo".center(40))
                
                # SELECCIÓN y VERIFICACIÓN DE DISPONIBILIDAD DE LOS ASIENTOS
                while True:
                    selec = input("\n• Seleccione: ").upper()
                    
                    # Verificar si el asiento existe
                    asiento_valido = buscar_asiento(asientos_t, selec)
                    """asiento_valido = False
                    for fila in asientos_t:
                        if selec in fila:
                            asiento_valido = True
                            break"""
                    
                    if not asiento_valido:
                        print(f"{Fore.RED}❌ {Fore.WHITE}El asiento seleccionado no existe. Seleccione un asiento válido")
                    elif selec in asientos_ocupads:
                        print(f"{Fore.RED}❌ {Fore.WHITE}El asiento seleccionado se encuentra ocupado. Seleccione un asiento válido")
                    else:
                        print(f"{Fore.GREEN}✔ {Fore.WHITE}Asiento asignado con éxito!")
                        break
                
                lista_seleccionados.append(selec)
                asientos_ocupads.append(selec)
            break
                
        except ValueError:
            print(f"\n{Fore.RED}❌ {Fore.WHITE}Debe ingresar un número")
            print("."*27)
        
    return lista_seleccionados

def buscar_asiento(asientos, selec, fila = 0): #
    """Funcion recursiva"""
    if fila >= len(asientos):
        return False # cuando se recorrieron todas las filas
    if selec in asientos[fila]:
        return True # si el asiento está en la fila actual
    return buscar_asiento(asientos, selec, fila + 1)  # busca en la siguiente fila

def asientosOcupados(hora, origen, destino):
    try:
        arch = open("reservas.txt", "rt")
        asientos_ocupados = []
        for registro in arch:
            asientos = registro.strip().split(";")
            if asientos[7] == hora and asientos[9] == origen and asientos[10] == destino:
                asientos_ocupados.append(asientos[11])

    except FileNotFoundError:
        print(f"\n{Fore.RED}❌ {Fore.WHITE}Archivo no encontrado")
        print("."*27)
    except OSError:
        print(f"\n{Fore.RED}❌ {Fore.WHITE}Error al abrir el archivo")
        print("."*27)
    finally:
        try:
            arch.close()
        except NameError:
            pass
    
    return asientos_ocupados

def imprimirAsientos(asientos_tot, lista_ocupados, lista_selec):
    """IMPRESIÓN y COLOREO DE ASIENTOS EN BASE A LA LISTA ESTADOS"""
    for f in range(len(asientos_tot)):
            # columnas A y B
        if asientos_tot[f][0] in lista_ocupados or asientos_tot[f][0] in lista_selec:
            print(f"{Fore.RED}|{str(asientos_tot[f][0]):^5}|".rjust(16), end="") # 2A
        else:
            print(f"{Fore.GREEN}|{str(asientos_tot[f][0]):^5}|".rjust(16), end="") # 2A
        if asientos_tot[f][1] in lista_ocupados or asientos_tot[f][1] in lista_selec:
            print(f"{Fore.RED}|{str(asientos_tot[f][1]):^5}|", end="") # 2B
        else:
            print(f"{Fore.GREEN}|{str(asientos_tot[f][1]):^5}|", end="") # 2B
            
        # Espacio interemdio
        print(" " * 4, end="")
            
            # columnas C y D
        if asientos_tot[f][2] in lista_ocupados or asientos_tot[f][2] in lista_selec:
            print(f"{Fore.RED}|{str(asientos_tot[f][2]):^5}|", end="") # 2C
        else:
            print(f"{Fore.GREEN}|{str(asientos_tot[f][2]):^5}|", end="") # 2C
        if asientos_tot[f][3] in lista_ocupados or asientos_tot[f][3] in lista_selec:
            print(f"{Fore.RED}|{str(asientos_tot[f][3]):^5}|") # 2D
        else:
            print(f"{Fore.GREEN}|{str(asientos_tot[f][3]):^5}|") # 2D

def simulacionPago(): #
    print("• Seleccione un método de pago:")
    print("1- Tarjeta de crédito")
    print("2- Tarjeta de débito")
    print("3- Transferencia bancaria")
    print("4- Pago en efectivo")
    
    while True:
        try:
            metodo = int(input("- "))
            
            # Tarjeta de crédito o débito
            if metodo == 1 or metodo == 2:
                tipo = "Crédito" if metodo == 1 else "Débito"
                print(f"\n{Fore.GREEN}✔ {Fore.WHITE}Ha seleccionado Tarjeta de {tipo}.")
                
                # Validar número de tarjeta
                while True:
                    tarjeta = input("• Ingrese el número de la tarjeta (16 dígitos): ")
                    if len(tarjeta) == 16 and tarjeta.isdigit():
                        break
                    print(f"\n{Fore.RED}❌ {Fore.WHITE}Número de tarjeta inválido. Debe tener 16 dígitos numéricos.")
                    print("."*27)
                
                # Validar nombre del titular
                while True:
                    nombre_titular = input("• Ingrese el nombre del titular: ").strip()
                    if nombre_titular:
                        break
                    print(f"\n{Fore.RED}❌ {Fore.WHITE}El nombre del titular no puede estar vacío.")
                    print("."*27)
                
                # Validar fecha de vencimiento
                while True:
                    vencimiento = input("• Ingrese la fecha de vencimiento (MM/AA): ")
                    if (len(vencimiento) == 5 and 
                        vencimiento[2] == "/" and 
                        vencimiento[:2].isdigit() and 
                        vencimiento[3:].isdigit() and 
                        1 <= int(vencimiento[:2]) <= 12):
                        break
                    print(f"\n{Fore.RED}❌ {Fore.WHITE}Fecha de vencimiento inválida. Debe estar en el formato MM/AA.")
                    print("."*27)
                
                # Validar CVV
                while True:
                    cvv = input("• Ingrese el CVV (3 dígitos): ")
                    if len(cvv) == 3 and cvv.isdigit():
                        break
                    print(f"\n{Fore.RED}❌ {Fore.WHITE}CVV inválido. Debe tener 3 dígitos numéricos.")
                    print("."*27)
                
                print("Procesando pago...")
                print(f"{Fore.GREEN}✔ {Fore.WHITE}Pago realizado con éxito.")
                break
            
            # Transferencia bancaria
            elif metodo == 3:
                print(f"\n{Fore.GREEN}✔ {Fore.WHITE}Ha seleccionado Transferencia Bancaria.")
                
                # Validar CBU o Alias
                while True:
                    cbu = input("• Ingrese el CBU o Alias de su cuenta bancaria: ")
                    if (len(cbu) == 22 and cbu.isdigit()) or cbu.isalnum():
                        break
                    print(f"\n{Fore.RED}❌ {Fore.WHITE}CBU/Alias inválido. Ingrese un CBU de 22 dígitos o un Alias válido.")
                    print("."*27)
                
                print("Procesando transferencia...")
                print(f"{Fore.GREEN}✔ {Fore.WHITE}Transferencia realizada con éxito.")
                break
            
            # Pago en efectivo
            elif metodo == 4:
                print("\nHa seleccionado Pago en Efectivo.")
                print("Diríjase a una sucursal para completar el pago.")
                print(f"{Fore.GREEN}✔ {Fore.WHITE}Reserva confirmada. Debe pagar antes de la fecha límite para mantener la reserva.")
                break
            
            else:
                print(f"\n{Fore.RED}❌ {Fore.WHITE}Opción inválida. Intente nuevamente.")
                print("."*27)
        
        except ValueError:
            print(f"\n{Fore.RED}❌ {Fore.WHITE}Debe ingresar un número válido.")
            print("."*27)

def resumirTotal(dest, orig, fecha, hora_precio, l_seleccionados, data_pasaj, cod_reserva): #
    for i in range(len(data_pasaj)):
        print()
        print("="*40)
        print("Resumen de compra".center(40).upper())
        print("="*40)
        print(f"{fecha[3]} --> {dest} a {orig}".center(40).upper())
        print("Fecha".ljust(20, '.') + str(f"{fecha[1]} de {fecha[0]} del {fecha[2]}").rjust(10, '.'))
        print("Horario".ljust(20, '.') + str(hora_precio[0]).rjust(20, '.'))
        print("Asiento".ljust(20, '.') + str(l_seleccionados[i]).rjust(20, '.'))
        print("Precio".ljust(20, '.') + str(hora_precio[1]).rjust(20, '.'))
        print("Codigo de reserva".ljust(20, '.') + str(cod_reserva).rjust(20, '.'))
        print()
        print("Nombre".ljust(20, '.') + str(data_pasaj[i][0]).capitalize().rjust(20, '.'))
        print("Apellido".ljust(20, '.') + str(data_pasaj[i][1]).capitalize().rjust(20, '.'))
        print("DNI".ljust(20, '.') + str(data_pasaj[i][2]).rjust(20, '.'))
        print("Email".ljust(20, '.') + str(data_pasaj[i][4]).rjust(20, '.'))
        print("="*40)

def guardarcompra(dest, orig, fecha, hora_precio, l_seleccionados, data_pasaj, cod_reserva): #
    try:
        arch = open("reservas.txt", "at")
        for i in range(len(data_pasaj)):
            linea=(f"{cod_reserva};{data_pasaj[i][1]};{data_pasaj[i][0]};{data_pasaj[i][2]};{data_pasaj[i][3]};{data_pasaj[i][4]};{fecha[2]}-{fecha[0]}-{fecha[1]};{hora_precio[0]};{hora_precio[1]};{orig};{dest};{l_seleccionados[i]}\n")
            arch.write(linea)
        
    except FileNotFoundError:
        print(f"\n{Fore.RED}❌ {Fore.WHITE}Archivo no encontrado")
        print("."*27)
    except OSError:
        print(f"\n{Fore.RED}❌ {Fore.WHITE}Error al abrir el archivo")
        print("."*27)
    finally:
        try:
            arch.close()
        except NameError:
            pass

def elegir_reserva(cod_reserv, apellid):
    try:
        arch = open("reservas.txt", "rt")
        reservas_encontradas = []
        for registro in arch:
            tarjeta = registro.strip().split(";")
            if tarjeta[0] == cod_reserv and tarjeta[1] == apellid:
                reservas_encontradas.append(tarjeta)
        
        if len(reservas_encontradas) >= 1:
            for i, reserva in enumerate(reservas_encontradas, 1):
                fech = reserva[6].split("-")
                print(f"{i}. {fech[2]} de {fech[1]} del {fech[0]} a las {reserva[7]}\n   Asiento: {reserva[11]}\n   Origen: {reserva[9]} --> Destino: {reserva[10]}\n")
        
        while True:
            try:
                seleccion = int(input("- "))-1
                assert 0 <= seleccion <= len(reservas_encontradas)
                registro_elegido = reservas_encontradas[seleccion]
                break
            except ValueError:
                print(f"\n{Fore.RED}❌ {Fore.WHITE}Debe seleccionar un número")
                print("."*27)
            except AssertionError:
                print(f"\n{Fore.RED}❌ {Fore.WHITE}Selección inválida. Por favor, intenta nuevamente.")
                print("."*27)
            except IndexError:
                print(f"\n{Fore.RED}❌ {Fore.WHITE}Selección inválida. Por favor, intenta nuevamente.")
                print("."*27)

    except FileNotFoundError:
        print(f"\n{Fore.RED}❌ {Fore.WHITE}Archivo no encontrado")
        print("."*27)
    except OSError:
        print(f"\n{Fore.RED}❌ {Fore.WHITE}Error al abrir el archivo")
        print("."*27)
    finally:
        try:
            arch.close()
        except NameError:
            pass
    
    return registro_elegido

def elegirOpcionDeCambio():
    print("Seleccione una opción de modificación:")
    print("1. Ajuste de Fecha")
    print("2. Reprogramación de Hora")
    print("3. Modificación de Origen y/o Destino")
    print("4. Selección de un Nuevo Asiento")
    print("5. Corrección de Datos Personales")
    
    while True:
        try:
            opcion = int(input("Ingrese el número de la opción que desea elegir: "))
            
            assert 0 < opcion < 6
            
            if opcion == 1:
                print("\nHa seleccionado: Ajuste de Fecha")
            elif opcion == 2:
                print("\nHa seleccionado: Reprogramación de Hora")
            elif opcion == 3:
                print("\nHa seleccionado: Modificación de Origen y/o Destino")
            elif opcion == 4:
                print("\nHa seleccionado: Selección de un Nuevo Asiento")
            elif opcion == 5:
                print("\nHa seleccionado: Corrección de Datos Personales")
            
            break
        
        except ValueError:
            print(f"\n{Fore.RED}❌ {Fore.WHITE}Debe ingresar un número válido.")
            print("."*27)
        except AssertionError:
            print(f"\n{Fore.RED}❌ {Fore.WHITE}Selección inválida. Por favor, intenta nuevamente.")
            print("."*27)
    
    return opcion

def modificar_reserva(reserva_eleg, option, provs):
    if option == 1:
        print("\n• Fechas válidas en sistema para sacar pasajes hasta el Mayo del 2025 inclusive")
        while True:
            m, a = ingresarFecha()
            mes_selec, est_fechas = imprimirFechas(m, a)
            dia_seleccionado = IngresarDia(est_fechas)
            if dia_seleccionado != 0:
                break
        fecha = (mes_selec, dia_seleccionado, a, "")
        hp = obtenerHorariosYPrecios(reserva_eleg[10], reserva_eleg[9], fecha)
        datos_pasajero = [[reserva_eleg[2], reserva_eleg[1], reserva_eleg[3], reserva_eleg[4], reserva_eleg[5]]]
        lista_seleccion_asientos = seleccionarAsientos(datos_pasajero, fecha, reserva_eleg[7], reserva_eleg[6], hp)

        eliminar_registro(reserva_eleg[0], reserva_eleg[1], reserva_eleg)
        guardarcompra(reserva_eleg[10], reserva_eleg[9], fecha, hp, lista_seleccion_asientos, datos_pasajero, reserva_eleg[0])
    elif opcion == 2:
        fecha_reserva = reserva_eleg[6].split("-")
        fecha = (fecha_reserva[1], fecha_reserva[2], fecha_reserva[0], "")
        hp = obtenerHorariosYPrecios(reserva_eleg[10], reserva_eleg[9], fecha)
        datos_pasajero = [[reserva_eleg[2], reserva_eleg[1], reserva_eleg[3], reserva_eleg[4], reserva_eleg[5]]]
        lista_seleccion_asientos = seleccionarAsientos(datos_pasajero, fecha, reserva_eleg[7], reserva_eleg[6], hp)

        eliminar_registro(reserva_eleg[0], reserva_eleg[1], reserva_eleg)
        guardarcompra(reserva_eleg[10], reserva_eleg[9], fecha, hp, lista_seleccion_asientos, datos_pasajero, reserva_eleg[0])
    elif opcion == 3:
        origen = elegirOrigenYDestino(provs, "Origenes")
        print(f"\n{Fore.GREEN}✔ {Fore.WHITE}Has seleccionado: {provs[origen]}")
        print("-"*50)
        destino = elegirOrigenYDestino(provs, "Destinos", provs[origen], origen)
        print(f"\n{Fore.GREEN}✔ {Fore.WHITE}Has seleccionado: {provs[destino]}")
        print("-"*50)
        print("\n• Fechas válidas en sistema para sacar pasajes hasta el Mayo del 2025 inclusive")
        while True:
            m, a = ingresarFecha()
            mes_selec, est_fechas = imprimirFechas(m, a)
            dia_seleccionado = IngresarDia(est_fechas)
            if dia_seleccionado != 0:
                break
        fecha = (mes_selec, dia_seleccionado, a, "")
        hp = obtenerHorariosYPrecios(provs[destino], provs[origen], fecha)
        datos_pasajero = [[reserva_eleg[2], reserva_eleg[1], reserva_eleg[3], reserva_eleg[4], reserva_eleg[5]]]
        lista_seleccion_asientos = seleccionarAsientos(datos_pasajero, fecha, reserva_eleg[10], reserva_eleg[9], hp)

        eliminar_registro(reserva_eleg[0], reserva_eleg[1], reserva_eleg)
        guardarcompra(provs[destino], provs[origen], fecha, hp, lista_seleccion_asientos, datos_pasajero, reserva_eleg[0])
    elif opcion == 4:
        datos_pasajero = [[reserva_eleg[2], reserva_eleg[1], reserva_eleg[3], reserva_eleg[4], reserva_eleg[5]]]
        fecha_reserva = reserva_eleg[6].split("-")
        fecha = (fecha_reserva[1], fecha_reserva[2], fecha_reserva[0], "")
        hp = (reserva_eleg[7], reserva_eleg[8])
        lista_seleccion_asientos = seleccionarAsientos(datos_pasajero, fecha, reserva_eleg[10], reserva_eleg[9], hp)

        eliminar_registro(reserva_eleg[0], reserva_eleg[1], reserva_eleg)
        guardarcompra(reserva_eleg[10], reserva_eleg[9], fecha, hp, lista_seleccion_asientos, datos_pasajero, reserva_eleg[0])
    elif opcion == 5:
        fecha_reserva = reserva_eleg[6].split("-")
        fecha = (fecha_reserva[1], fecha_reserva[2], fecha_reserva[0], "")
        hp = (reserva_eleg[7], reserva_eleg[8])
        datos_pasajero = completar_datos_pasajeros(1)
        lista_seleccion_asientos = [reserva_eleg[11]]

        eliminar_registro(reserva_eleg[0], reserva_eleg[1], reserva_eleg)
        guardarcompra(reserva_eleg[10], reserva_eleg[9], fecha, hp, lista_seleccion_asientos, datos_pasajero, reserva_eleg[0])

# Programa principal

provincias = ["Buenos Aires", "Misiones", "Salta", "Mendoza", "Santa Fe"]

print(f"{Fore.YELLOW}\n*** Bienvenido al Sistema de Venta de Pasajes UADEBUS ***")
print("-"*57)

inicio = True
while inicio != 3:
    try:
        print(f"\nIngrese la opción deseada:\n{Fore.YELLOW}1 -->{Fore.WHITE} CONSULTAR PASAJE\n{Fore.YELLOW}2 -->{Fore.WHITE} INICIAR COMPRA\n{Fore.YELLOW}3 -->{Fore.WHITE} FINALIZAR PROGRAMA")
        inicio=int(input("- "))
        
        assert 0 < inicio < 4
        
        if inicio == 1:
            volver = False
            while True and volver != True:
                cod_reserva = input("\n• Ingrese el código de reserva: ")
                apellido_reserva = input("• Ingrese su apellido: ").capitalize()
                pasaje = leerTarjeta(cod_reserva, apellido_reserva)
                if not pasaje == "":
                    imprimirTarjeta(pasaje)
                    while True:
                        try:
                            print(f"\nIngrese la opción deseada:\n{Fore.YELLOW}1 -->{Fore.WHITE} MODIFICAR RESERVA\n{Fore.YELLOW}2 -->{Fore.WHITE} CANCELAR RESERVA\n{Fore.YELLOW}3 -->{Fore.WHITE} VOLVER AL INICIO")
                            reserva = int(input("- "))
                            assert 0 < reserva < 4
                            if reserva == 1:
                                print(f"\nIndique cuáles de sus viajes modificar:\n")
                                reserva_elegida = elegir_reserva(cod_reserva, apellido_reserva)
                                opcion = elegirOpcionDeCambio()
                                modificar_reserva(reserva_elegida, opcion, provincias)
                                print(f"\n{Fore.GREEN}✔ {Fore.WHITE}Datos actualizados con éxito!")
                                print("."*27)
                                volver = True
                                break
                            elif reserva == 2:
                                print(f"\nIndique cuáles de sus viajes modificar:\n")
                                reserva_elegida = elegir_reserva(cod_reserva, apellido_reserva)
                                eliminar_registro(cod_reserva, apellido_reserva, reserva_elegida)
                                print(f"\n{Fore.GREEN}✔ {Fore.WHITE}Reserva cancelada con éxito!")
                                print("."*27)
                                volver = True
                                break
                            elif reserva == 3:
                                volver = True
                                break
                        except ValueError:
                            print(f"\n{Fore.RED}❌ {Fore.WHITE}Debe ingresar un número")
                            print("."*27)
                        except AssertionError:
                            print(f"\n{Fore.RED}❌ {Fore.WHITE}Las opciones válidas son 1, 2 o 3")
                            print("."*37)
                else:
                    respuesta = input("¿Desea intentar nuevamente? (s/n): ").lower()
                    if respuesta == "n":
                        break

        elif inicio == 2:
            """ORIGEN Y DESTINO"""
            origen = elegirOrigenYDestino(provincias, "Origenes")
            print(f"\n{Fore.GREEN}✔ {Fore.WHITE}Has seleccionado: {provincias[origen]}")
            print("-"*50)

            destino = elegirOrigenYDestino(provincias, "Destinos", provincias[origen], origen)
            print(f"\n{Fore.GREEN}✔ {Fore.WHITE}Has seleccionado: {provincias[destino]}")
            print("-"*50)
            
            """FECHAS"""
            print("• Fechas válidas en sistema para sacar pasajes hasta el Mayo del 2025 inclusive")

            while True:
                m_ida, a_ida = ingresarFecha()
                mes_selec_ida, est_fechas = imprimirFechas(m_ida, a_ida)
                dia_seleccionado_ida = IngresarDia(est_fechas)
                if dia_seleccionado_ida != 0:
                    break

            fecha_ida = (mes_selec_ida, dia_seleccionado_ida, a_ida, "IDA")

            vuelta = input("¿Desea seleccionar una fecha de regreso? (s/n): ").lower()
            if vuelta == 's':
                while True:
                    m_vuelta, a_vuelta = ingresarFecha()
                    mes_selec_vuelta, est_fechas = imprimirFechas(m_vuelta, a_vuelta)
                    dia_seleccionado_vuelta = IngresarDia(est_fechas, dia_seleccionado_ida, m_ida, a_ida, m_vuelta, a_vuelta)
                    
                    if dia_seleccionado_vuelta != 0:
                        break
                fecha_vuelta = (mes_selec_vuelta, dia_seleccionado_vuelta, a_vuelta, "VUELTA")
            else:
                fecha_vuelta = None
            
            print("-"*50)
            
            """HORARIOS Y PRECIOS"""
            if fecha_vuelta == None:
                hp_ida = obtenerHorariosYPrecios(provincias[destino], provincias[origen], fecha_ida)
                print("-"*50)
            else:
                hp_ida = obtenerHorariosYPrecios(provincias[destino], provincias[origen], fecha_ida)
                print()
                hp_vuelta = obtenerHorariosYPrecios(provincias[origen], provincias[destino], fecha_vuelta)
                print("-"*50)

            """LISTA DE PASAJEROS"""
            while True:
                try:
                    total_pasajeros = int(input("• Ingrese total de pasajeros: "))
                    datos_pasajeros = completar_datos_pasajeros(total_pasajeros) # Matriz
                    break
                except ValueError:
                    print(f"\n{Fore.RED}❌ {Fore.WHITE}Debe ingresar un número")
                    print("."*27)

            print("\nDatos de los pasajeros registrados:")
            for i, datos in enumerate(datos_pasajeros, 1):
                print(f"{Fore.GREEN}✔ {Fore.WHITE}\nPasajero {i}: Nombre: {datos[0]}, Apellido: {datos[1]}, DNI: {datos[2]}, Edad: {datos[3]}, Email: {datos[4]}")
            print("-"*50)
            
            """IMPRESIÓN DE ASIENTOS"""
            if fecha_vuelta == None:
                lista_seleccionados_ida = seleccionarAsientos(datos_pasajeros, fecha_ida, provincias[destino], provincias[origen], hp_ida)    
                for i in range(len(datos_pasajeros)):
                    print(f"\n{Fore.GREEN}✔ {Fore.WHITE}Asiento {lista_seleccionados_ida[i]} asignado a {datos_pasajeros[i][0]}")
                
                print("-"*50)
            else:
                lista_seleccionados_ida = seleccionarAsientos(datos_pasajeros, fecha_ida, provincias[destino], provincias[origen], hp_ida)    
                for i in range(len(datos_pasajeros)):
                    print(f"\n{Fore.GREEN}✔ {Fore.WHITE}Asiento {lista_seleccionados_ida[i]} asignado a {datos_pasajeros[i][0]}")
                
                print()
                
                lista_seleccionados_vuelta = seleccionarAsientos(datos_pasajeros, fecha_vuelta, provincias[origen], provincias[destino], hp_vuelta)    
                for i in range(len(datos_pasajeros)):
                    print(f"\n{Fore.GREEN}✔ {Fore.WHITE}Asiento {lista_seleccionados_vuelta[i]} asignado a {datos_pasajeros[i][0]}")
            
            """ RESUMEN DE PAGO """
            if fecha_vuelta == None:
                print(f"• El monto total a pagar es $ {hp_ida[1] * total_pasajeros}")
            else:
                print(f"• El monto total a pagar es $ {(hp_ida[1] + hp_vuelta[1]) * total_pasajeros}")
            
            simulacionPago() 
            
            """ GUARDAR RESERVA """
            codigoreserva= random.randint(0,999999)
            guardarcompra(provincias[destino], provincias[origen], fecha_ida, hp_ida, lista_seleccionados_ida, datos_pasajeros, codigoreserva)
            if vuelta == "s":
                guardarcompra(provincias[origen], provincias[destino], fecha_vuelta, hp_vuelta, lista_seleccionados_vuelta, datos_pasajeros, codigoreserva)
            
            """RESUMEN TOTAL"""
            if fecha_vuelta == None:
                resumirTotal(provincias[destino], provincias[origen], fecha_ida, hp_ida, lista_seleccionados_ida, datos_pasajeros, codigoreserva)
            else:
                resumirTotal(provincias[destino], provincias[origen], fecha_ida, hp_ida, lista_seleccionados_ida, datos_pasajeros, codigoreserva)
                resumirTotal(provincias[origen], provincias[destino], fecha_vuelta, hp_vuelta, lista_seleccionados_vuelta, datos_pasajeros, codigoreserva)
        else:
            break
        
    except ValueError:
        print(f"\n{Fore.RED}❌ {Fore.WHITE}Debe ingresar un número")
        print("."*27)
    except AssertionError:
        print(f"\n{Fore.RED}❌ {Fore.WHITE}Las opciones válidas son 1, 2 o 3")
        print("."*37)
    

        
