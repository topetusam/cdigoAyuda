# from tabulate import tabulate 
# import requests
# import json
# import os
# import modules.getActivos as gActivos
# import modules.getPersonas as gPersonas
# import modules.getMovActivos as gTipoMovActivos
# import modules.getAsignacionActivos as gAActivos

# import modules.getZonas as gZonas
# import modules.getReportes as gReportes  




# # print(tabuzip_fileip_fileip_fileate(gPersonas.getEliminarPersona("ab951234-e724-47b0-889a-33fad0797124")["body"], headers="keys", tablefmt="github"))
# # print(tabulate(gAActivos.asignar_activo_a_persona(), headers="keys", tablefmt="github"))
# # print(tabulate(gAActivos.eliminarAsignacion(), headers="keys", tablefmt="github"))



# def menuActivos():
#         while True:
        
#             print("""
                  
#   __  __ _____ _   _ _   _                  
#  |  \/  | ____| \ | | | | |                 
#  | |\/| |  _| |  \| | | | |                 
#  | |  | | |___| |\  | |_| |                 
#  |_| _|_|_____|_____|_____     _____  ____  
#     / \  / ___|_   _|_ _\ \   / / _ \/ ___| 
#    / _ \| |     | |  | | \ \ / / | | \___ \ 
#   / ___ \ |___  | |  | |  \ V /| |_| |___) |
#  /_/   \_\____| |_| |___|  \_/  \___/|____/ 
                                            

#                 1. AGREGAR
#                 2. EDITAR
#                 3. ELIMINAR
#                 4. BUSCAR
#                 5. REGRESAR AL MENNU PRINCIPAL
                
            
#                 """)
#             opcion = int(input("\nSelecione una de las opciones: "))
#             if(opcion == 1):
#                 gActivos.menu()
#             if(opcion == 2):
#                 gActivos.menu2()
#             if(opcion == 3):
#                 gActivos.menu1()
#             if(opcion == 4):
#                 print(tabulate(gActivos.getBuscarActivo(), headers="keys", tablefmt="github"))
#             if (opcion == 5):
#                 break

# def menuPersona():
    
#         while True:
            
#             print("""
#  __  __ _____ _   _ _   _                          
#  |  \/  | ____| \ | | | | |                         
#  | |\/| |  _| |  \| | | | |                         
#  | |  | | |___| |\  | |_| |                         
#  |____|___________\______/ ___  _   _    _    ____  
#  |  _ \| ____|  _ \/ ___| / _ \| \ | |  / \  / ___| 
#  | |_) |  _| | |_) \___ \| | | |  \| | / _ \ \___ \ 
#  |  __/| |___|  _ < ___) | |_| | |\  |/ ___ \ ___) |
#  |_|   |_____|_| \_\____/ \___/|_| \_/_/   \_\____/ 
                                                    

#                 1. AGREGAR
#                 2. EDITAR
#                 3. ELIMINAR
#                 4. BUSCAR
#                 5. REGRESAR AL MENU PRINCIPAL
                
            
#                 """)
#             opcion = int(input("\nSelecione una de las opciones: "))
#             if(opcion == 1):
#                 gPersonas.menu()
#             if(opcion == 2):
#                 gPersonas.menu2()
#             if(opcion == 3):
#                 gPersonas.menu1()
#             if(opcion == 4):
#                 print(tabulate(gPersonas.getBuscarPersona(), headers="keys", tablefmt="github"))
#             if (opcion == 5):
#                 break
          
# def menuZonas():
     
#      while True:
            
#             print("""
#   __  __ _____ _   _ _   _      
#  |  \/  | ____| \ | | | | |     
#  | |\/| |  _| |  \| | | | |     
#  | |  | | |___| |\  | |_| |     
#  |____________|__ \_|____/____  
#  |__  / _ \| \ | |  / \  / ___| 
#    / / | | |  \| | / _ \ \___ \ 
#   / /| |_| | |\  |/ ___ \ ___) |
#  /____\___/|_| \_/_/   \_\____/ 
                                
