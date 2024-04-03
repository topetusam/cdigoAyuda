# from tabulate import tabulate
# import json
# import requests
# import modules.getActivos as asigActivos
# import modules.getPersonas as asigPersonas
# import modules.getZonas as asigZonas
# from datetime import datetime



# def getGenerateData():
#     peticion= requests.get("http://154.38.171.54:5503/activos")
#     data=peticion.json()
#     return data



# def getEstados():
#     for val in asigActivos.getAllData():
#         if val.get("idEstado") == "0":
#             print("El activo no a sido asignado")
#         elif val.get("idEstado") == "1":
#             print("El activo ha sido asignado")
#         elif val.get("idEstado") == "2":
#             print("El activo ha sido dado de baja por daño")
#         elif val.get("idEstado") == "3":
#             print("El activo ha sido enviado a la garantia")
#         elif val.get("idEstado") == "4":
#             print("El activo ha sido reasignado")
#         else:
#             break    



# def generar_historial(id, fecha, tipomov, id_resp_movimiento):
#     id_resp_movimiento = int(input("Ingrese el id del responsable: "))
#     historial = {
#         "NroId": id,
#         "Fecha": fecha,
#         "tipoMov": str(tipomov),
#         "idRespMov": str(id_resp_movimiento)
#     }
#     return historial


# def asignar_activo_a_persona():
#     id_activo = input("Ingrese el ID del activo que desea asignar: ")
#     id_persona = input("Ingrese el ID de la persona a la que desea asignar el activo: ")
    
#     activo_encontrado = None
#     for val in asigActivos.getAllData():
#         if val.get("id") == id_activo or val.get("id") == int(id_activo):
#             activo_encontrado = val
#             break
#     if not activo_encontrado:
#         print("El activo con el ID ingresado no existe.")
#         return
    
#     if val.get("idEstado")== "2":
#         print("El activo esta dado de baja y no se puede asignar")
#         return
    
#     if val.get("idEstado")== "3":
#         print("El activo esta en garantia y no se puede asignar")
#         return

#     if val.get("idEstado")== "1":
#         print("El activo ya se encuentra asignado")
#         return

#     persona_encontrada = None
#     for val in asigPersonas.getAllData():
#         if val.get("id") == id_persona or val.get("id") == int(id_persona):
#             persona_encontrada = val
#             break
#     if not persona_encontrada:
#         print("La persona con el ID ingresado no existe.")
#         return
    
#     fecha_asignacion = datetime.now().strftime("%Y-%m-%d")
#     tipo_asignacion = "Personal"
    
#     asignacion = {
#         "NroAsignacion": (id_activo),
#         "FechaAsignacion": fecha_asignacion,
#         "TipoAsignacion": tipo_asignacion,
#         "AsignadoA": persona_encontrada.get("Nombre")
#     }
    

#     if "asignaciones" not in activo_encontrado:
#         activo_encontrado["asignaciones"] = []
#     activo_encontrado["asignaciones"].append(asignacion)
    
#     historial_asignacion = generar_historial(id_activo, fecha_asignacion, 1, id_persona)
    
#     if "historialActivos" not in activo_encontrado:
#         activo_encontrado["historialActivos"] = []
#     activo_encontrado["historialActivos"].append(historial_asignacion)

#     if activo_encontrado.get("idEstado") == "0":
#         activo_encontrado["idEstado"] = "1"
#         url_estado = f"http://154.38.171.54:5503/activos/{id_activo}"
#         peticion_estado = requests.put(url_estado, data=json.dumps({"idEstado": "1"}))
#         if peticion_estado.status_code == 200:
#             print("Estado del activo actualizado correctamente.")
#         else:
#             print("Error al actualizar el estado del activo.")
#             return    


#     peticion = requests.put(f"http://154.38.171.54:5503/activos/{id_activo}", data=json.dumps(activo_encontrado))
#     res = peticion.json()
#     if peticion.status_code == 200:
#         print("Activo asignado correctamente.")

#     else:
#         print("Error al asignar el activo.")



# def asignar_activo_a_zona():
#     id_activo = input("Ingrese el ID del activo que desea asignar: ")
#     id_zona = input("Ingrese el ID de la zona a la que desea asignar el activo: ")
    
#     activo_encontrado = None
#     for val in asigActivos.getAllData():
#         if val.get("id") == id_activo or val.get("id") == int(id_activo):
#             activo_encontrado = val
#             break
#     if not activo_encontrado:
#         print("El activo con el ID ingresado no existe.")
#         return
#     if val.get("idEstado")== "2":
#         print("El activo esta dado de baja y no se puede asignar")
#         return
    
#     if val.get("idEstado")== "3":
#         print("El activo esta en garantia y no se puede asignar a ninguna zona")
#         return
    
#     if val.get("idEstado")== "1":
#         print("El activo ya se encuentra asignado")
#         return
    
#     zona_encontrada = None
#     for val in asigZonas.getAllData():
#         if val.get("id") == id_zona or val.get("id") == int(id_zona):
#             zona_encontrada = val
#             break
#     if not zona_encontrada:
#         print("La Zona con el ID ingresado no existe.")
#         return
    
#     fecha_asignacion = datetime.now().strftime("%Y-%m-%d")
#     tipo_asignacion = "Zona"
    
#     asignacion = {
#         "NroAsignacion": (id_activo),
#         "FechaAsignacion": fecha_asignacion,
#         "TipoAsignacion": tipo_asignacion,
#         "AsignadoA": zona_encontrada.get("id")
#     }
    

#     if "asignaciones" not in activo_encontrado:
#         activo_encontrado["asignaciones"] = []
#     activo_encontrado["asignaciones"].append(asignacion)
    
#     historial_asignacion = generar_historial(id_activo, fecha_asignacion, 1, id_zona)
    
#     if "historialActivos" not in activo_encontrado:
#         activo_encontrado["historialActivos"] = []
#     activo_encontrado["historialActivos"].append(historial_asignacion)

#     if activo_encontrado.get("idEstado") == "0":
#         activo_encontrado["idEstado"] = "1"
#         url_estado = f"http://154.38.171.54:5503/activos/{id_activo}"
#         peticion_estado = requests.put(url_estado, data=json.dumps({"idEstado": "1"}))
#         if peticion_estado.status_code == 200:
#             print("Estado del activo actualizado correctamente.")
#         else:
#             print("Error al actualizar el estado del activo.")
#             return    


#     peticion = requests.put(f"http://154.38.171.54:5503/activos/{id_activo}", data=json.dumps(activo_encontrado))
#     res = peticion.json()
#     if peticion.status_code == 200:
#         print("Activo asignado correctamente.")

#     else:
#         print("Error al asignar el activo.")
    





# def eliminarAsignacion(id):
#         idasignacion=input("ingrese el numero de id de la asignacion para eliminarla: ")
#         for val in getGenerateData():
#             for val in val.get("asignaciones", []):
#                 if idasignacion == val.get("NroAsignacion"):
#                     peticion = requests.delete(f"http://154.38.171.54:5503/activos/{id}/asignaciones/{idasignacion}")
#                     if peticion.status_code == 204:
#                         print("Asignación eliminada correctamente.")
#                         return
#                     else:
#                         print("Error al eliminar la asignación.")
#                         return
#         print("No se encontro ninguna Asignacion")
