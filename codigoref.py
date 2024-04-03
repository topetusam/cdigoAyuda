# from tabulate import tabulate
# import json
# import requests


# def getAllData():
#     peticion= requests.get("http://154.38.171.54:5503/zonas")
#     data=peticion.json()
#     return data

# def getAllZona(id):
#     peticion= requests.get(f"http://154.38.171.54:5503/zonas/{id}")
#     return[peticion.json()] if peticion.ok else []


# def getAgregarZona():
    

#     while True:
#         zona = {
#        "nombreZona": input("ingrese la nueva zona de CAMPUS: "),
#       "totalCapacidad": int(input("Ingrese la capacidad de la zona: "))
#         }

#         peticion = requests.post("http://154.38.171.54:5503/zonas", data=json.dumps(zona))
#         res = peticion.json() 
#         res["mensaje"] = "Producto Guardado"
#         print(tabulate([res], headers="keys", tablefmt="github"))
#         input("Presione una tecla para continuar.....")
#         break
    
# def getEliminarZona(id):
#         data = getAllZona(id)
#         if(len(data)):       
             
#              peticion = requests.delete(f"http://154.38.171.54:5503/zonas/{id}")
#              if(peticion.status_code == 204):
#                     data.append({"message": "producto eliminado correctamente"})
#                     return {
#                 "body": data, 
#                 "status": peticion.status_code,
#             }
#         else:
#             return {
#             "body":[{
#                 "message":"producto no encontrado",
#                 "id": id
#             }],
#             "status": 400,
#         }

# def EditarZona(id):
#     Zona = {
#             1: "nombreZona",
#       2: "totalCapacidad"            
#     }

#     persona_existente = getAllZona(id)
#     if not persona_existente:
#         return {"mensaje": "Producto no encontrado"}

#     producto_actualizado = persona_existente[0].copy()
    
#     for key, value in Zona.items():
#           print(f"{key}. {value}")

#     opciondeseada=int(input("seleccione el dato que desea cambiar: "))
#     if opciondeseada not in Zona.keys():
#         return {"mensaje": "dato no encontrado"}

#     if Zona[opciondeseada] == "totalCapacidad":
#         nuevovalor = int(input(f"Ingrese el nuevo valor para {Zona[opciondeseada]}: "))
#     else:
#         nuevovalor = input(f"Ingrese el nuevo valor para {Zona[opciondeseada]}: ")

#     producto_actualizado[Zona[opciondeseada]]=nuevovalor


#     peticion = requests.put(f"http://154.38.171.54:5503/zonas/{id}", data=json.dumps(producto_actualizado))
#     res = peticion.json()

#     if peticion.status_code == 200:
#         res["mensaje"] = "Producto actualizado correctamente"
#     else:
#         res["mensaje"] = "Error al actualizar el producto"
    
#     return [res]


# def getBuscarZona():
#     BuscarZona= []
#     buscar=int(input("ingrese el id para mostrar la zona: "))
#     for val in getAllData():
#         if buscar == val.get("id"):
#             BuscarZona.append({
#                 "nombre": val.get("nombreZona"),
#                 "capacidad": val.get("totalCapacidad"),
#                 "id": val.get("id")
#             }
#             )
#     return BuscarZona





# def menu():
#     while True:
#         print("""  
#    ____ _   _   _    ____  ____    _    ____  
#   / ___| | | | / \  |  _ \|  _ \  / \  |  _ \ 
#  | |  _| | | |/ _ \ | |_) | | | |/ _ \ | |_) |
#  | |_| | |_| / ___ \|  _ <| |_| / ___ \|  _ < 
#   ____________/ _ \_\_| \_\____/_/   \_\_| \_\
#  |__  / _ \| \ | |  / \                       
#    / / | | |  \| | / _ \                      
#   / /| |_| | |\  |/ ___ \                     
#  /____\___/|_| \_/_/   \_\                    
                                                     
                                                                                                                                                    
#             1. GUARDAR UNA ZONA NUEVA
#             0. ATRAS
          
#           """)        
#         opcion = int(input("\nSelecione una de las opciones: "))
#         if(opcion == 1):
#             print(tabulate(getAgregarZona(), headers="keys", tablefmt="github"))
#             input("Precione una tecla para continuar.....")
#         elif(opcion == 0):
#             break

# def menu1():
#     while True:
#         print("""  
#  _____ _     ___ __  __ ___ _   _    _    ____  
#  | ____| |   |_ _|  \/  |_ _| \ | |  / \  |  _ \ 
#  |  _| | |    | || |\/| || ||  \| | / _ \ | |_) |
#  | |___| |___ | || |  | || || |\  |/ ___ \|  _ < 
#  |___________|___|_| _|_|___|_| \_/_/   \_\_| \_\
#  |__  / _ \| \ | |  / \                          
#    / / | | |  \| | / _ \                         
#   / /| |_| | |\  |/ ___ \                        
#  /____\___/|_| \_/_/   \_\                       
                                                                     
                                                                                                                                                    
#             1. ELIMINAR UNA ZONA
#             0. ATRAS
          
#           """)        
#         opcion = int(input("\nSelecione una de las opciones: "))
#         if(opcion == 1):
#             IdActivo = input("Ingrese el id de la persona que desea eliminar: ")
#             print(tabulate(getEliminarZona(IdActivo), headers="keys", tablefmt="github"))

#             input("Precione una tecla para continuar.....")
#         elif(opcion == 0):
#             break
# def menu2():
    
#     while True:
#         print("""  
#      _    ____ _____ _   _   _    _     ___ _____   _    ____  
#     / \  / ___|_   _| | | | / \  | |   |_ _|__  /  / \  |  _ \ 
#    / _ \| |     | | | | | |/ _ \ | |    | |  / /  / _ \ | |_) |
#   / ___ \ |___  | | | |_| / ___ \| |___ | | / /_ / ___ \|  _ < 
#  /____________| __|  ____/_/   \_\_____|___/____/_/   \_\_| \_\
#  |__  / _ \| \ | |  / \                                        
#    / / | | |  \| | / _ \                                       
#   / /| |_| | |\  |/ ___ \                                      
#  /____\___/|_| \_/_/   \_\                                     
                                                                                    
                                                                                                                                                    
#             1. ACTUALIZR DATOS DE UNA ZONA
#             0. ATRAS
          
#           """)        
#         opcion = int(input("\nSelecione una de las opciones: "))
#         if(opcion == 1):
#             id = input("Ingrese el id de la Zona que desea actualizar: ")
#             print(tabulate(EditarZona(id), headers="keys", tablefmt="github"))
#             input("Precione una tecla para continuar.....")
#         elif(opcion == 0):
#             break