#                 1. AGREGAR
#                 2. EDITAR 
#                 3. ELIMINAR
#                 4. BUSCAR
#                 5. REGRESAR AL MENU PRINCIPAL
                
            
#                 """)
#             opcion = int(input("\nSelecione una de las opciones: "))
#             if(opcion == 1):
#                 gZonas.menu()
#             if(opcion == 2):
#                 gZonas.menu2()
#             if(opcion == 3):
#                 gZonas.menu1()
#             if(opcion == 4):
#                 print(tabulate(gZonas.getBuscarZona(), headers="keys", tablefmt="github"))
#             if (opcion == 5):
#                 break

# def menuAsignacionActivos():
    
#         while True:
            
#             print("""
#   __  __ _____ _   _ _   _                                 
#  |  \/  | ____| \ | | | | |                                
#  | |\/| |  _| |  \| | | | |                                
#  | |  | | |___| |\  | |_| |                                
#  |_| _|_|_____|___\______/  _    _    ____ ___ ___  _   _  
#     / \  / ___|_ _/ ___| \ | |  / \  / ___|_ _/ _ \| \ | | 
#    / _ \ \___ \| | |  _|  \| | / _ \| |    | | | | |  \| | 
#   / ___ \ ___) | | |_| | |\  |/ ___ \ |___ | | |_| | |\  | 
#  /_/ _ \_\____/___________ \_/_______\____|___\___/|_| \_| 
#     / \  / ___|_   _|_ _\ \   / / _ \/ ___|                
#    / _ \| |     | |  | | \ \ / / | | \___ \                
#   / ___ \ |___  | |  | |  \ V /| |_| |___) |               
#  /_/   \_\____| |_| |___|  \_/  \___/|____/                
                                                           

#                 1. CREAR ASIGNACION
#                 2. BUSCAR ASIGNACION
#                 3. REGRESAR AL MENU PRINCIPAL

                
            
#                 """)
#             opcion = int(input("\nSelecione una de las opciones: "))
#             if(opcion == 1):
#                 print("""
#                       1.Asignar activo a zona
#                       2.Asignar activo a Personal
#                       """)
#                 opcion1 = int(input("Seleccione una de las opciones: "))
#                 if(opcion1 == 1):
#                     print(tabulate(gAActivos.asignar_activo_a_zona(), headers="keys", tablefmt="github"))
#                 if (opcion1 ==2):
#                      print(tabulate(gAActivos.asignar_activo_a_persona(), headers="keys", tablefmt="github"))       
#             if(opcion == 2):
#                 print(tabulate(gAActivos.buscarAsignacion(), headers="keys", tablefmt="github"))
#             if(opcion == 3):
#                 break



# def menuReportes():
    
#         while True:
            
#             print("""
#  __  __ _____ _   _ _   _                       
#  |  \/  | ____| \ | | | | |                      
#  | |\/| |  _| |  \| | | | |                      
#  | |  | | |___| |\  | |_| |                      
#  |____|___________\_|____/____ _____ _____ ____  
#  |  _ \| ____|  _ \ / _ \|  _ \_   _| ____/ ___| 
#  | |_) |  _| | |_) | | | | |_) || | |  _| \___ \ 
#  |  _ <| |___|  __/| |_| |  _ < | | | |___ ___) |
#  |_| \_\_____|_|    \___/|_| \_\|_| |_____|____/ 
                                                 

#                 1. LISTAR TODOS LOS ACTIVOS
#                 2. LISTAR ACTIVOS POR CATEGORIA
#                 3. LISTAR ACTIVOS DADOS DE BAJA POR DAÑO 
#                 4. LISTAR ACTIVOS Y ASIGNACION
#                 5  LISTAR HISTORIAL DE MOV. DE ACTIVO
#                 6. REGRESAR AL MENU PRINCIPAL

                
            
#                 """)
#             opcion = int(input("\nSelecione una de las opciones: "))
#             if(opcion == 1):
#                 print(tabulate(gReportes.getActivosLista(), headers="keys", tablefmt = 'rounded_grid'))
#             if(opcion == 2):
#                 print(tabulate(gReportes.getActivosCategoria(), headers="keys", tablefmt = 'rounded_grid'))
#             if(opcion == 3):
#                 print(tabulate(gReportes.getActivosDadosdeBaja(), headers="keys", tablefmt = 'rounded_grid'))
#             if(opcion == 4):
#                 print(tabulate(gReportes.getActivosAsignacion(), headers="keys", tablefmt = 'rounded_grid'))
#             if (opcion == 5):
#                 print(tabulate(gReportes.getActivosHistorial(), headers="keys", tablefmt = 'rounded_grid'))
#             elif(opcion == 6):
#                 break

# def menuMovimientodeActivos():
#         while True:
            
#             print("""
#   __  __ _____ _   _ _   _                                   
#  |  \/  | ____| \ | | | | |                                  
#  | |\/| |  _| |  \| | | | |                                  
#  | |  | | |___| |\  | |_| |                                  
#  |__  __|_______| \______/__  __ ___ _____ _   _ _____ ___   
#  |  \/  |/ _ \ \   / /_ _|  \/  |_ _| ____| \ | |_   _/ _ \  
#  | |\/| | | | \ \ / / | || |\/| || ||  _| |  \| | | || | | | 
#  | |  | | |_| |\ V /  | || |  | || || |___| |\  | | || |_| | 
#  |_| _|_|\____ _____ ______|  |_____|_____|_| \_| |_| \___/  
#     / \  / ___|_   _|_ _\ \   / / _ \/ ___|                  
#    / _ \| |     | |  | | \ \ / / | | \___ \                  
#   / ___ \ |___  | |  | |  \ V /| |_| |___) |                 
#  /_/   \_\____| |_| |___|  \_/  \___/|____/                  
                                                             

#                 1. RETORNO DE ACTIVOS
#                 2. DAR DE BAJA ACTIVO
#                 3. CAMBIAR ASIGNACION DE ACTIVO
#                 4. ENVIAR A GARANTIA A ACTIVO
#                 5. REGRESAR AL MENU PRINCIPAL

                
            
#                 """)
#             opcion = int(input("\nSelecione una de las opciones: "))
#             if(opcion == 1):
#                 gTipoMovActivos.getretornoEstado()
#             if(opcion == 2):
#                 gTipoMovActivos.getDarDeBajaPorDaño()
#             if(opcion == 3):
#                 gTipoMovActivos.getCambiarAsignacionActivo()
#             if(opcion == 4):
#                 gTipoMovActivos.getEnviarAgarantiaActivo()
#             if (opcion == 5):
#                 break

# if (__name__=='__main__'):
#     while True:
            
#             os.system("clear")
#             print("""
#  ____ ___ ____ _____ _____ __  __    _                                  
#  / ___|_ _/ ___|_   _| ____|  \/  |  / \                                 
#  \___ \| |\___ \ | | |  _| | |\/| | / _ \                                
#   ___) | | ___) || | | |___| |  | |/ ___ \                               
#  |____/________/ |_| |_____|_|  |_/_/   \_\                              
#  |  _ \| ____|                                                           
#  | | | |  _|                                                             
#  | |_| | |___                                                            
#  |_____|_____|____ _____ ___ ___  _   _                                  
#   / ___| ____/ ___|_   _|_ _/ _ \| \ | |                                 
#  | |  _|  _| \___ \ | |  | | | | |  \| |                                 
#  | |_| | |___ ___) || |  | | |_| | |\  |                                 
#   _____|_____|_____ __| ____\__________|_   _ _____  _    ____  ___ ___  
#  |  _ \| ____| |_ _| \ | \ \   / / ____| \ | |_   _|/ \  |  _ \|_ _/ _ \ 
#  | | | |  _|    | ||  \| |\ \ / /|  _| |  \| | | | / _ \ | |_) || | | | |
#  | |_| | |___   | || |\  | \ V / | |___| |\  | | |/ ___ \|  _ < | | |_| |
#  |____/|_____| |___|_| \_|  \_/  |_____|_| \_| |_/_/   \_\_| \_\___\___/ 
                                                                         

                  
#                 1. ACTIVOS 
#                 2. PERSONAL
#                 3. ZONAS
#                 4. ASIGNACION DE ACTIVOS
#                 5. REPORTES
#                 6. MOVIMIENTO DE ACTIVOS
#                 7. SALIR  
            
#                 """)
#             opcion = int(input("\nSelecione una de las opciones: "))
            
#             if(opcion == 1):
#                 menuActivos()
#             if(opcion == 2):
#                 menuPersona()
#             if(opcion == 3):
#                 menuZonas()
#             if(opcion == 4):
#                 menuAsignacionActivos()
#             if (opcion == 5):
#                 menuReportes()
#             if (opcion == 6):
#                 menuMovimientodeActivos()        
#             elif(opcion == 7):

#                 break